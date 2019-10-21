


def do_something(arg1, arg2, f):
    return f(arg1, arg2)


def add(x1, x2):
    return x1 + x2

def difference(x1, x2):
    return abs(x1 - x2)

def product(x1, x2):
    return x1 * x2



print(do_something(3, 6, add))
print(do_something(3, 6, difference))
print(do_something(3, 6, product))
    
