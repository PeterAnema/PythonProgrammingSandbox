def count_forever():
    i = 1
    while True:
        yield i
        i += 1

for number in count_forever():
    print(number)