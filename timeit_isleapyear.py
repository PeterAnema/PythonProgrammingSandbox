from timeit import timeit

def function1(year):
    is_leap_year = ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)
    return is_leap_year

def function2(year):
    return ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)

def function3(year):
    is_leap_year = False
    if year % 4 == 0: is_leap_year = True
    if year % 100 == 0: is_leap_year = False
    if year % 400 == 0: is_leap_year = True
    return is_leap_year

def function4(year):
    is_leap_year = False
    if year % 4 == 0:
        is_leap_year = True
        if year % 100 == 0:
            is_leap_year = False
            if year % 400 == 0:
                is_leap_year = True
    return is_leap_year

def function5(year):
    is_leap_year = False
    if year % 4 == 0:
        is_leap_year = True
        if year % 100 == 0:
            is_leap_year = False
            if year % 400 == 0:
                is_leap_year = True
    return is_leap_year

def function6(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


print(timeit('function1(2004)', setup='from __main__ import function1'))
print(timeit('function2(2004)', setup='from __main__ import function2'))
print(timeit('function3(2004)', setup='from __main__ import function3'))
print(timeit('function4(2004)', setup='from __main__ import function4'))
print(timeit('function5(2004)', setup='from __main__ import function5'))
print(timeit('function6(2004)', setup='from __main__ import function6'))
