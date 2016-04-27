'''
Route Generation With Meta
c Jimmy Yue

Code Generator Protocol
Provides Syntax Conventions for code generators
'''


class Generator(object):
    def __init__(self):
        self.level = 0
        self.tab = "    "

    def indent(self, degree=1):
        self.level = self.level + degree

    def dedent(self, degree=1):
        if self.level - degree < 0:
            raise SyntaxError("Cannot dedent below level 0")
        self.level = self.level - degree

    def block(self):
        return self.tab * self.level
