
class BankAccount(object):

    def __init__(self, name):
        self.accountHolder = name
        self.__balance = 0.0

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def info(self):
        print('%s: %.2f' % (self.accountHolder, self.__balance))

#--------------------------------------

acc1 = BankAccount('Fahad')
acc1.deposit(200)
acc1.withdraw(50)

acc2 = BankAccount('Peter')
acc2.deposit(1000)
acc2.withdraw(100)

acc1.info()
acc2.info()