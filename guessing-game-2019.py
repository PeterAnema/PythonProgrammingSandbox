import random

secret_number = random.randint(1, 100)

print('Guess a number between 1 and 100')

number_of_guesses = 0
while True:

    guess = int(input('What is your guess? '))
    number_of_guesses += 1
    
    if guess < secret_number:
        print('higher ...')

    elif guess > secret_number:
        print('lower ...')

    else:
        print('Yes! The number was %d' % secret_number)
        print('You guessed it in %d guesses' % number_of_guesses)
        break
