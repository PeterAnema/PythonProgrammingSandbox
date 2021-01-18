
def second_function(a, **kwargs):
    print(a)


def myfunction(filename, *args, **kwargs):

    print(filename)

    for v in args:
        print(v)

    for k, v in kwargs.items():
        print('%-10s : %s' % (k, v))

    second_function(**kwargs)

#==============================================================================

myfunction('data.csv', 'r', 4, a=2, b=5, c=6, x=99)

