
class BankAccount(object):

    def __init__(self, iban, name):
        self.__iban = iban
        self.__account_holder = name
        self.__balance = 0.0

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def info(self):
        print('Account %s of %s has a balance of €%.2f' % (self.__iban,
                                                           self.__account_holder,
                                                           self.__balance))


# --------------------------------------

acc1 = BankAccount('NL86INGB0564654689', 'Fahad')
acc1.deposit(200)
acc1.withdraw(50)

acc2 = BankAccount('NL45ABCA0354253678', 'Peter')
acc2.deposit(1000)
acc2.withdraw(100)

acc1.info()
acc2.info()