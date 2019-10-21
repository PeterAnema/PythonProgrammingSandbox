

def optional_add(number1, number2=None, number3=None):
    total = number1
    if number2 is not None:
        total += number2
    if number3 is not None:
        total += number3
    return total


print( optional_add(1) )
print( optional_add(1, 2) )
print( optional_add(1, 2, 3) )


print( optional_add('A', 'B') )



def variadic_add(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print( variadic_add(1) )
print( variadic_add(1, 2) )
print( variadic_add(1, 2, 3) )
