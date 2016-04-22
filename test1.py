import venom


venom.ui(
test_app.POST('/api/v1/signup', UserHandler).body({
    'ag': venom.Parameters.Integer(required=False, min=0, max=200),
    'password': venom.Parameters.String(),
    'username': venom.Parameters.String()
}), 'ui-3456789')
