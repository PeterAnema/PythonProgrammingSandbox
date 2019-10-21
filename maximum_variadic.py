
def maximum(*numbers):
    """Determine maximum value of a variadic list of arguments"""
    if numbers:
        max_value = numbers[0]
        for number in numbers[1:]:
            if number > max_value:
                max_value = number
        return max_value
    else:
        return None


def minimum(*numbers):
    """Determine minimum value of a variadic list of arguments"""
    if numbers:
        max_value = numbers[0]
        for number in numbers[1:]:
            if number < max_value:
                max_value = number
        return max_value
    else:
        return None


def min_max(*numbers):
    """Determine minimum and maximum value of a variadic list of arguments"""
    if numbers:
        min_value = numbers[0]
        max_value = numbers[0]
        for number in numbers[1:]:
            if number < min_value:
                min_value = number
            if number > max_value:
                max_value = number
        return min_value, max_value
    else:
        return None


# client code

if __name__ == '__main__':

    print(maximum(2,8,3,4))
    print(minimum(2,8,3,4))

    print(min_max(9,6,23,46,234,678,12,342))
