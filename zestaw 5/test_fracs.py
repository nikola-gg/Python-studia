import unittest
from fracs import (
    add_frac, sub_frac, mul_frac, div_frac,
    is_positive, is_zero, cmp_frac, frac2float
)

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac_basic(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([-1, 2], [1, 2]), [0, 1])
        self.assertEqual(add_frac([1, -2], [1, 2]), [0, 1])

    def test_sub_frac_basic(self):
        self.assertEqual(sub_frac([3, 4], [1, 4]), [1, 2])
        self.assertEqual(sub_frac([1, 2], [3, 2]), [-1, 1])
        self.assertEqual(sub_frac([1, -2], [1, 2]), [-1, 1])

    def test_mul_frac_basic(self):
        self.assertEqual(mul_frac([2, 3], [3, 4]), [1, 2])
        self.assertEqual(mul_frac([-1, 2], [2, 3]), [-1, 3])
        self.assertEqual(mul_frac([0, 5], [7, 9]), [0, 1])

    def test_div_frac_basic(self):
        self.assertEqual(div_frac([2, 3], [4, 5]), [5, 6])
        self.assertEqual(div_frac([-1, 2], [1, 3]), [-3, 2])

    def test_div_frac_by_zero_raises(self):
        with self.assertRaises(ZeroDivisionError):
            div_frac([1, 2], [0, 7])

    def test_is_positive(self):
        self.assertTrue(is_positive([1, 3]))
        self.assertFalse(is_positive([-1, 3]))
        self.assertFalse(is_positive([0, 5]))
        self.assertFalse(is_positive([1, -3]))

    def test_is_zero(self):
        self.assertTrue(is_zero([0, 1]))
        self.assertTrue(is_zero([0, 5]))
        self.assertFalse(is_zero([1, 5]))


    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [2, 4]), 0)
        self.assertEqual(cmp_frac([1, 3], [1, 2]), -1)
        self.assertEqual(cmp_frac([3, 2], [1, 2]), 1)
        self.assertEqual(cmp_frac([1, -2], [1, 2]), -1)

    def test_frac2float(self):
        self.assertAlmostEqual(frac2float([1, 2]), 0.5)
        self.assertAlmostEqual(frac2float([-1, 4]), -0.25)
        self.assertAlmostEqual(frac2float([3, 1]), 3.0)

    def tearDown(self):
        pass
    
if __name__ == '__main__':
    unittest.main()