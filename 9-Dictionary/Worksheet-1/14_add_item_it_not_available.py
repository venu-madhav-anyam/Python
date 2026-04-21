user = {'name': 'Riya'}

if not user.get('status'):
    user['status'] = 'active'

print(user)