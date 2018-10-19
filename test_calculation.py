import unittest
from calculate import calculation

class test_calculation(unittest.TestCase):

    def test_add(self):
        result=calculation.addition(3,4)
        self.assertEqual(result,7)
        result=calculation.addition(-1,1)
        self.assertEqual(result,0)
        result=calculation.addition(-1,-2)
        self.assertEqual(result,-3)

    def test_sub(self):
        result=calculation.subtraction(-1,-1)
        self.assertEqual(result, 0)

    def test_div(self):
        result=calculation.division(-1,-1)
        self.assertEqual(result, 1)

    def test_mul(self):
        result = calculation.multiplication(-1, -1)
        self.assertEqual(result, 1)

    def test_exception(self):
        self.assertRaises(ValueError, calculation.division, 5,0)

if __name__=='__main__':
    unittest.main()
