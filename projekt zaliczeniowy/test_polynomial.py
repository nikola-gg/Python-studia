import unittest
from polynomial import Polynomial


class TestPolynomial(unittest.TestCase):

    def test_constructor_empty_list(self):
        with self.assertRaises(ValueError):
            Polynomial([])

    def test_constructor_only_zeros(self):
        p = Polynomial([0, 0, 0])
        self.assertTrue(p.is_zero())
        self.assertEqual(p.degree(), -1)

    def test_add(self):
        p = Polynomial([1, 2])
        q = Polynomial([3, 4])
        self.assertEqual(p + q, Polynomial([4, 6]))

    def test_add_different_degrees(self):
        p = Polynomial([1])
        q = Polynomial([0, 2, 3])
        self.assertEqual(p + q, Polynomial([1, 2, 3]))

    def test_add_zero(self):
        p = Polynomial([1, -2, 3])
        z = Polynomial([0])
        self.assertEqual(p + z, p)
        self.assertEqual(z + p, p)

    def test_sub(self):
        p = Polynomial([5, 0, 1])
        q = Polynomial([2, 1])
        self.assertEqual(p - q, Polynomial([3, -1, 1]))

    def test_sub_self(self):
        p = Polynomial([3, 4, 5])
        self.assertTrue((p - p).is_zero())

    def test_mul(self):
        p = Polynomial([1, 1])
        q = Polynomial([1, -1])
        self.assertEqual(p * q, Polynomial([1, 0, -1]))

    def test_mul_by_zero(self):
        p = Polynomial([2, 3])
        z = Polynomial([0])
        self.assertTrue((p * z).is_zero())
        self.assertTrue((z * p).is_zero())

    def test_mul_by_constant(self):
        p = Polynomial([1, 2, 3])
        c = Polynomial([5])
        self.assertEqual(p * c, Polynomial([5, 10, 15]))

    def test_eval(self):
        p = Polynomial([1, 2, 3])
        self.assertEqual(p(2), 17)

    def test_eval_zero(self):
        p = Polynomial([0])
        self.assertEqual(p(100), 0)

    def test_eval_negative_x(self):
        p = Polynomial([1, 0, 1])
        self.assertEqual(p(-2), 5)

    def test_eq(self):
        p = Polynomial([1, 2, 3, 0, 0])
        q = Polynomial([1, 2, 3])
        self.assertTrue(p == q)
        self.assertFalse(p != q)

    def test_not_eq(self):
        p = Polynomial([1, 2])
        q = Polynomial([1, 2, 0, 1])
        self.assertFalse(p == q)

    def test_zero_and_degree(self):
        p = Polynomial([0])
        q = Polynomial([0, 0, 0])
        r = Polynomial([1, 0, 0])

        self.assertTrue(p.is_zero())
        self.assertTrue(q.is_zero())
        self.assertFalse(r.is_zero())

        self.assertEqual(p.degree(), -1)
        self.assertEqual(r.degree(), 0)

    def test_getitem(self):
        p = Polynomial([7, 8])
        self.assertEqual(p[0], 7)
        self.assertEqual(p[1], 8)
        self.assertEqual(p[5], 0)

        with self.assertRaises(IndexError):
            _ = p[-1]

    def test_getitem_high_degree(self):
        p = Polynomial([1, 2, 3])
        self.assertEqual(p[100], 0)

    def test_str(self):
        self.assertEqual(str(Polynomial([0])), "0")
        self.assertEqual(str(Polynomial([1])), "1")
        self.assertEqual(str(Polynomial([0, 1])), "x")
        self.assertEqual(str(Polynomial([0, -1])), "-x")
        self.assertEqual(str(Polynomial([2, 1, 1])), "2 + x + x^2")

    def test_str_with_gaps(self):
        p = Polynomial([0, 0, 3, 0, 1])
        self.assertEqual(str(p), "3x^2 + x^4")

    def test_str_negative_coeffs(self):
        p = Polynomial([0, -1, -2])
        self.assertEqual(str(p), "-x + -2x^2")

    def test_derivative_basic(self):
        p = Polynomial([1, 2, 3])
        self.assertEqual(p.derivative(), Polynomial([2, 6]))

    def test_derivative_constant(self):
        p = Polynomial([5])
        self.assertEqual(p.derivative(), Polynomial([0]))

    def test_derivative_zero(self):
        p = Polynomial([0])
        self.assertEqual(p.derivative(), Polynomial([0]))

    def test_derivative_with_gaps(self):
        p = Polynomial([0, 0, 3, 0, 1])
        self.assertEqual(p.derivative(), Polynomial([0, 6, 0, 4]))


if __name__ == "__main__":
    unittest.main()
