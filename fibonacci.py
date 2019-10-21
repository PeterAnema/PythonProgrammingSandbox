
def fibonacci(n):
    fib = []
    n1 = 0
    fib.append(n1)
    n2 = 1
    fib.append(n2)
    for i in range(n-2):
        n1, n2 = n2, n1 + n2
        fib.append(n2)
    return fib


def fibonacci_generator(n):
    n1 = 0
    yield n1
    n2 = 1
    yield n2
    for i in range(n-2):
        n1, n2 = n2, n1 + n2
        yield n2


if __name__ == '__main__':
    n = 20
    print(*fibonacci(n))
    print(*fibonacci_generator(n))