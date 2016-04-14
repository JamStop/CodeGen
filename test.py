import venom

test_app = venom.Application(version=1, debug=True, protocol=venom.Protocols.JSONProtocol)

class Handler0(venom.RequestHandler):
    pass

test_app.GET('/users/:id', Handler0).query({
    'email': venom.Parameters.String(min=5),
    'file': venom.Parameters.Integer(min=1)
})
.headers({
    'X-Authorization': venom.Parameters.Integer(required=False, min=8)
})
.url({
    'agetype': venom.Parameters.String(choices=['adult', 'child'])
})
.body({
    'filename': venom.Parameters.String(max=100, min=3, characters=abcdefghijklmnop),
    'email': venom.Parameters.String(min=2, pattern='.*'),
    'file': venom.Parameters.Integer(min=0),
    'nested': venom.Parameters.Dict({
        'foo': venom.Parameters.Float()
    }, required=False)
})
