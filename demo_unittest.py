import unittest


class DemoUnitTests(unittest.TestCase):

    def test1(self):

        self.assertEqual(4, 2 + 2)

    def test2(self):

        self.assertEqual(40, 20 + 20)

    def test3(self):

        self.assertEqual(5, 3 + 2)



if __name__ == "__main__":
    unittest.main()
