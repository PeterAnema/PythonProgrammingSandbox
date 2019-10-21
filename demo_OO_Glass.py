
class Glass:

    def __init__(self, volume = 100.0):
        self.__volume = volume
        self.__fluid = None
        self.__amount = 0
        self.__clean = True

    def fill(self, fluid, amount = None):

        if self.is_clean() or self.__fluid == fluid:
            self.__fluid = fluid
            self.__clean = False

            if amount:
                self.__amount = min(self.__volume, self.__amount + amount)
            else:
                self.__amount = self.__volume

        else:

            if not self.is_empty():
                print('Please empty your glass first')
                return

            if not self.is_clean():
                print('Please clean your glass first')
                return


    def drink(self, amount):
        self.__amount = max(0, self.__amount - amount)

    def clean(self):
        self.__amount = 0
        self.__clean = True

    def is_empty(self):
        return self.__amount == 0

    def is_clean(self):
        return self.__clean

    def info(self):
        if self.is_clean():
            return 'This glass is empty and clean'
        elif self.is_empty():
            return 'This glass is empty but it is not clean'
        else:
            return 'This glass is filled with %gcl of %s' % (self.__amount, self.__fluid)

#----------------------------------------------------

glass = Glass(160)
print(glass.info())

glass.fill('Water')
print(glass.info())

glass.drink(100)
print(glass.info())

glass.fill('Cola', 20)
print(glass.info())

glass.drink(100)
print(glass.info())

glass.fill('Cola', 20)
print(glass.info())

glass.clean()
print(glass.info())

glass.fill('Cola', 20)
print(glass.info())


