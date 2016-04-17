import venom

test_app = venom.Application(version=1, debug=True, protocol=venom.Protocols.JSONProtocol)


class Handler0(venom.RequestHandler):
    def get(self):
        pass


venom.ui(
test_app.GET('/users/:id', Handler0).query({
    'file': venom.Parameters.Integer(min=1),
    'email': venom.Parameters.String(min=5)
}).body({
    'file': venom.Parameters.Integer(min=0),
    'nested': venom.Parameters.Dict({
        'foo': venom.Parameters.Float()
    }, required=False),
    'email': venom.Parameters.String(min=2, pattern='.*'),
    'filename': venom.Parameters.String(characters='abcdefghijklmnop', max=100, min=3)
}).url({
    'agetype': venom.Parameters.String(choices=['adult', 'child'])
}).headers({
    'X-Authorization': venom.Parameters.Integer(min=8, required=False)
}), 'UI.30f137b6-66e6-4649-b959-75ec03321f3e')

venom.ui(
test_app.GET('/users/:id', Handler0).query({
    'email': venom.Parameters.String(min=5),
    'file': venom.Parameters.Integer(min=1)
}).headers({
    'X-Authorization': venom.Parameters.Integer(min=8, required=False)
}).body({
    'email': venom.Parameters.String(pattern='.*', min=2),
    'filename': venom.Parameters.String(characters='abcdefghijklmnop', max=100, min=3),
    'file': venom.Parameters.Integer(min=0),
    'nested': venom.Parameters.Dict({
        'foo': venom.Parameters.Float()
    }, required=False)
}).url({
    'agetype': venom.Parameters.String(choices=['adult', 'child'])
}), 'UI.2feca3e1-2942-4f1c-8adf-f1482b9f990a')

venom.ui(
test_app.GET('/users/:id', Handler0).headers({
    'X-Authorization': venom.Parameters.Integer(required=False, min=8)
}).url({
    'agetype': venom.Parameters.String(choices=['adult', 'child'])
}).body({
    'filename': venom.Parameters.String(characters='abcdefghijklmnop', min=3, max=100),
    'file': venom.Parameters.Integer(min=0),
    'nested': venom.Parameters.Dict({
        'foo': venom.Parameters.Float()
    }, required=False),
    'email': venom.Parameters.String(pattern='.*', min=2)
}).query({
    'file': venom.Parameters.Integer(min=1),
    'email': venom.Parameters.String(min=5)
}), 'UI.77cb1752-30f2-41bf-92e1-f7886c90a281')

venom.ui(
test_app.GET('/users/:id', Handler0).url({
    'agetype': venom.Parameters.String(choices=['adult', 'child'])
}).query({
    'file': venom.Parameters.Integer(min=1),
    'email': venom.Parameters.String(min=5)
}).body({
    'file': venom.Parameters.Integer(min=0),
    'nested': venom.Parameters.Dict({
        'foo': venom.Parameters.Float()
    }, required=False),
    'email': venom.Parameters.String(min=2, pattern='.*'),
    'filename': venom.Parameters.String(max=100, min=3, characters='abcdefghijklmnop')
}).headers({
    'X-Authorization': venom.Parameters.Integer(required=False, min=8)
}), 'UI.99dc7e68-602f-41bd-95b9-2622dd2b36c1')

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

