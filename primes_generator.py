
def find_next_prime(list_of_primes):
    number_to_test = max(list_of_primes) + 2
    while True:
        maximumFactor = int(number_to_test ** 0.5) + 1
        for factor in list_of_primes:
            if number_to_test % factor == 0: 
                break
            if factor > maximumFactor: 
                return number_to_test
        else:
            return number_to_test
        number_to_test += 2


def find_primes(n = None):
    list_of_primes = [2, 3]
    number_of_primes = len(list_of_primes)
    for prime in list_of_primes:
        yield prime

    while True:
        nextPrime = find_next_prime(list_of_primes)
        list_of_primes.append(nextPrime)
        number_of_primes += 1
        yield nextPrime

        if n and number_of_primes >= n:
            break

# -------------------------------------------------------

try:
    for p in find_primes(300000):
        print(p)

except KeyboardInterrupt:
    print('\nstopped!')
