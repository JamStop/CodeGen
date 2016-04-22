import venom


app = venom.Application(version=1, debug=True, protocol=venom.Protocols.JSONProtocol)


class Handler0(venom.RequestHandler):
    def get(self):
        import json
        pass

class Handler1(venom.RequestHandler):
    def get(self):
        pass


venom.ui(
test_app.GET('/users/:id', UserHandler).query({
    'email': venom.Parameters.String(min=5),
    'file': venom.Parameters.Integer(min=1)
}).body({
    'filename': venom.Parameters.String(min=3, max=100, characters='abcdefghijklmnop'),
    'email': venom.Parameters.String(min=2, pattern='.*'),
    'nested': venom.Parameters.Dict({
        'foo': venom.Parameters.Float()
    }),
    'file': venom.Parameters.Integer(min=0)
}).headers({
    'X-Authorization': venom.Parameters.Integer(min=8, required=False)
}).url({
    'agetype': venom.Parameters.String(choices=['adult', 'child'])
}), 'UI.1234')



test other



venom.ui(
app.GET('/users/:id', UserHandler).url({
    'agetype': venom.Parameters.String(choices=['adult', 'child'])
}).body({
    'filename': venom.Parameters.String(max=100, characters='abcdefghijklmnop', min=3),
    'file': venom.Parameters.Integer(min=0),
    'nested': venom.Parameters.Dict({
        'foo': venom.Parameters.Float()
    }),
    'email': venom.Parameters.String(min=2, pattern='.*')
}).query({
    'file': venom.Parameters.Integer(min=1),
    'email': venom.Parameters.String(min=5)
}).headers({
    'X-Authorization': venom.Parameters.Integer(required=False, min=8)
}), 'ui-1234')

venom.ui(
app.GET('/users/:id1', UserHandler)
, 'ui-2345')
