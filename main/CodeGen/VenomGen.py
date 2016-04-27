'''
Venom Gen Base Class
c Jimmy Yue

This class accepts the metaobject from the Venom IDE,
and conducts the generation process.
'''

from CodeGen import VenomRouteGen
from sys import argv
import json


class VenomGen(object):
    def __init__(self):
        self.generated_route = None

    def generate(self, metaobject):
        meta = json.loads(metaobject)
        for key in meta:
            gen_object = meta[key]
            if not gen_object:
                continue

            if key == "routes":
                self._generate_route(gen_object)

        if self.generated_route:
            route_file, file_path = self.generated_route[0], self.generated_route[1]
            with open(file_path, "w") as file:
                for line in route_file:
                    file.write(line)

    def _generate_route(self, gen_object):
        route_gen = VenomRouteGen.VenomRouteGen()
        self.generated_route = route_gen.generate(gen_object)
