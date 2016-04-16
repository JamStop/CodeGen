import venom

test_app = venom.Application(version=1, debug=True, protocol=venom.Protocols.JSONProtocol)


class Handler0(venom.RequestHandler):
    def get(self):
        pass


venom.ui(
test_app.GET('/users/:id', Handler0).headers({
    'X-Authorization': venom.Parameters.Integer(required=False, min=8)
}).url({
    'agetype': venom.Parameters.String(choices=['adult', 'child'])
}).query({
    'email': venom.Parameters.String(min=5),
    'file': venom.Parameters.Integer(min=1)
}).body({
    'nested': venom.Parameters.Dict({
        'foo': venom.Parameters.Float()
    }, required=False),
    'file': venom.Parameters.Integer(min=0),
    'email': venom.Parameters.String(min=2, pattern='.*'),
    'filename': venom.Parameters.String(min=3, max=100, characters='abcdefghijklmnop')
}), 'UI.f9cd61dc-ce53-4fcd-8143-ff202a0fdf74')
