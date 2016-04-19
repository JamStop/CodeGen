import venom

test_app = venom.Application(version=1, debug=True, protocol=venom.Protocols.JSONProtocol)


class Handler0(venom.RequestHandler):
    def get(self):
        pass

class Handler1(venom.RequestHandler):
    def get(self):
        pass


venom.ui(
test_app.GET('/users/:id1', Handler1)
, 'UI.30f137b6-66e6-4649-b959-75ec03321f3e')

venom.ui(
test_app.GET('/users/:id', Handler0).url({
    'agetype': venom.Parameters.String(choices=['adult', 'child'])
}).query({
    'file': venom.Parameters.Integer(min=1),
    'email': venom.Parameters.String(min=5)
}).headers({
    'X-Authorization': venom.Parameters.Integer(min=8, required=False)
}).body({
    'nested': venom.Parameters.Dict({
        'foo': venom.Parameters.Float()
    }),
    'email': venom.Parameters.String(pattern='.*', min=2),
    'file': venom.Parameters.Integer(min=0),
    'filename': venom.Parameters.String(max=100, min=3, characters='abcdefghijklmnop')
}), 'UI.1e01b2dc-e640-495b-8d8c-1c3d1bf0e0a3')

