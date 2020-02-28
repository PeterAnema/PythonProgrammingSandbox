

def f1(n):
    numbers = []
    for i in range(n):
        numbers.append(i)
    return numbers

def f2(n):
    for i in range(n):
        yield i

def f3(n):
    yield from range(n)

# ----------------------------

print(f1(10))
print(f2(10))
print(f3(10))

for i in f1(10):
    print(i)

for i in f2(10):
    print(i)

for i in f3(10):
    print(i)

print(sum(f1(10)))
print(sum(f2(10)))
print(sum(f3(10)))


