'''
V1
c Jimmy Yue
credits to http://effbot.org/zone/python-code-generator.htm for inspiration
'''

import json
import re
import uuid
import os
from collections import defaultdict
from collections import namedtuple

# TODO: Go over existing code -> Cleanup
# TODO: Pickle Pickle Pickle
# TODO: Better tracking of what's been changed and what hasn't

# TODO: Code gen/regen, can actually do a mix of methodology. Biggest problem in my head is the dependency
#       between the route gen and the handler gen. Current idea: regenerate handlers all the time
#       Ideas: Use a pointer system

"""
venom.ui(
app.GET('/thing', Handler)
, GUID)

or

venom.ui(
app.GET('/thing', Handler).query({
  'thing': None
}), GUID)
"""


Codeblock = namedtuple('Codeblock', 'content, index')


class VenomGen(object):
    def __init__(self):
        self.level = 0
        self.applications = defaultdict(Codeblock)
        self.imports = []
        self.routes = defaultdict(Codeblock)
        self.handlers = []
        self.tab = "    "
        self.guids = set()
        self.file = []
        self.changes = []

    # Basic write functionalities
    # def write(self, string):
    #     self.routes.append(self.block() + string + "\n")

    def indent(self, degree=1):
        self.level = self.level + degree

    def dedent(self, degree=1):
        if self.level - degree < 0:
            raise SyntaxError("Cannot dedent below level 0")
        self.level = self.level - degree

    def generate(self, file_name):
        with open(file_name + ".py", "w") as file:
            for change in self.changes:
                index = change.index
                content = change.content
                if index:
                    self.file[index] = content
                else:
                    self.file.append(content)
            for line in self.file:
                file.write(line)

            # for line_number in range(len(self.file)):
            #     line = self.file[line_number]
            # # Header Generation
            # for line in self.imports:
            #     file.write(line)
            #     self.is_application(line)
            # file.write("\n\n")
            #
            # for app in self.applications.values():
            #     file.write(app + "\n")
            # file.write("\n")
            #
            # # Handler Generation
            # for handler in self.handlers:
            #     for line in handler[2]:
            #         file.write(line)
            #     file.write("\n")
            # file.write("\n")
            #
            # # Code Generation (Codeblocks, Models, Etc.)
            # for route in self.routes.values():
            #     file.write(route.content)
            #     file.write("\n")

    def block(self):
        return self.tab * self.level

    def start(self, file_name):
        os.system("touch {}.py".format(file_name))
        with open(file_name + ".py", "r") as file:
            is_route = False
            is_handler = False
            route = ""
            index = 0
            for line in file:
                # Find Handlers
                # if self.is_handler()

                # Find Codeblocks
                if self.is_route(line):
                    is_route = True
                if is_route:
                    route += line
                    guid = self.is_guid(line)
                    if guid:
                        is_route = False
                        self.routes[guid] = Codeblock(content=route, index=index)
                        self.file.append(route)
                        route = ""
                        index += 1
                else:
                    self.file.append(line)
                    index += 1
    # End basic write functionalities

    # Custom Syntax functionalities
    def write_route(self, route_obj):
        route_name = route_obj["path"]
        # TODO: Application generation so this inefficient approach isn't used anymore
        current_app = next(iter(self.applications.keys()))
        method = route_obj["method"]
        keys = set(route_obj.keys())
        handler = self.get_handler(route_obj)
        new_route = Codeblock(content="", index=None)

        guid = None
        if "ui.guid" in keys and route_obj["ui.guid"]:
            guid = route_obj["ui.guid"]
            if guid in self.routes:
                new_route = self.routes[guid]
        elif guid is None:
            guid = "UI.{}".format(uuid.uuid4())
            while guid in self.routes:
                guid = "UI.{}".format(uuid.uuid4())

        route = "\nvenom.ui(\n"
        route += "{}.{}('{}', {})".format(current_app, method, route_name, handler)

        # Adding Options
        for key in keys:
            if key in {"url", "headers", "query"} and route_obj[key]:
                route += ".{}({{\n".format(key) + self.parse_params(route_obj[key]) + "})"
            elif key == "body" and route_obj["body"]:
                # TODO: List functionalities with body
                route += ".{}({{\n".format(key) + self.parse_params(route_obj[key]["template"]) + "})"
        if not route_obj["url"] and not route_obj["headers"] and not route_obj["query"] and not route_obj["body"]:
            route += "\n"
        route += ", '{}')\n".format(guid)
        new_route = new_route._replace(content=route)
        self.changes.append(new_route)

    # TODO: Finish up handler creation
    def get_handler(self, route_obj):
        route_name = route_obj["path"]
        method = route_obj["method"]
        handler = []
        handler_index = None

        for item in self.handlers:
            if item[0] == route_name:
                handler = item[2]
                handler_index = self.handlers.index(item)
                break
        if handler != []:
            # TODO: Use old handler
            pass
        else:
            handler_name = "Handler{}".format(len(self.handlers))

            handler.append("class {}(venom.RequestHandler):\n".format(handler_name))
            self.indent()
            handler.append(self.block() + "def {}(self):\n".format(method.lower()))
            self.indent()
            handler.append(self.block() + "pass\n")
            self.dedent()
            self.dedent()

            self.handlers.append((route_name, handler_name, handler))
            return handler_name

    def write_applications(self, object):
        self.imports.append("import venom\n")
        apps = object["apps"]
        for app in apps:
            self.applications[app] = \
                "{} = venom.Application(version=1, debug=True, protocol=venom.Protocols.JSONProtocol)\n".format(app)

    def parse_params(self, params):
        self.indent()
        result = ""
        keys = list(params.keys())
        for i in range(len(keys)):
            item_name = keys[i]
            item = params[item_name]
            item_type = item["type"]
            item_attributes = ""
            if item["attributes"]:
                item_attributes = self.parse_attributes(item["attributes"])

            result += self.block() + "'{}': venom.Parameters.{}(".format(item_name, item_type)
            if item_type == "Dict":
                # TODO: Check for empty attributes
                result += "{{\n{}{}}}".format(self.parse_params(item["template"]), self.block())
                if item_attributes:
                    result += ", "
            result += "{})".format(item_attributes)
            if i < len(keys) - 1:
                result += ","
            result += "\n"
        self.dedent()
        return result

    def parse_attributes(self, attributes):
        result = ""
        for key, value in attributes.items():
            if value is None or (key == "required" and value):
                continue

            if result != "":
                result += ", "

            if key in {"pattern", "characters"}:
                value = "'{}'".format(value)

            result += "{}={}".format(key, value)
        return result

    def is_guid(self, line):
        match = re.match("(?:}\))?, '(UI\.[a-zA-Z0-9-]+)'\)", line)
        if not match:
            return None
        return match.groups()[0]

    def is_import(self, line):
        match = re.match("((?:from [a-zA-Z]+ )?(?:import [a-zA-Z]+))", line)
        if not match:
            return None
        return match.groups()[0]

    def is_route(self, line):
        return line.strip() == "venom.ui("

    def is_application(self, line):
        regex = (
            "([a-zA-Z]+ = venom\.Application\(version=[0-9]+, "
            "debug=(?:(?:True)|(?:False)), protocol=venom.Protocols.JSONProtocol\))"
            )
        match = \
            re.match(regex, line)
        if not match:
            return None
        return match.groups()[0]

    def is_handler(self, line):
        match = re.match("", line)
