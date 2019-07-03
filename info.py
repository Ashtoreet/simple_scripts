user_info = {'first_name': '', 'last_name': ''}

user_info['first_name'] = input('Enter name: ')
user_info['last_name'] = input('Enter last_name: ')

print(user_info)
print('{} {}'.format(user_info['first_name'], user_info['last_name']))
