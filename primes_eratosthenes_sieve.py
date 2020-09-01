# Eratosthenes sieve for determining primes
#
# A cute idea for `filtering out' prime numbers, invented by the Alexandrian mathematician Eratosthenes,
# works as follows. Suppose you want to find out all prime numbers below, say, 1000. You first cancel
# all multiples of 2 (except 2) from a list 1..1000. Now you will cancel all multiples of 3 (except 3).
# 4 has already been canceled, as it is a multiple of 2. Now you will take off all multiples of 5,
# except 5. And so on. Ultimately, what remains in the list would be prime numbers!

# It would be convenient to have a function which would return the first N values yielded by a generator.

def firstn(g, n):
	for i in range(n):
		yield next(g)

# Let's start with a generator which gives us all integers from `i' onwards:

def intsfrom(i):
	while True:
		yield i
		i = i + 1

# Now let's write a generator which will eliminate all multiples of a number `n' from a sequence:

def exclude_multiples(n, ints):
	for i in ints:
		if (i % n):
			yield i

# An invocation of the generator, say, list(firstn(exclude_multiples(2, intsfrom(1)), 5)),
# will give us the list [1,3,5,7,9].

# Now, its time for us to build our `sieve'.

def sieve(ints):
	while True:
		prime = next(ints)
		yield prime
		ints = exclude_multiples(prime, ints)


if __name__ == '__main__':
    for i in firstn(sieve(intsfrom(2)), 400):
        print(i)
