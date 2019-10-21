class Processor:
    '''
    The brains of this application.

    doctests:

    >>> processor = Processor()
    >>> processor.getResult()
    '0'
    >>> processor.keyPressed('1')
    >>> processor.keyPressed('2')
    >>> processor.getResult()
    '12'
    >>> processor.keyPressed('+')
    >>> processor.getResult()
    '12'
    >>> processor.keyPressed('2')
    >>> processor.getResult()
    '2'
    >>> processor.keyPressed('=')
    >>> processor.getResult()
    '14'
    >>> processor.keyPressed('C')
    >>> processor.getResult()
    '0'

    '''

    DECIMALFORMAT = '%g'


    def __init__(self):
        self.reset()

    def reset(self):
        self._invoer = 0
        self._keyspressed = ''
        self._stored = 0
        self._result = self._stored
        self._operator = ""
        self._decimal_point_pressed = False

    def getResult(self):
        return Processor.DECIMALFORMAT % (self._result)

    def convertToNumber(self, keyspressed):
        if self._decimal_point_pressed:
            return float(self._keyspressed)
        else:
            return int(self._keyspressed)

    def keyPressed(self, key):

        if key in '1234567890':
            self._keyspressed += key
            self._invoer = self.convertToNumber(self._keyspressed)
            self._result = self._invoer

        elif key in '.':
            if not self._decimal_point_pressed:
                self._decimal_point_pressed = True
                if not self._keyspressed:
                    self._keyspressed = '0'
                self._keyspressed += key
                self._invoer = self.convertToNumber(self._keyspressed)
                self._result = self._invoer

        elif key in '+-*/=':
            self.calculate()
            self._operator = key
            self._keyspressed = ''
            self._decimal_point_pressed = False
            self._invoer = 0
            self._result = self._stored

        elif key in 'C':
            self.reset()


    def calculate(self):

        if self._operator == "+":
            self._stored += self._invoer;

        elif self._operator == "-":
            self._stored -= self._invoer;

        elif self._operator == "*":
            self._stored *= self._invoer;

        elif self._operator == "/":
            self._stored /= self._invoer;

        else:
            self._stored = self._result;


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
