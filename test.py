import venom
from google.appengine.ext import ndb

test_app = venom.Application(version=1, debug=True, protocol=venom.Protocols.JSONProtocol)
