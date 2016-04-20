'''
Venom Gen Base Class
c Jimmy Yue

This class accepts the metaobject from the Venom IDE,
and conducts the generation process.
'''

import VenomRouteGen
from sys import argv
import json


class VenomGen(object):
    def __init__(self):
        self.route_files = []

    def generate(self, metaobject):
        meta = json.loads(metaobject)
        for key in meta:
            gen_object = meta[key]
            # if not gen_object:
            #     continue

            if key == "routes":
                self._generate_route(gen_object)

    def _generate_route(self, gen_object):
        route_gen = VenomRouteGen.VenomRouteGen()
        self.route_files = route_gen.generate(gen_object)
        print(self.route_files)

if __name__ == "__main__":
    test = VenomGen()
    test.generate('''{
    "routes": {
    }
    }''')
