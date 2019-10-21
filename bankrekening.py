class BankAccount():
    """ Dit is mijn BankAccount klasse """

    # magic methods
    def __init__(self, account_holder, iban):
        self.saldo = 0
        self.account_holder = account_holder
        self.iban = iban
        # self.id = BankAccount.__nextId
        # BankAccount.__nextId += 1

    def __del__(self):
        print('Rekening van %s opgeheven' % self.account_holder)

    def __str__(self):
        return 'Rekening van %s heeft een saldo van %d' % (self.account_holder, self.saldo)

    def __repr__(self):
        return '%s: %d' % (self.account_holder, self.saldo)

    # getters
    def getSaldo(self):
        return self.saldo

    # setters
    def setSaldo(self, amount):
        self.saldo = amount

    # other methods
    def deposit(self, amount):
        self.saldo += amount
        print('%d gestort op de rekening van %s. Saldo is nu %d' % (amount, self.account_holder, self.saldo))

    def withdraw(self, amount):
        self.saldo -= amount
        print('%d opgenomen van de rekening van %s. Saldo is nu %d' % (amount, self.account_holder, self.saldo))


class SavingsAccount(BankAccount):

    def __init__(self, account_holder, iban):
        super().__init__(account_holder, iban)

    def geefRente(self, rente=0.1):
        self.saldo *= 1 + rente


# -----------------------------------------------

acc1 = BankAccount('Jessie', 'NL00INGB002837346')

acc1.deposit(100)
acc1.withdraw(50)


acc2 = SavingsAccount('Sepideh', 'NL00INGB04857634')

acc2.deposit(1000)
acc2.withdraw(50)


acc2.flag = True
setattr(acc2, 'flag', True)

acc2.geefRente(0.1)


print(acc1)
print(acc2)

print(repr(acc1))
print(repr(acc2))

print(BankAccount.__doc__)