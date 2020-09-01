from timeit import timeit

def function1():
    n = 10
    if n == 10:
        b = True
    else:
        b = False

def function2():
    n = 10
    b = True if n == 10 else False

def function3():
    n = 10
    b = n == 10

print( timeit(function1) )
print( timeit(function2) )
print( timeit(function3) )
