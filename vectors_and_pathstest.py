import unittest
from vectors_and_paths import Vector

class VectorTest(unittest.TestCase):

    def test_can_create_vector(self):

        v = Vector(1,1)

        self.assertEqual(v.x, 1)
        self.assertEqual(v.y, 1)


    def test_can_str_vectors(self):

        v = Vector(2, 2)

        self.assertEqual('Vector(2,2)', str(v))


    def test_can_add_vectors(self):

        v1 = Vector(2, 2)
        v2 = Vector(-2, 2)

        v3 = v1 + v2

        self.assertEqual((v3.x, v3.y), (0, 4))

    def test_can_compare_vectors(self):

        v1 = Vector(2, 2)
        v2 = Vector(2, 2)
        v3 = Vector(-2, 2)

        self.assertTrue(v1 == v2)
        self.assertTrue(v1 != v3)
        self.assertFalse(v1 == v3)


if __name__ == '__main__':
    unittest.main()
