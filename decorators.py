def trace(func):
    "This decorator dumps out the arguments passed to a function before calling it"

    argnames = func.__code__.co_varnames[:func.__code__.co_argcount]
    fname = func.__qualname__

    def wrapper(*args, **kwargs):

        print(fname + "(",
              ', '.join('%s=%r' % entry for entry in list(zip(argnames,args[:len(argnames)])) +
                                                     [("args", list(args[len(argnames):]))] +
                                                     [("kwargs", kwargs)]),
              ")")

        return func(*args, **kwargs)

    return wrapper



@trace
def f(x,y):
    return x+y


print( f(3,4) )