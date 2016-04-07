'''
V1
c Jimmy Yue
credits to http://effbot.org/zone/python-code-generator.htm for basic write functions
'''

import string


class VenomGen:
    def __init__(self):
        self.level = 0
        self.code = []
        self.tab = "\t"

    # Basic write functionalities
    def end(self):
        return string.join(self.code, "")

    def write(self, string):
        self.code.append(self.tab * self.level + string)

    def indent(self):
        self.level = self.level + 1

    def dedent(self):
        if self.level == 0:
            raise SyntaxError("")
        self.level = self.level - 1
    # End basic write functionalities

if __name__ == "__main__":
    v = VenomGen()
    v.write("for i in Range(5):")
    v.indent()
    v.write("print(i)")
    v.dedent

    print(v.end())
