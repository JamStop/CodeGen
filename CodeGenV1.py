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

    def save(self, file_name):
        with open(file_name + ".py", "w") as file:
            for line in self.header:
                file.write(line)
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
        return

    def write_header(self, header):
        self.header.append("import venom\n\n")
        apps = header["apps"]
        for app in apps:
            self.header.append(
                "{} = venom.Application(version=1, debug=True, protocol=venom.Protocols.JSONProtocol)\n".format(app)
            )
        self.header.append("\n")

    def parse_params(self, py_object):
        self.code.append(self.tab)

if __name__ == "__main__":
    test_header = {"apps": ["test_app"]}
    test_route = {"route_type": "GET", "route_name": "/serve/"}

    v = VenomGen()
    v.start("test")

    v.write_header(test_header)
    v.write_route(test_route)

    v.save("test")
    print(v.end())
