from timeit import timeit

def function1():
    squares = []
    for n in range(100):
        squares.append(n**2)

def function2():
    squares = [n**2 for n in range(100)]


print( timeit(function1) )
print( timeit(function2) )
