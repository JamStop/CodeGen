from CodeGen import VenomGen
from sys import argv

'''
Command line is "python3 VenomGeneration '{META}'"
Example metaobject:
{"routes":{"filePath":"test.py","UI.1234":{"path":"/users/:id","method":"GET","handler":"UserHandler","handlerFile":"VenomHandlers","headers":{"X-Authorization":{"type":"Integer","attributes":{"required":false,"pattern":null,"min":8}}},"url":{"agetype":{"type":"String","attributes":{"required":true,"pattern":null,"min":null,"choices":["adult","child"],"max":null,"characters":null}}},"query":{"file":{"type":"Integer","attributes":{"max":null,"choices":null,"required":true,"min":1}},"email":{"type":"String","attributes":{"max":null,"min":5}}},"body":{"type":"Dict","template":{"filename":{"type":"String","attributes":{"required":true,"pattern":null,"min":3,"choices":null,"max":100,"characters":"abcdefghijklmnop"}},"file":{"type":"Integer","attributes":{"min":0}},"nested":{"type":"Dict","template":{"foo":{"type":"Float","attributes":{"required":true}}},"attributes":{}},"email":{"type":"String","attributes":{"min":2,"required":true,"pattern":".*"}}}}},"UI.2345":{"path":"/users/:id1","method":"GET","handler":"UserHandler","handlerFile":"VenomHandlers","headers":{},"url":{},"query":{},"body":{}}}}
'{"ui-56389134":{"body":{"attributes":{"required":true},"guid":"1664f39f-7077-441e-f758-c22aa19c43a7","key":"root","template":{"age_new":{"attributes":{"required":false},"guid":"5b3bd9b3-8aff-22ba-c554-a158dd42889d","key":"age_new","type":"Integer"},"password":{"attributes":{"required":false},"guid":"20112b9d-4fef-4ed9-229b-0cb3efb1de8e","key":"password","type":"String"},"username":{"attributes":{"required":false},"guid":"6979ed60-4177-f22e-60ff-8734300cc975","key":"username","type":"String"}},"type":"Dict"},"headers":{},"methods"frown emoticon"PUT"],"path":"/api/v1/profile/:user","query":{},"ui.guid":"ui-56389134","url":{"user":{"attributes":{"required":true},"guid":"5e1b243f-129f-d080-c576-f4e328d5720b","key":"user","modelname":"User","type":"Model"}}},"filePath":"/Users/jeroen/Developer/pyvenom/pyvenom/framework/routes.py"}'
'''
if __name__ == "__main__":
    metaobject = argv[1]

    vgen = VenomGen.VenomGen()
    vgen.generate(metaobject)
