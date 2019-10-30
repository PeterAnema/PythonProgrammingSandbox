
def highest(*numbers):
    highest_number = numbers[0]
    for number in numbers[1:]:
        if number > highest_number:
            highest_number = number
    return highest_number

# ---------------------------------


print(highest(29, 3, 12, 56))











#
# def bepaal_grootste(*getallen):
#     grootste = 0
#     for getal in getallen:
#         if getal > grootste:
#             grootste = getal
#     return grootste
#
#
# print(bepaal_grootste(1,4,2,5,99,4,7,2,3,23))
