
class MyClass:

    def methode1(*args):
        print('\nMethode 1 - standard method')
        print(args)

    @classmethod
    def methode2(*args):
        print('\nMethode 2 - @classmethod')
        print(args)

    @staticmethod
    def methode3(*args):
        print('\nMethode 3 - @staticmethod')
        print(args)


if __name__ == '__main__':

    MyClass.methode1()
    MyClass.methode2()
    MyClass.methode3()

    o = MyClass()

    o.methode1()
    o.methode2()
    o.methode3()
