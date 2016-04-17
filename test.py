import venom

test_app = venom.Application(version=1, debug=True, protocol=venom.Protocols.JSONProtocol)


class Handler0(venom.RequestHandler):
    def get(self):
        pass


venom.ui(
test_app.GET('/users/:id', None)
, 'UI.30f137b6-66e6-4649-b959-75ec03321f3e')

venom.ui(
test_app.GET('/users/:id', Handler0).url({
    'agetype': venom.Parameters.String(choices=['adult', 'child'])
}).query({
    'file': venom.Parameters.Integer(min=1),
    'email': venom.Parameters.String(min=5)
}).headers({
    'X-Authorization': venom.Parameters.Integer(required=False, min=8)
}).body({
    'file': venom.Parameters.Integer(min=0),
    'email': venom.Parameters.String(pattern='.*', min=2),
    'filename': venom.Parameters.String(characters='abcdefghijklmnop', min=3, max=100),
    'nested': venom.Parameters.Dict({
        'foo': venom.Parameters.Float()
    }, required=False)
}), 'UI.2737393d-6504-4d4c-a90b-55dc4fa66819')
