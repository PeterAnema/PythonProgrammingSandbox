

names = []

# name = 'x'
# while name != '':
#     name = input("Who's next? : ")
#     if name != '':
#         names.append(name)

while True:
    name = input("Who's next? : ")
    if name == '':
        break
    names.append(name)

for name in sorted(names):
    print(name)