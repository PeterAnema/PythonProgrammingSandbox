
def myfunction(**kwargs):

    for k, v in kwargs.items():
        print('%-10s : %s' % (k, v))

#==============================================================================

myfunction(a=2, b=5, c=6, x=99)

