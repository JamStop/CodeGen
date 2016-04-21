'''
Route Generation With Meta
c Jimmy Yue

Generates route files given a collection of route objects
'''

from collections import namedtuple, defaultdict
import re
import os
from CodeGen import CodeGenerator


Route = namedtuple('Route', 'content, index')


class VenomRouteGen(CodeGenerator.Generator):
    def __init__(self):
        super(VenomRouteGen, self).__init__()
        self.imports = set()
        self.new_imports, self.import_index = [], None
        self.routes = defaultdict(Route)
        self.changed_routes = []
        self.guids = set()
        self.file = []

    def generate(self, route_objects):
        self.load_routes(route_objects["filePath"])
        for route_key in route_objects:
            if route_key == "filePath":
                continue
            route_data = route_objects[route_key]
            self.write_route(route_data, route_key)
        self.update_file()
        return (self.file, route_objects["filePath"])

    def update_file(self):
        # Make changes
        for route in self.changed_routes:
            index = route.index
            content = route.content
            if index:
                self.file[index] = content
            else:
                self.file.append(content)

        # Sanitize newlines
        state = None
        newline_count = 0
        new_file = []
        for line in self.file:
            if self.is_import(line):
                if state != 'IMPORT' and state is not None:
                    new_lines = 2 - newline_count
                    new_file.append("\n" * new_lines)
                new_file.append(line)
                newline_count = 0
                state = 'IMPORT'
                print("import")
            # TODO: Maybe throw an error if guids are improperly placed
            elif self.is_route(line):
                if state == 'ROUTE':
                    new_file.append("\n")
                elif state != 'ROUTE' and state is not None:
                    new_lines = 2 - newline_count
                    new_file.append("\n" * new_lines)
                new_file.append(line)
                newline_count = 0
                state = 'ROUTE'
                print("route")
            elif line != "\n":
                if state != 'OTHER' and state is not None:
                    new_lines = 2 - newline_count
                    new_file.append("\n" * new_lines)
                new_file.append(line)
                newline_count = 0
                state = 'OTHER'
                print("other")
            if state == 'OTHER' and line == "\n" and newline_count <= 2:
                new_file.append(line)
                newline_count += 1
        self.file = new_file


    def load_routes(self, file_path):
        os.system("touch {}".format(file_path))
        with open(file_path, "r") as file:
            is_route = False
            route = ""
            index = 0

            for line in file:
                # Find imports
                if self.is_import(line):
                    self.file.append(line)
                    self.imports.add(line)
                    self.import_index = index + 1
                    index += 1
                    continue

                # Find routes
                if self.is_route(line):
                    is_route = True
                if is_route:
                    route += line
                    guid = self.is_guid(line)
                    if guid:
                        is_route = False
                        self.routes[guid] = Route(content=route, index=index)
                        self.file.append(route)
                        route = ""
                        index += 1
                    continue

                self.file.append(line)
                index += 1

    def write_route(self, route_obj, guid):
        route_name = route_obj["path"]
        # TODO: Applications
        current_app = "test_app"
        method = route_obj["method"]
        keys = set(route_obj.keys())
        # TODO: Handler Handling
        handler = route_obj["handler"]
        self.import_handler(handler, route_obj["handlerFile"])
        new_route = Route(content="", index=None)

        if guid in self.routes:
            new_route = self.routes[guid]

        route = "venom.ui(\n"
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
        self.changed_routes.append(new_route)

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

    def import_handler(self, handler_name, handler_path):
        pass

    '''
    Regex helpers for route/import detection
    '''

    def is_guid(self, line):
        match = re.match("(?:}\))?, '(UI\.[a-zA-Z0-9-]+)'\)", line)
        if not match:
            return None
        return match.groups()[0]

    def is_import(self, line):
        match = re.match("((?:from [a-zA-Z]+ )?(?:import .+))", line)
        if not match:
            return None
        return match.groups()[0]

    def is_route(self, line):
        stripped_line = line.strip()
        return stripped_line[:9] == "venom.ui("