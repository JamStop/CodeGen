from CodeGen import VenomGen
from sys import argv

'''
Command line is "python3 VenomGeneration '{META}'"
Example metaobject:
{"routes":{"filePath":"test.py","UI.1234":{"path":"/users/:id","method":"GET","handler":"UserHandler","handlerFile":"VenomHandlers","headers":{"X-Authorization":{"type":"Integer","attributes":{"required":false,"pattern":null,"min":8}}},"url":{"agetype":{"type":"String","attributes":{"required":true,"pattern":null,"min":null,"choices":["adult","child"],"max":null,"characters":null}}},"query":{"file":{"type":"Integer","attributes":{"max":null,"choices":null,"required":true,"min":1}},"email":{"type":"String","attributes":{"max":null,"min":5}}},"body":{"type":"Dict","template":{"filename":{"type":"String","attributes":{"required":true,"pattern":null,"min":3,"choices":null,"max":100,"characters":"abcdefghijklmnop"}},"file":{"type":"Integer","attributes":{"min":0}},"nested":{"type":"Dict","template":{"foo":{"type":"Float","attributes":{"required":true}}},"attributes":{}},"email":{"type":"String","attributes":{"min":2,"required":true,"pattern":".*"}}}}},"UI.2345":{"path":"/users/:id1","method":"GET","handler":"UserHandler","handlerFile":"VenomHandlers","headers":{},"url":{},"query":{},"body":{}}}}
'''
if __name__ == "__main__":
    metaobject = argv[1]

    vgen = VenomGen.VenomGen()
    vgen.generate(metaobject)
