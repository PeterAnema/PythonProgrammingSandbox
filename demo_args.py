
def f(*args):
    som = 0
    for number in args:
        som = som + number
    return som


print(f(1, 2, 3))
print(f(1, 2, 3, 4))
