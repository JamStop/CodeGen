'''
V1
c Jimmy Yue
credits to http://effbot.org/zone/python-code-generator.htm for inspiration
'''

import json
import re
import uuid
from collections import defaultdict

# TODO: Go over existing code -> Cleanup
# TODO: Pickle Pickle Pickle

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


class VenomGen:
    def __init__(self):
        self.level = 0
        self.apps = []
        self.header = []
        self.code = defaultdict(str)
        self.handlers = []
        self.tab = "    "
        self.file = []
        self.guids = set()

    # Basic write functionalities
    def end(self):
        return "".join(self.code)

    def write(self, string):
        self.code.append(self.block() + string + "\n")

    def indent(self):
        self.level = self.level + 1

    def dedent(self):
        if self.level == 0:
            raise SyntaxError("Cannot dedent below level 0")
        self.level = self.level - 1

    def generate(self, file_name):
        with open(file_name + ".py", "w") as file:
            # Header Generation
            for line in self.header:
                file.write(line)
            file.write("\n\n")

            # Handler Generation
            for handler in self.handlers:
                for line in handler[2]:
                    file.write(line)
                file.write("\n")
            file.write("\n")

            # Code Generation (Routes, Models, Etc.)
            for line in self.code.values():
                file.write(line)
                file.write("\n")

    def block(self):
        return self.tab * self.level

    def start(self, file_name):
        file = open(file_name + ".py", "r")
        is_route = False
        route = ""
        for line in file:
            self.file.append(line)

            # Find Handlers
            # TODO: Handlers

            # Find Routes
            if line.strip() == "venom.ui(":
                is_route = True
            if is_route:
                route += line
            guid = self.is_guid(line)
            if guid and is_route:
                is_route = False
                self.code[guid] = route
                route = ""

        file.close()
    # End basic write functionalities

    # Custom Syntax functionalities
    def write_route(self, route_obj):
        route_name = route_obj["path"]
        method = route_obj["method"]
        keys = set(route_obj.keys())
        handler = self.get_handler(route_obj)

        guid = None
        if "ui.guid" in keys and route_obj["ui.guid"] not in {None, ""}:
            guid = route_obj["ui.guid"]
        if guid is None:
            while guid not in self.code.keys():
                guid = "UI.{}".format(uuid.uuid4())
                self.code[guid] = ""

        route = "venom.ui(\n"
        route += "{}.{}('{}', {})".format(self.apps[0], method, route_name, handler)

        # Adding Options
        for key in keys:
            if key in {"url", "headers", "query"}:
                route += ".{}({{\n".format(key) + self.parse_params(route_obj[key]) + "})"
            elif key == "body":
                # TODO: List functionalities with body
                route += ".{}({{\n".format(key) + self.parse_params(route_obj[key]["template"]) + "})"
        # TODO: Better option for checking lack of other keys
        if len(keys) <= 3:
            route += "\n"
        route += ", '{}')\n".format(guid)
        self.code[guid] = route

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

    def write_header(self, header):
        self.header.append("import venom\n\n")
        apps = header["apps"]
        for app in apps:
            self.header.append(
                "{} = venom.Application(version=1, debug=True, protocol=venom.Protocols.JSONProtocol)\n".format(app)
            )
            self.apps.append(app)

    def parse_params(self, params):
        self.indent()
        result = ""
        keys = list(params.keys())
        for i in range(len(keys)):
            item_name = keys[i]
            item = params[item_name]
            item_type = item["type"]
            item_attributes = self.parse_attributes(item["attributes"])

            result += self.block() + "'{}': venom.Parameters.{}(".format(item_name, item_type)
            if item_type == "Dict":
                result += "{{\n{}{}}}, ".format(self.parse_params(item["template"]), self.block())
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
