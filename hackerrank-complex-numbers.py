class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)

    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)

    def __mul__(self, no):
        return Complex(self.real * no.real - self.imaginary * no.imaginary,
                       self.real * no.imaginary + self.imaginary * no.real)

    def __truediv__(self, no):
        Discriminant = no.real ** 2 + no.imaginary ** 2
        Nominator = self * no.conjugate()
        return Complex(Nominator.real / Discriminant, Nominator.imaginary / Discriminant)

    def conjugate(self):
        return Complex(self.real, -self.imaginary)

    def mod(self):
        return Complex((self.real ** 2 + self.imaginary ** 2) ** 0.5, 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

    def __repr__(self):
        return self.__str__()


c1 = Complex(2,1)
c2 = Complex(5,6)

print(c1+c2)
print(c1-c2)
print(c1*c2)
print(c1/c2)
print(c1.mod())
print(c2.mod())
