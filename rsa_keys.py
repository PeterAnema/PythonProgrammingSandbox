# Determine a pair of RSA keys for asymetric encryption
#
# Choose 2 primes: E.g. p = 3 and q = 11
# Compute n = p * q = 3 * 11 = 33.
# Compute φ(n) = (p - 1) * (q - 1) = 2 * 10 = 20. This is called the totient of n
# Choose e such that 1 < e < φ(n) and e and φ(n) are coprime. Let e = 7
# Compute a value for d such that (d * e) % φ(n) = 1. One solution is d = 3 [(3 * 7) % 20 = 1]
# Public key is (e, n) => (7, 33)
# Private key is (d, n) => (3, 33)
# The encryption of m = 2 is c = 2**7 % 33 = 29
# The decryption of c = 29 is m = 29**3 % 33 = 2

import demo_random
import itertools

#PRIMES = (7, 11, 13, 17, 19)   # without 1, 2, 3, 5
PRIMES = (7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
#PRIMES = (7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439) # , 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541)

def find_divisor_pairs(n):
    divisors = {(1, n)}
    for i in range(2, int(n ** 0.5) + 1):
        q = n // i
        if q * i == n:
            divisors.add((i,q))
    return divisors

def find_divisors(n):
    divisor_pairs = find_divisor_pairs(n)
    return {d1 for d1, d2 in divisor_pairs} | {d2 for d1, d2 in divisor_pairs}

def find_prime_divisors(n):
    prime_divisors = set()
    for d in find_divisors(n):
        if len(find_divisor_pairs(d)) == 1:
            prime_divisors.add(d)
    return prime_divisors

def is_coprime(n1, n2):
    d1 = find_prime_divisors(n1)
    d2 = find_prime_divisors(n2)
    return bool(d1 & d2 == {1})

def totient(p, q):
    return (p - 1) * (q - 1)

def find_es(totient):
    es = set()
    for e in range(1, totient + 1):
        if is_coprime(e, totient):
            es.add(e)
    return es

def choose_e(totient):
    es = find_es(totient)
    es.discard(1)
    return demo_random.choice(tuple(es))

def find_ds(e, totient):
    ds = set()
    for d in range(1, totient + 1):
        if (d * e) % totient == 1:
            ds.add(d)
    return ds

def choose_d(e, totient):
    ds = find_ds(e, totient)
    return demo_random.choice(tuple(ds))

def choose_e_and_d(totient):
    while True:
        e = choose_e(totient)
        d = choose_d(e, totient)
        if d != e:
            return e, d

def determine_rsa_keys(p, q, verbose = False):

    n = p * q
    t = totient(p, q)

    e, d = choose_e_and_d(t)

    public_key = (e, n)
    private_key = (d, n)

    if verbose:
        print('p                  : %d' % p)
        print('q                  : %d' % q)
        print()
        print('n                  : %d' % n)
        print('totient - phi(n)   : %d' % t)
        print('e                  : %d' % e)
        print('d                  : %d' % d)
        print()

    return public_key, private_key

def encrypt_number(number, key):
    e, totient = key
    return number ** e % totient

def decrypt_number(encrypted, key):
    d, totient = key
    return encrypted ** d % totient

def encrypt_text(text, key, encoding = 'utf-8'):
    encoded = text.encode(encoding)
    return [encrypt_number(c, key) for c in encoded]

def decrypt_text(numbers, key, encoding = 'utf-8'):
    return bytes([decrypt_number(n, key) for n in numbers]).decode(encoding)

def test():
    for p, q in itertools.product(PRIMES, PRIMES):
        if p == q:
            continue
        print(p, q, end = ' ==> ')
        public_key, private_key = determine_rsa_keys(p, q)
        print(public_key, private_key, end = ' testing ... ')
        for number in range(10):
            encrypted = encrypt_number(number, public_key)
            decrypted = decrypt_number(encrypted, private_key)
            if decrypted != number:
                print('Error: %d', number)
            assert decrypted == number
        print('All OK')


# ---------------------------------------------------------

if __name__  == '__main__':

    print('RSA asymetric encryption')
    print()

    p = demo_random.choice(PRIMES)          # A prime e.g. 3
    while True:
        q = demo_random.choice(PRIMES)      # Another prime e.g. 11
        if p != q:
            break

    public_key, private_key = determine_rsa_keys(p, q, verbose = True)    # with 2 primes

    print('public key         : %s' % str(public_key))
    print('private key        : %s' % str(private_key))
    print()

    # encrypting and decrypting a number
    number = demo_random.randint(10, 99)     # to encrypt
    print('random number %d' % number)

    print()

    encrypted = encrypt_number(number, public_key)
    print('encrypted with public key\n ==> %d' % (encrypted))

    decrypted = decrypt_number(encrypted, private_key)
    print('decrypted with private key\n ==> %d' % (decrypted))

    print()

    encrypted = encrypt_number(number, private_key)
    print('encrypted with private key\n ==> %d' % (encrypted))

    decrypted = decrypt_number(encrypted, public_key)
    print('decrypted with public key\n ==> %d' % (decrypted))

    print()

    # encrypting and decrypting text
    secret_text = 'dit is unicode met tekst patiënt'     # to encrypt
    print('text: %s' % secret_text)

    print()

    encrypted = encrypt_text(secret_text, public_key)
    print('encrypted with public key\n ==> %s' % encrypted)

    decrypted = decrypt_text(encrypted, private_key)
    print('decrypted with private key\n ==> %s' % decrypted)

    print()

    encrypted = encrypt_text(secret_text, private_key)
    print('encrypted with private key\n ==> %s' % encrypted)

    decrypted = decrypt_text(encrypted, public_key)
    print('decrypted with public key\n ==> %s' % decrypted)
