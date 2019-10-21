import unittest



class Counter:
    def __init__(self):
        self.__count = 0
    def count(self, n=0):
        self.__count += n
    def getCount(self):
        return self.__count




class CounterUnitTests(unittest.TestCase):

    def test_Counter(self):
        """Test routine for counter"""
        c = Counter()
        self.assertEqual(c.getCount(), 0, 'reset to 0')

        for n in range(10):
            c.count()
        self.assertEqual(c.getCount(), 10, 'increment 10 times')

        c.count(5)
        self.assertEqual(c.getCount(), 15, 'add 5')


if __name__ == "__main__":
    unittest.main()
    