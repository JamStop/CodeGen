from CodeGen import VenomGen
from sys import argv

'''
Command line is "python3 VenomGeneration '{META}'"
'''
if __name__ == "__main__":
    metaobject = argv[1]

    vgen = VenomGen.VenomGen()
    vgen.generate(metaobject)
