'''
V1
c Jimmy Yue
credits to http://effbot.org/zone/python-code-generator.htm for inspiration
'''


class VenomGen:
    def __init__(self):
        self.level = 0
        self.header = []
        self.code = []
        self.handlers = []
        self.tab = "    "
        self.file = None

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
            file.write("\n")

            # Handler Generation
            for handler in self.handlers:
                for line in handler[2]:
                    file.write(line)
                file.write("\n")
            file.write("\n")

            # Code Generation (Routes, Models, Etc.)
            for line in self.code:
                file.write(line)

    def block(self):
        return self.tab * self.level

    def start(self, file_name):
        file = open(file_name + ".py", "r")
        self.file = file.readlines()
        file.close()
    # End basic write functionalities

    # Custom Syntax functionalities
    def write_route(self, route_obj):
        route_name = route_obj["path"]
        method = route_obj["method"]
        keys = route_obj.keys()
        handler = self.get_handler(route_obj)

        route = "app.{}({}, {})".format(method, route_name, handler)

        self.code.append(route)

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
            pass
        else:
            handler_name = "Handler{}".format(len(self.handlers))

            handler.append("class {}(venom.RequestHandler):\n".format(handler_name))
            self.indent()
            handler.append(self.block() + "pass")
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

    def parse_params(self, py_object):
        self.code.append(self.tab)

if __name__ == "__main__":
    test_header = {"apps": ["test_app"]}
    test_route = {
        "path": "/users/:id",
        "method": "GET",
        "headers": [
            {
                "name": "X-Authorization",
                "type": "integer"
            }
        ],
        "urlParameters": [
            {
                "name": "id",
                "type": "integer",
                "required": True
            }
        ],
        "queryParameters": [
            {
                "name": "expand",
                "type": "array",
                "items": {
                    "type": "string"
                }
            }
        ]
    }

    v = VenomGen()
    v.start("test")

    v.write_header(test_header)
    v.write_route(test_route)

    v.generate("test")
    print(v.end())
