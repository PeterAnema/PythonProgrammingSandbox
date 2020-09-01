year = int(input('Which year? '))

is_leapyear = year % 4 == 0
is_leapyear = is_leapyear and year % 100 != 0
is_leapyear = is_leapyear or year % 400 == 0

print('Is %d a leapyear? %s' % (year, is_leapyear))