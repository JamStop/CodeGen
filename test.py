import venom

test_app = venom.Application(version=1, debug=True, protocol=venom.Protocols.JSONProtocol)


class Handler0(venom.RequestHandler):
    def get(self):
        pass

class Handler1(venom.RequestHandler):
    def get(self):
        pass


venom.ui(
test_app.GET('/users/:id', Handler0).url({
    'agetype': venom.Parameters.String(choices=['adult', 'child'])
}).headers({
    'X-Authorization': venom.Parameters.Integer(min=8, required=False)
}).body({
    'file': venom.Parameters.Integer(min=0),
    'nested': venom.Parameters.Dict({
        'foo': venom.Parameters.Float()
    }, ),
    'filename': venom.Parameters.String(min=3, max=100, characters='abcdefghijklmnop'),
    'email': venom.Parameters.String(min=2, pattern='.*')
}).query({
    'file': venom.Parameters.Integer(min=1),
    'email': venom.Parameters.String(min=5)
}), 'UI.01bf2b09-ebd5-4aee-85e1-3e0aeb8a75fb')

venom.ui(
test_app.GET('/users/:id1', Handler1)
, 'UI.30f137b6-66e6-4649-b959-75ec03321f3e')

venom.ui(
test_app.GET('/users/:id', Handler0).body({
    'email': venom.Parameters.String(min=2, pattern='.*'),
    'nested': venom.Parameters.Dict({
        'foo': venom.Parameters.Float()
    }, ),
    'file': venom.Parameters.Integer(min=0),
    'filename': venom.Parameters.String(min=3, characters='abcdefghijklmnop', max=100)
}).headers({
    'X-Authorization': venom.Parameters.Integer(required=False, min=8)
}).url({
    'agetype': venom.Parameters.String(choices=['adult', 'child'])
}).query({
    'email': venom.Parameters.String(min=5),
    'file': venom.Parameters.Integer(min=1)
}), 'UI.f963a13a-39b2-4fb7-a2e9-fb363db9b225')

venom.ui(
test_app.GET('/users/:id', Handler0).url({
    'agetype': venom.Parameters.String(choices=['adult', 'child'])
}).body({
    'file': venom.Parameters.Integer(min=0),
    'filename': venom.Parameters.String(characters='abcdefghijklmnop', min=3, max=100),
    'nested': venom.Parameters.Dict({
        'foo': venom.Parameters.Float()
    }, ),
    'email': venom.Parameters.String(pattern='.*', min=2)
}).query({
    'file': venom.Parameters.Integer(min=1),
    'email': venom.Parameters.String(min=5)
}).headers({
    'X-Authorization': venom.Parameters.Integer(required=False, min=8)
}), 'UI.b78a5c3a-0009-4230-874f-0bf22a1d06a5')

