'''
'{"routes":{"ui-3456789":{"body":{"attributes":{"required":true},
"guid":"4e36dd24-c8d9-f804-effb-16c893d689f7","key":"root","template":{"ag":{"attributes":{"max":200,"min":0,
"required":false},"guid":"c539e890-850f-afad-d378-0b3163fdf1f3","key":"ag","type":"Integer"},"password
":{"attributes":{"required":true},"guid":"30082b18-6af3-918e-85ae-c54fdb060185","key":"password","type":
"String"},"username":{"attributes":{"required":true},"guid":"6781e83b-c0db-0a37-7531-8595272a9d60","key":"u
sername","type":"String"}},"type":"Dict"},"handler":"UserHandler","handlerFile":"VenomHandlers","headers":{},"m
ethod":"POST","methods":["POST"],"path":"/api/v1/signup","query":{},"ui.guid":"ui-3456789","url":{}},"filePath":"jero
en.py"}}''
'''


import venom
from handlers import LoginHandler
from handlers import SignupHandler
from handlers import GroupsHandler
from handlers import ProfileHandler
from handlers import HelloWorldHandler
from models import User


version1 = venom.Application(version=1)


venom.ui(
version1.POST('/login', LoginHandler).body({
 'username': venom.Parameters.String(),
 'password': venom.Parameters.String()
}), 'ui-0234789')

venom.ui(
test_app.POST('/api/v1/signup', UserHandler).body({
    'username': venom.Parameters.String(),
    'ag': venom.Parameters.Integer(min=0, max=200, required=False),
    'password': venom.Parameters.String()
}), 'ui-3456789')


# right now this has an error where it created
# a new user instead of updating the old one


venom.ui(
version1.PUT('/profile/:user', ProfileHandler).url({
 'user': venom.Parameters.Model(User)
}).body({
 'username': venom.Parameters.String(required=False),
 'password': venom.Parameters.String(required=False),
 'age': venom.Parameters.Integer(required=False)
}), 'ui-56389134')


version1.GET('/groups/:tag', GroupsHandler).url({
 'tag': venom.Parameters.String(choices=[
   'children', 'adults', 'teenagers', 'seniors', 'discounted'
 ])
})


venom.ui(
version1.GET('/crazything/:foo/:bar', GroupsHandler).url({
 'foo': venom.Parameters.String(),
 'bar': venom.Parameters.Float(min=7)
}).headers({
 'X-Authorization': venom.Parameters.Model(User),
 'user-agent': venom.Parameters.String()
}).query({
 'count': venom.Parameters.Integer(),
 'buzzword': venom.Parameters.String()
}).body({
 'favorite_things': venom.Parameters.List({
   'name': venom.Parameters.String(),
   'age': venom.Parameters.Float(),
   'random_json': venom.Parameters.Dict({
     'my_str': venom.Parameters.String(),
     'my_int_list': venom.Parameters.List(
       venom.Parameters.Integer()
     )
   })
 }),
 'date': venom.Parameters.Integer(),
 'random_string': venom.Parameters.String()
}), 'ui-93486109347')


version2 = venom.Application(version=2)


version2.GET('/helloworld', HelloWorldHandler)
