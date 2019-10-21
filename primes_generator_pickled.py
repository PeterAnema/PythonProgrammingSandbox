import pickle
import os

class PrimesGeneratorPickled:
    __PICKLE_FILENAME = 'primes.pickle'

    def __init__(self, reset_pickle=False):
        self.__list_of_primes = []
        if reset_pickle: self.__reset_pickle()
        self.__load_from_pickle()
        pass

    def __enter__(self):
        return self

    def __exit__(self, exit_type, exit_value, exit_traceback):
        self.__save_to_pickle()
        print(self)

    def __repr__(self):
        return "PrimesGeneratorPickled()"

    def __str__(self):
        return "PrimesGeneratorPickled: %d primes found" % len(self.__list_of_primes)

    def __save_to_pickle(self, filename = __PICKLE_FILENAME):
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except:
            pass

    def __load_from_pickle(self, filename = __PICKLE_FILENAME):
        try:
            with open(filename, 'rb') as f:
                self.__dict__.update(pickle.load(f).__dict__)
        except:
            self.__reset_pickle()

    def __reset_pickle(self, filename = __PICKLE_FILENAME):
        try:
            os.remove(filename)
        except:
            pass
        self.__list_of_primes = []

    @staticmethod
    def __find_next_prime(list_of_primes):
        numberToTest = max(list_of_primes) + 2
        while True:
            maximumFactor = int(numberToTest ** 0.5) + 1
            for factor in list_of_primes:
                if numberToTest % factor == 0:
                    break
                if factor > maximumFactor:
                    return numberToTest
            else:
                return numberToTest
            numberToTest += 2

    def find_primes(self, n=None, start=0):
        number_of_known_primes = len(self.__list_of_primes)
        index = start if start >= 0 else number_of_known_primes + start + 1
        index = min(index, number_of_known_primes)

        # print(self.__list_of_primes)

        while True:
            if n and index > n - 1:
                break

            if index < number_of_known_primes:
                nextPrime = self.__list_of_primes[index]

            else:
                if number_of_known_primes < 2:
                    nextPrime = (2, 3)[number_of_known_primes]
                else:
                    nextPrime = PrimesGeneratorPickled.__find_next_prime(self.__list_of_primes)

                self.__list_of_primes.append(nextPrime)
                number_of_known_primes += 1

            if index >= start:
                yield nextPrime

            index += 1


# -------------------------------------------------------

verbose = True

try:
    with PrimesGeneratorPickled() as pg:
        for p in pg.find_primes(start=-1):
            if verbose:
                print(p)

except KeyboardInterrupt:
    print('stopped')
