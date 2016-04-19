import venom


test_app = venom.Application(version=1, debug=True, protocol=venom.Protocols.JSONProtocol)


class Handler0(venom.RequestHandler):
    def get(self):
        pass

class Handler1(venom.RequestHandler):
    def get(self):
        pass


venom.ui(
test_app.GET('/users/:id', Handler0).body({
    'filename': venom.Parameters.String(characters='abcdefghijklmnop', min=3, max=100),
    'email': venom.Parameters.String(min=2, pattern='.*'),
    'nested': venom.Parameters.Dict({
        'foo': venom.Parameters.Float()
    }),
    'file': venom.Parameters.Integer(min=0)
}).headers({
    'X-Authorization': venom.Parameters.Integer(required=False, min=8)
}).query({
    'file': venom.Parameters.Integer(min=1),
    'email': venom.Parameters.String(min=5)
}).url({
    'agetype': venom.Parameters.String(choices=['adult', 'child'])
}), 'UI.d49f29a5-201f-4f53-b938-32bea1380973')

venom.ui(
test_app.GET('/users/:id1', Handler1)
, 'UI.30f137b6-66e6-4649-b959-75ec03321f3e')
