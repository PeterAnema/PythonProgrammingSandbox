import demo_random
from collections import Counter
from operator import itemgetter
from timeit import timeit


def function1():
    d = {n: l.count(n) for n in set(l)}
    d = dict(sorted(d.items(), key=itemgetter(0)))
    return d

def function2():
    d = {}
    for n in l:
        d[n] = d.get(n, 0) + 1
    d = dict(sorted(d.items(), key=itemgetter(0)))
    return d

def function3():
    d = dict(Counter(l))
    d = dict(sorted(d.items(), key=itemgetter(0)))
    return d

if __name__ == '__main__':

    low = 0
    high = 1000
    n = 2000

    l = list(demo_random.choices(range(low, high + 1), k=n))

    print( function1() )
    print( function2() )
    print( function3() )

    print( timeit(function1, number=500) )
    print( timeit(function2, number=500) )
    print( timeit(function3, number=500) )
