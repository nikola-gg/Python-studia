import pytest
from triangles import Triangle
from points import Point


def test_str():
    t = Triangle(0, 0, 2, 0, 0, 2)
    assert str(t) == "[(0, 0), (2, 0), (0, 2)]"


def test_repr():
    t = Triangle(0, 0, 2, 0, 0, 2)
    assert repr(t) == "Triangle(0, 0, 2, 0, 0, 2)"


def test_eq_and_ne():
    t1 = Triangle(0, 0, 2, 0, 0, 2)
    t2 = Triangle(2, 0, 0, 2, 0, 0)
    t3 = Triangle(0, 0, 3, 0, 0, 2)

    assert t1 == t2
    assert not (t1 == t3)

    assert not (t1 != t2)
    assert t1 != t3


def test_center_property():
    t = Triangle(0, 0, 6, 0, 0, 6)
    assert t.center == Point(2, 2)


def test_area():
    t = Triangle(1, 1, 5, 1, 3, 4)
    assert pytest.approx(t.area(), rel=1e-9) == 6.0


def test_move():
    t = Triangle(0, 0, 2, 0, 0, 2)
    moved = t.move(1, 1)

    assert t.pt1 == Point(0, 0)
    assert t.pt2 == Point(2, 0)
    assert t.pt3 == Point(0, 2)

    assert moved.pt1 == Point(1, 1)
    assert moved.pt2 == Point(3, 1)
    assert moved.pt3 == Point(1, 3)


def test_collinear_raises_value_error():
    with pytest.raises(ValueError):
        Triangle(0, 0, 1, 1, 2, 2)


def test_make4_structure_and_area():
    t = Triangle(0, 0, 4, 0, 0, 4)
    t1, t2, t3, t4 = t.make4()

    # m_AB = (2,0), m_BC = (2,2), m_AC = (0,2)
    assert t1 == Triangle(0, 0, 2, 0, 0, 2)
    assert t2 == Triangle(0, 4, 0, 2, 2, 2)
    assert t3 == Triangle(2, 0, 0, 2, 2, 2)
    assert t4 == Triangle(4, 0, 2, 0, 2, 2)

    total_area = t1.area() + t2.area() + t3.area() + t4.area()
    assert pytest.approx(t.area(), rel=1e-9) == total_area


def test_from_points_creates_equivalent_triangle():
    p1 = Point(0, 0)
    p2 = Point(2, 0)
    p3 = Point(0, 2)

    t1 = Triangle(0, 0, 2, 0, 0, 2)
    t2 = Triangle.from_points((p1, p2, p3))
    assert t1 == t2


def test_from_points_accepts_list_as_well():
    p1 = Point(0, 0)
    p2 = Point(1, 0)
    p3 = Point(0, 1)

    t = Triangle.from_points([p1, p2, p3])
    assert t == Triangle(0, 0, 1, 0, 0, 1)


def test_from_points_wrong_length_raises_value_error():
    p1 = Point(0, 0)
    p2 = Point(1, 1)

    with pytest.raises(ValueError):
        Triangle.from_points((p1, p2))


def test_from_points_wrong_type_raises_type_error():
    p1 = Point(0, 0)
    p2 = Point(1, 1)

    with pytest.raises(TypeError):
        Triangle.from_points((p1, p2, (0, 0)))


def test_bounding_box_numeric_properties():
    t = Triangle(1, 2, 4, -1, -2, 3)

    assert t.left == -2
    assert t.right == 4
    assert t.bottom == -1
    assert t.top == 3
    assert t.width == 6
    assert t.height == 4


def test_bounding_box_point_properties():
    t = Triangle(1, 2, 4, -1, -2, 3)

    assert t.topleft == Point(-2, 3)
    assert t.bottomleft == Point(-2, -1)
    assert t.topright == Point(4, 3)
    assert t.bottomright == Point(4, -1)
