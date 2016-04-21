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
test_app.GET('/users/:id', UserHandler).headers({
    'X-Authorization': venom.Parameters.Integer(min=8, required=False)
}).url({
    'agetype': venom.Parameters.String(choices=['adult', 'child'])
}).body({
    'filename': venom.Parameters.String(min=3, characters='abcdefghijklmnop', max=100),
    'file': venom.Parameters.Integer(min=0),
    'email': venom.Parameters.String(min=2, pattern='.*'),
    'nested': venom.Parameters.Dict({
        'foo': venom.Parameters.Float()
    })
}).query({
    'file': venom.Parameters.Integer(min=1),
    'email': venom.Parameters.String(min=5)
}), 'UI.1234')
