import venom

test_app = venom.Application(version=1, debug=True, protocol=venom.Protocols.JSONProtocol)


class Handler0(venom.RequestHandler):
    def get(self):
        pass


venom.ui(
test_app.GET('/users/:id', None), 'UI.30f137b6-66e6-4649-b959-75ec03321f3e')

venom.ui(
test_app.GET('/users/:id', Handler0).url({
    'agetype': venom.Parameters.String(choices=['adult', 'child'])
}).headers({
    'X-Authorization': venom.Parameters.Integer(required=False, min=8)
}).body({
    'file': venom.Parameters.Integer(min=0),
    'filename': venom.Parameters.String(characters='abcdefghijklmnop', min=3, max=100),
    'nested': venom.Parameters.Dict({
        'foo': venom.Parameters.Float()
    }, required=False),
    'email': venom.Parameters.String(min=2, pattern='.*')
}).query({
    'file': venom.Parameters.Integer(min=1),
    'email': venom.Parameters.String(min=5)
}), 'UI.ae048dc2-4393-4600-bbbd-1b7d6df11674')
