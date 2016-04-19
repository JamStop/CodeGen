import venom

test_app = venom.Application(version=1, debug=True, protocol=venom.Protocols.JSONProtocol)


class Handler0(venom.RequestHandler):
    def get(self):
        pass

class Handler1(venom.RequestHandler):
    def get(self):
        pass


venom.ui(
test_app.GET('/users/:id1', Handler1)
, 'UI.30f137b6-66e6-4649-b959-75ec03321f3e')

venom.ui(
test_app.GET('/users/:id', Handler0).url({
    'agetype': venom.Parameters.String(choices=['adult', 'child'])
}).query({
    'file': venom.Parameters.Integer(min=1),
    'email': venom.Parameters.String(min=5)
}).body({
    'file': venom.Parameters.Integer(min=0),
    'email': venom.Parameters.String(pattern='.*', min=2),
    'nested': venom.Parameters.Dict({
        'foo': venom.Parameters.Float()
    }, ),
    'filename': venom.Parameters.String(max=100, characters='abcdefghijklmnop', min=3)
}).headers({
    'X-Authorization': venom.Parameters.Integer(required=False, min=8)
}), 'UI.66a33fc3-1da6-4fe7-8162-907f45b13f82')

