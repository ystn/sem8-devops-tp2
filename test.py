import unittest
import calcul

class TestCalculPackage(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calcul.add(2, 5), 7)

if __name__ == '__main__':
    unittest.main()