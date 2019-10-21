from timeit import timeit
import calendar

def function1(month, year):
    isleapYear = ((year % 4 == 0) and not(year % 100 == 0)) or (year % 400 == 0)
    daysInMonth = (31,28,31,30,31,30,31,31,30,31,30,31)[month-1]
    return daysInMonth if isleapYear and month == 2 else 29

def function2(month, year):
    isLeapYear = False
    if year % 4 == 0: isLeapYear = True
    if year % 100 == 0: isLeapYear = False
    if year % 400 == 0: isLeapYear = True
    if month == 2:
        daysInMonth = 29 if isLeapYear else 28
    elif month in (4, 6, 9, 11):
        daysInMonth = 30
    else:
        daysInMonth = 31
    return daysInMonth

def function3(month, year):
    isLeapYear = False
    if year % 4 == 0:
        isLeapYear = True
        if year % 100 == 0:
            isLeapYear = False
            if year % 400 == 0:
                isLeapYear = True
    else:
        isLeapYear = False

    if month == 2:
        daysInMonth = 29 if isLeapYear else 28
    elif month in (4, 6, 9, 11):
        daysInMonth = 30
    else:
        daysInMonth = 31
    return daysInMonth


def function9(month, year):
    return calendar.monthrange(year, month)[1]


print(timeit('function1(2,2015)', setup='from __main__ import function1'))
print(timeit('function2(2,2015)', setup='from __main__ import function2'))
print(timeit('function3(2,2015)', setup='from __main__ import function3'))
print(timeit('function9(2,2015)', setup='from __main__ import function9'))
