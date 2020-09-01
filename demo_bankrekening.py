class Bankrekening:

    def __init__(self):
        self.saldo = 0

    def storten(self, bedrag):
        self.saldo += bedrag

    def opnemen(self, bedrag):
        self.saldo -= bedrag

    def vraag_saldo(self):
        return 'saldo is nu %d' % self.saldo

#=============================================

rekening = Bankrekening()

rekening.storten(1000)
rekening.opnemen(27)
rekening.opnemen(7)
rekening.opnemen(50)

print(rekening.vraag_saldo())
