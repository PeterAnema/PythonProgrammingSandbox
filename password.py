import demo_random
import string

uppercase = string.ascii_uppercase     # 'ABCDEFGHIJKLMNPQRSTUVWXYZ'    #
lowercase = 'abcdefghijklmnopqrstuvwxyz'
number = '0123456789'
special = '#@&!*%$'

n_length = 6
n_uppercase = 1
n_lowercase = 1
n_number = 1
n_special = 1

characters  = demo_random.choices(uppercase, k = n_uppercase)
characters += demo_random.choices(lowercase, k = n_lowercase)
characters += demo_random.choices(number, k = n_number)
characters += demo_random.choices(special, k = n_special)
characters += demo_random.choices(uppercase + lowercase + number + special,
                                  k = n_length - n_uppercase - n_lowercase - n_number - n_special)

demo_random.shuffle(characters)

password = ''.join(characters)

print(password)
