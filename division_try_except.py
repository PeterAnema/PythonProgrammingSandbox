

class DelenDoorNulFout(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)



def divide(x, y):
    try:
        if y == 0:
            raise DelenDoorNulFout('Delen door nul')

        return x / y

    except DelenDoorNulFout:
        print('Delen door nul kan echt niet!!!')


print( divide(2, 2) )
print( divide(2, 1) )
print( divide(2, 0) )