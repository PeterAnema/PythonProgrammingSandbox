import random

LOWER = 1
UPPER = 99

print(f'Guess a number between {LOWER} and {UPPER}')

magic_number = random.randint(LOWER, UPPER)

number_of_guesses = 0
while True:

    guess = int(input('What is your next guess? '))
    number_of_guesses += 1

    if guess > magic_number:
        print('lower ...')

    elif guess < magic_number:
        print('higher ...')

    elif guess == magic_number:
        print('YEAAAH! You guessed it in %d guesses' % number_of_guesses)
        break