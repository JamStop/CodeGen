import venom


test_app = venom.Application(version=1, debug=True, protocol=venom.Protocols.JSONProtocol)


class Handler0(venom.RequestHandler):
    def get(self):
        pass

class Handler1(venom.RequestHandler):
    def get(self):
        pass
venom.ui(
test_app.GET('/users/:id1', UserHandler)
, 'UI.2345')
venom.ui(
test_app.GET('/users/:id', UserHandler).query({
    'email': venom.Parameters.String(min=5),
    'file': venom.Parameters.Integer(min=1)
}).body({
    'filename': venom.Parameters.String(min=3, max=100, characters='abcdefghijklmnop'),
    'nested': venom.Parameters.Dict({
        'foo': venom.Parameters.Float()
    }),
    'email': venom.Parameters.String(pattern='.*', min=2),
    'file': venom.Parameters.Integer(min=0)
}).headers({
    'X-Authorization': venom.Parameters.Integer(min=8, required=False)
}).url({
    'agetype': venom.Parameters.String(choices=['adult', 'child'])
}), 'UI.1234')
