
print("List comprehension:")
mylist = [1,2,3,4,5,6]
print([item*2 for item in mylist])


print("Sorting")
mylist = ['aaaaa','c','bb','eeeeeeee']
print(sorted(mylist, key=lambda item: len(item)))


print("Map")
mylist = range(-5,6)
print(list(map(lambda item: item ** 2, mylist)))
print([item ** 2 for item in mylist])


print("Filter")
mylist = range(-5,6)
print(list(filter(lambda item: item % 2 != 0, mylist)))
print([x for x in mylist if x % 2 != 0])


print("Generator:")

for x in list([item**2 for item in range(1000000)]):
    print(x)

for x in (item**2 for item in range(1000000)):
    print(x)
