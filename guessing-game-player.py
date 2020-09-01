low = 1
high = 100

number_of_guesses = 0
while True:
    guess = (low + high) // 2

    response = input('Is your number %d? [higher,lower,yes] : ' % guess).lower()
    number_of_guesses += 1

    if response.startswith('h'):    # e.g. higher
        low = guess + 1

    elif response.startswith('l'):  # e.g. lower
        high = guess - 1

    elif response.startswith('y'):  # e.g. yes
        print("YEAH! Guessed it in %d guesses" % number_of_guesses)
        break

    else:
        print('Invalid answer!')
        number_of_guesses -= 1

    if low > high:
        print("You cheated! I quit.")
        break
