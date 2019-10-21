from timeit import timeit

def function1():
    n = 5
    return 1 <= n < 10

def function2():
    n = 5
    return n >= 1 and n < 10

def function3():
    n = 5
    return n in range(1, 11)

print( timeit(function1) )
print( timeit(function2) )
print( timeit(function3) )
