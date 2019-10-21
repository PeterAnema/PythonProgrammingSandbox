

def numbers1(n):
    nums = []
    for i in range(n):
        nums.append(i)
    return nums

def numbers2(n):
    for i in range(n):
        yield i

print('A')
for n in numbers2(200000000):
    print(n)

print('B')
for n in numbers2(20000000):
    print(n)
print('C')
