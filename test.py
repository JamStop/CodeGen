import venom


app = venom.Application(version=1, debug=True, protocol=venom.Protocols.JSONProtocol)


class Handler0(venom.RequestHandler):
    def get(self):
        import json
        pass

class Handler1(venom.RequestHandler):
    def get(self):
        pass



test other



venom.ui(
app1.GET('/users/:id', UserHandler).query({
    'email': venom.Parameters.String(min=5),
    'file': venom.Parameters.Integer(min=1)
}).body({
    'filename': venom.Parameters.String(min=3, characters='abcdefghijklmnop', max=100),
    'nested': venom.Parameters.Dict({
        'foo': venom.Parameters.Float()
    }),
    'email': venom.Parameters.String(min=2, pattern='.*'),
    'file': venom.Parameters.Integer(min=0)
}).url({
    'agetype': venom.Parameters.String(choices=['adult', 'child'])
}).headers({
    'X-Authorization': venom.Parameters.Integer(required=False, min=8)
}), 'ui-1234')

venom.ui(
app1.GET('/users/:id1', UserHandler)
, 'ui-2345')
