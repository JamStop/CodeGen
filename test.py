import venom


test_app = venom.Application(version=1, debug=True, protocol=venom.Protocols.JSONProtocol)


class Handler0(venom.RequestHandler):
    def get(self):
        pass

class Handler1(venom.RequestHandler):
    def get(self):
        pass


venom.ui(
test_app.GET('/users/:id', Handler0).query({
    'email': venom.Parameters.String(min=5),
    'file': venom.Parameters.Integer(min=1)
}).url({
    'agetype': venom.Parameters.String(choices=['adult', 'child'])
}).body({
    'nested': venom.Parameters.Dict({
        'foo': venom.Parameters.Float()
    }),
    'filename': venom.Parameters.String(characters='abcdefghijklmnop', max=100, min=3),
    'email': venom.Parameters.String(min=2, pattern='.*'),
    'file': venom.Parameters.Integer(min=0)
}).headers({
    'X-Authorization': venom.Parameters.Integer(required=False, min=8)
}), 'UI.227efe57-4c0e-4eb4-b82f-76451e10be13')

venom.ui(
test_app.GET('/users/:id1', Handler1)
, 'UI.30f137b6-66e6-4649-b959-75ec03321f3e')

venom.ui(
test_app.GET('/users/:id', Handler0).url({
    'agetype': venom.Parameters.String(choices=['adult', 'child'])
}).body({
    'nested': venom.Parameters.Dict({
        'foo': venom.Parameters.Float()
    }),
    'filename': venom.Parameters.String(characters='abcdefghijklmnop', max=100, min=3),
    'email': venom.Parameters.String(pattern='.*', min=2),
    'file': venom.Parameters.Integer(min=0)
}).query({
    'email': venom.Parameters.String(min=5),
    'file': venom.Parameters.Integer(min=1)
}).headers({
    'X-Authorization': venom.Parameters.Integer(required=False, min=8)
}), 'UI.6f1b6e7c-06a7-4716-a756-92e18c098e9c')
