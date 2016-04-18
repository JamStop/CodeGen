import venom

test_app = venom.Application(version=1, debug=True, protocol=venom.Protocols.JSONProtocol)


class Handler0(venom.RequestHandler):
    def get(self):
        pass


venom.ui(
test_app.GET('/users/:id', Handler0).headers({
    'X-Authorization': venom.Parameters.Integer(min=8, required=False)
}).url({
    'agetype': venom.Parameters.String(choices=['adult', 'child'])
}).query({
    'file': venom.Parameters.Integer(min=1),
    'email': venom.Parameters.String(min=5)
}).body({
    'filename': venom.Parameters.String(min=3, characters='abcdefghijklmnop', max=100),
    'file': venom.Parameters.Integer(min=0),
    'nested': venom.Parameters.Dict({
        'foo': venom.Parameters.Float()
    }, required=False),
    'email': venom.Parameters.String(min=2, pattern='.*')
}), 'UI.df4df8ed-9655-4199-b73e-e2226e8791c1')

venom.ui(
test_app.GET('/users/:id', None)
, 'UI.30f137b6-66e6-4649-b959-75ec03321f3e')
