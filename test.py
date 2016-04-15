import venom

test_app = venom.Application(version=1, debug=True, protocol=venom.Protocols.JSONProtocol)


class Handler0(venom.RequestHandler):
    def get(self):
        pass


venom.ui(
test_app.GET('/users/:id', Handler0).headers({
    'X-Authorization': venom.Parameters.Integer(required=False, min=8)
}).query({
    'file': venom.Parameters.Integer(min=1),
    'email': venom.Parameters.String(min=5)
}).url({
    'agetype': venom.Parameters.String(choices=['adult', 'child'])
}).body({
    'filename': venom.Parameters.String(characters='abcdefghijklmnop', min=3, max=100),
    'file': venom.Parameters.Integer(min=0),
    'email': venom.Parameters.String(pattern='.*', min=2),
    'nested': venom.Parameters.Dict({
        'foo': venom.Parameters.Float()
    }, required=False)
}), 'UI.244bee07-7f01-4331-ab12-398e3ba4896a')
