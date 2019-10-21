from timeit import timeit

def function1():
    s = "%s %d %g" % ("uitkomst", 10, 3.14)

def function2():
    s = "{} {} {}".format("uitkomst", 10, 3.14)

def function3():
    s = f"{'uitkomst'} {10} {3,14}"

def function4():
    s = str(10) + " " + str(3.14) + " uitkomst"

print( timeit(function1) )
print( timeit(function2) )
print( timeit(function3) )
print( timeit(function4) )
