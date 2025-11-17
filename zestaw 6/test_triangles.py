import unittest
from triangles import Triangle
from points import Point

class TestTriangle(unittest.TestCase):
    def test_str(self):
        t = Triangle(1, 2, 3, 4, 5, 6)
        self.assertEqual(str(t), "[(1, 2), (3, 4), (5, 6)]")

    def test_repr(self):
        t = Triangle(1, 2, 3, 4, 5, 6)
        self.assertEqual(repr(t), "Triangle(1, 2, 3, 4, 5, 6)")

    def test_eq(self):
        t1 = Triangle(1, 2, 3, 4, 5, 6)
        t2 = Triangle(3, 4, 5, 6, 1, 2)
        t3 = Triangle(1, 2, 3, 4, 5, 7)

        self.assertTrue(t1 == t2)
        self.assertFalse(t1 == t3)

    def test_ne(self):
        t1 = Triangle(2, 3, 4, 5, 6, 7)
        t2 = Triangle(4, 5, 6, 7, 2, 3)
        t3 = Triangle(2, 3, 4, 5, 6, 8)

        self.assertFalse(t1 != t2)
        self.assertTrue(t1 != t3)

    def test_center(self):
        t = Triangle(1, 2, 4, 5, 7, 8)
        self.assertEqual(t.center(), Point(4, 5))

    def test_area(self):
        t = Triangle(1, 1, 5, 1, 3, 4)
        self.assertAlmostEqual(t.area(), 6.0)

    def test_move(self):
        t = Triangle(1, 2, 3, 4, 5, 6)
        t.move(1, 1)

        self.assertEqual(t.pt1, Point(2, 3))
        self.assertEqual(t.pt2, Point(4, 5))
        self.assertEqual(t.pt3, Point(6, 7))

if __name__ == "__main__":
    unittest.main()