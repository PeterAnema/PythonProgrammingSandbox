class WrittenNumber():

    EXCEPTIONS = {0:'nul', 11:'elf', 12:'twaalf', 13:'dertien'}
    ONES = ('', 'een', 'twee', 'drie', 'vier', 'vijf', 'zes', 'zeven', 'acht', 'negen')
    TENS = ('','tien','twintig','dertig','viertig','vijftig','zestig','zeventig','tachtig','negentig')
    HONDERD = 'honderd'
    DUIZEND = 'duizend'

    def __init__(self, value):
        self.__value = value
        
    def __str__(self):
        return str(self.write(self.__value))

    @staticmethod
    def write(number):
        if number in WrittenNumber.EXCEPTIONS.keys():
            return WrittenNumber.EXCEPTIONS[number]
        else:
            digits = map(int, list(('000' + str(abs(number)))[-4:]))

            digit4, digit3, digit2, digit1 = digits
            # rest, digit1 = divmod(number, 10)
            # rest, digit2 = divmod(rest, 10)
            # rest, digit3 = divmod(rest, 10)
            # rest, digit4 = divmod(rest, 10)

            written = ''

            if digit4 > 0:
                written += WrittenNumber.DUIZEND if digit4 == 1 else WrittenNumber.ONES[digit4] + WrittenNumber.DUIZEND

            if digit3 > 0:
                written += WrittenNumber.HONDERD if digit3 == 1 else WrittenNumber.ONES[digit3] + WrittenNumber.HONDERD

            if digit2 * 10 + digit1 in WrittenNumber.EXCEPTIONS.keys():
                if digit1:
                    return written + WrittenNumber.ONES[digit1]
                else:
                    return written
            elif digit2 == 0:
                if digit1:
                    return written + WrittenNumber.ONES[digit1]
                else:
                    return written
            elif digit2 == 1:
                if digit1:
                    return written + WrittenNumber.ONES[digit1] + WrittenNumber.TENS[digit2]
                else:
                    return written + WrittenNumber.TENS[digit2]
            else:
                if digit1:
                    s = written + WrittenNumber.ONES[digit1]
                    if s[-1] == 'e':
                        return s + 'ën'+ WrittenNumber.TENS[digit2]
                    else:
                        return s + 'en'+ WrittenNumber.TENS[digit2]
                else:
                    return written + WrittenNumber.TENS[digit2]


if __name__ == '__main__':

    for number in range(1, 1001):
        print(WrittenNumber(number))
