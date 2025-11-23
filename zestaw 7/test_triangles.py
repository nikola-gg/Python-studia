import unittest
from triangles import Triangle
from points import Point

class TestTriangle(unittest.TestCase):

    def test_str(self):
        t = Triangle(0, 0, 2, 0, 0, 2)
        self.assertEqual(str(t), "[(0, 0), (2, 0), (0, 2)]")

    def test_repr(self):
        t = Triangle(0, 0, 2, 0, 0, 2)
        self.assertEqual(repr(t), "Triangle(0, 0, 2, 0, 0, 2)")

    def test_eq(self):
        t1 = Triangle(0, 0, 2, 0, 0, 2)
        t2 = Triangle(2, 0, 0, 2, 0, 0)
        t3 = Triangle(0, 0, 3, 0, 0, 2)

        self.assertTrue(t1 == t2)
        self.assertFalse(t1 == t3)

    def test_ne(self):
        t1 = Triangle(0, 0, 2, 0, 0, 2)
        t2 = Triangle(2, 0, 0, 2, 0, 0)
        t3 = Triangle(0, 0, 3, 0, 0, 2)

        self.assertFalse(t1 != t2)
        self.assertTrue(t1 != t3)

    def test_center(self):
        t = Triangle(0, 0, 6, 0, 0, 6)
        self.assertEqual(t.center(), Point(2, 2))

    def test_area(self):
        t = Triangle(1, 1, 5, 1, 3, 4)
        self.assertAlmostEqual(t.area(), 6.0)

    def test_move(self):
        t = Triangle(0, 0, 2, 0, 0, 2)
        moved = t.move(1, 1)

        self.assertEqual(t.pt1, Point(0, 0))
        self.assertEqual(t.pt2, Point(2, 0))
        self.assertEqual(t.pt3, Point(0, 2))

        self.assertEqual(moved.pt1, Point(1, 1))
        self.assertEqual(moved.pt2, Point(3, 1))
        self.assertEqual(moved.pt3, Point(1, 3))

    def test_collinear_raises_value_error(self):
        with self.assertRaises(ValueError):
            Triangle(0, 0, 1, 1, 2, 2)

    def test_make4_structure_and_area(self):
        t = Triangle(0, 0, 4, 0, 0, 4)
        t1, t2, t3, t4 = t.make4()

        # m_AB = (2,0), m_BC = (2,2), m_AC = (0,2)

        self.assertEqual(t1, Triangle(0, 0, 2, 0, 0, 2))
        self.assertEqual(t2, Triangle(0, 4, 0, 2, 2, 2))
        self.assertEqual(t3, Triangle(2, 0, 0, 2, 2, 2))
        self.assertEqual(t4, Triangle(4, 0, 2, 0, 2, 2))

        total_area = t1.area() + t2.area() + t3.area() + t4.area()
        self.assertAlmostEqual(t.area(), total_area)


if __name__ == "__main__":
    unittest.main()
