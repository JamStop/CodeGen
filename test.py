import venom

test_app = venom.Application(version=1, debug=True, protocol=venom.Protocols.JSONProtocol)

class Handler0(venom.RequestHandler):
    pass

app.GET(/users/:id, Handler0)