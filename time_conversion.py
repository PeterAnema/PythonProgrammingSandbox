def timeConversion(s):
    #
    # Write your code here.
    #
    am_or_pm = s[-2:]
    h,m,s = map(int, s[:8].split(':'))
    if am_or_pm.lower() == 'pm':
        if h == 12:
            h = 0
        else:
            h += 12
    return '%02d:%02d:%02d' % (h,m,s)

def print_result(s):
    result = timeConversion(s)
    print('%s => %s' % (s, result))


for h in range(1,13):
    print_result('%02d:40:02AM' % h)
for h in range(1,13):
    print_result('%02d:40:02PM' % h)
