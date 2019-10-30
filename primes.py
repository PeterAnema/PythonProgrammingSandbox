
def find_next_prime(list_of_primes):
    candidate_prime = max(list_of_primes) + 2
    while True:
        maximum_factor = int(candidate_prime ** 0.5) + 1
        for factor in list_of_primes:
            if candidate_prime % factor == 0: 
                break
            if factor > maximum_factor: 
                return candidate_prime
        else:
            return candidate_prime
        candidate_prime += 2


def find_primes(number_of_primes):
    list_of_primes = [2, 3]

    for i in range(len(list_of_primes), number_of_primes):

        nextPrime = find_next_prime(list_of_primes)
        list_of_primes.append(nextPrime)

    return list_of_primes
    
# -------------------------------------------------------

if __name__ == '__main__':
    for p in find_primes(30000):
        print(p)
