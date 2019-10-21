class MyException(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message



def divide(a, b):
    try:
        if b > 100:
            raise MyException("Kan boven 100!")
        return a / b

    except MyException as err:
        print(err)



print(divide(10,200))