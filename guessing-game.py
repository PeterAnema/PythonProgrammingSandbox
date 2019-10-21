import random

print("Guess a number between 1 and 99")

magic_number = random.randint(1, 99)

number_of_guesses = 0
while True:

    guess = int(input("What is your next guess? "))
    number_of_guesses += 1

    if guess > magic_number:
        print("lower ...")

    elif guess < magic_number:
        print("higher ...")

    elif guess == magic_number:
        print("YEAAAH! You guessed it in %d guesses" % number_of_guesses)
        break