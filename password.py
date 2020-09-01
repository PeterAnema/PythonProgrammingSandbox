import random
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

characters  = random.choices(uppercase, k = n_uppercase)
characters += random.choices(lowercase, k = n_lowercase)
characters += random.choices(number, k = n_number)
characters += random.choices(special, k = n_special)
characters += random.choices(uppercase + lowercase + number + special,
                             k = n_length - n_uppercase - n_lowercase - n_number - n_special)

random.shuffle(characters)

password = ''.join(characters)

print(password)
