print('hello')

class WrongMove(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def quotient(x,y):
    if y <= 0:
        raise WrongMove('You know you should not divide by zero!')
    return x / y

try:
    print(quotient(10,0))

except WrongMove as err:
    print('WrongMove!! ', err)