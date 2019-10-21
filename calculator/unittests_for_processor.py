import unittest

from processor import Processor

class CounterUnitTests(unittest.TestCase):

    def test_processor_init(self):
        p = Processor()
        self.assertEqual(p.getResult(), '0', 'initialize to 0')

    def test_processor_numeric(self):
        p = Processor()
        p.keyPressed('1')
        p.keyPressed('2')
        p.keyPressed('3')
        self.assertEqual(p.getResult(), '123', '123 pressed')

    def test_processor_add(self):
        p = Processor()
        p.keyPressed('1')
        p.keyPressed('+')
        p.keyPressed('3')
        p.keyPressed('=')
        self.assertEqual(p.getResult(), '4', '1+3 pressed')

    def test_processor_subtract(self):
        p = Processor()
        p.keyPressed('1')
        p.keyPressed('-')
        p.keyPressed('3')
        p.keyPressed('=')
        self.assertEqual(p.getResult(), '-2', '1-3 pressed')

    def test_processor_multiply(self):
        p = Processor()
        p.keyPressed('2')
        p.keyPressed('*')
        p.keyPressed('3')
        p.keyPressed('=')
        self.assertEqual(p.getResult(), '6', '2*3 pressed')

    def test_processor_divide(self):
        p = Processor()
        p.keyPressed('6')
        p.keyPressed('/')
        p.keyPressed('3')
        p.keyPressed('=')
        self.assertEqual(p.getResult(), '2', '6/3 pressed')


if __name__ == "__main__":
    unittest.main()
