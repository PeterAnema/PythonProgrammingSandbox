import random
from timeit import timeit

def function1():
    c = number in l

def function2():
    c = number in t

def function3():
    c = number in s

if __name__ == '__main__':

    low = 0
    high = 999999
    n = 2000

    r = random.sample(range(low, high+1), n)
    s = set(r)
    l = list(r)
    t = tuple(r)

    number = random.randint(low, high)

    print( timeit(function1) )
    print( timeit(function2) )
    print( timeit(function3) )
