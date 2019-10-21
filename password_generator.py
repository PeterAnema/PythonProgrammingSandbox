import random

uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuvwxyz'
number = '0123456789'
special = '#@&!*%$'

def create_password(n_length = 8, n_uppercase = 1, n_lowercase = 1, n_number = 1, n_special = 1):
    characters  = random.choices(uppercase, k = n_uppercase)
    characters += random.choices(lowercase, k = n_lowercase)
    characters += random.choices(number, k = n_number)
    characters += random.choices(special, k = n_special)
    characters += random.choices(uppercase + lowercase + number + special,
                                 k = n_length - n_uppercase - n_lowercase - n_number - n_special)

    random.shuffle(characters)

    return ''.join(characters)

def count_characters_in_set_of_characters(s, set_of_characters):
    n = 0
    for c in s:
        if c in set_of_characters:
            n += 1
    return n

def check_password(password, n_length = 8, n_uppercase = 1, n_lowercase = 1, n_number = 1, n_special = 1):
    is_valid = len(password) >= n_length and \
               count_characters_in_set_of_characters(password, uppercase) >= n_uppercase and \
               count_characters_in_set_of_characters(password, lowercase) >= n_lowercase and \
               count_characters_in_set_of_characters(password, number) >= n_number and \
               count_characters_in_set_of_characters(password, special) >= n_special
    return is_valid

def check_password(password, n_length = 8, n_uppercase = 1, n_lowercase = 1, n_number = 1, n_special = 1):
    return len(password) >= n_length and \
           len(filter(lambda c: c in uppercase, password)) >= n_uppercase and \
           len(filter(lambda c: c in lowercase, password)) >= n_lowercase and \
           len(filter(lambda c: c in number, password)) >= n_number and \
           len(filter(lambda c: c in special, password)) >= n_special


# Maak een random wachtwoord met:
#   minimaal 8 karakters
#   tenminste 2 hoofdletters
#   tenminste 2 kleine letters
#   tenminste 2 cijfers
#   tenminste 1 speciale tekens

password = create_password(8, 2, 2, 2, 1)

print('Wachtwoord: %s' % password)

if check_password(password, 10, 2, 2, 2, 2):
    print("Dit is een geldige wachtwoord")
else:
    print("Dit wachtwoord is NIET OK!!!")
