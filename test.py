import venom

test_app = venom.Application(version=1, debug=True, protocol=venom.Protocols.JSONProtocol)


class Handler0(venom.RequestHandler):
    def get(self):
        pass


test_app.GET('/users/:id', Handler0).body({
    'file': venom.Parameters.Integer(min=0),
    'nested': venom.Parameters.Dict({
        'foo': venom.Parameters.Float()
    }, required=False),
    'email': venom.Parameters.String(min=2, pattern='.*'),
    'filename': venom.Parameters.String(min=3, max=100, characters='abcdefghijklmnop')
}).headers({
    'X-Authorization': venom.Parameters.Integer(min=8, required=False)
}).query({
    'file': venom.Parameters.Integer(min=1),
    'email': venom.Parameters.String(min=5)
}).url({
    'agetype': venom.Parameters.String(choices=['adult', 'child'])
})