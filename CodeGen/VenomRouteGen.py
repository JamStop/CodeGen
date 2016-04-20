'''
Route Generation With Meta
c Jimmy Yue

Generates route files given a collection of route objects
'''

from collections import namedtuple, defaultdict
import re
import CodeGenerator


Route = namedtuple('Route', 'content, index')
File = namedtuple('File', 'path, lines')


class VenomRouteGen(CodeGenerator.Generator):
    def __init__(self):
        super(VenomRouteGen, self).__init__()
        self.imports = []
        self.routes = defaultdict(Route)
        self.guids = set()
        self.file = File(path="", lines="")
        self.changes = []

    def generate(self, route_objects):
        files = []
        return files
