from string import Template

firstname = 'Albert'
lastname = 'Einstein'

print('The name is ' + firstname + ' ' + lastname + '.')

print('The name is %s %s.' % (firstname, lastname))

print('The name is {} {}.'.format(firstname, lastname))

print(f'The name is {firstname} {lastname}.')

print(Template('The name is $firstname $lastname.').substitute(firstname=firstname, lastname=lastname))
