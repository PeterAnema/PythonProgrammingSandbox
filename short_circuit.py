

def n(n):
    print("n")
    return n


def f1():
    print("f1")
    return 1


def f2():
    print("f2")
    return 10



print( f1() < n(5) < f2() )

print()

print( n(5) > f1() and n(5) < f2() )