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
test_app.GET('/users/:id', UserHandler).url({
    'agetype': venom.Parameters.String(choices=['adult', 'child'])
}).body({
    'email': venom.Parameters.String(min=2, pattern='.*'),
    'file': venom.Parameters.Integer(min=0),
    'nested': venom.Parameters.Dict({
        'foo': venom.Parameters.Float()
    }),
    'filename': venom.Parameters.String(characters='abcdefghijklmnop', min=3, max=100)
}).query({
    'email': venom.Parameters.String(min=5),
    'file': venom.Parameters.Integer(min=1)
}).headers({
    'X-Authorization': venom.Parameters.Integer(required=False, min=8)
}), 'UI.1234')
