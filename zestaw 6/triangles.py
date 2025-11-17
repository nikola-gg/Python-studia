from points import Point

class Triangle:
    """Klasa reprezentująca trójkąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

    def __str__(self):         # "[(x1, y1), (x2, y2), (x3, y3)]"
        return f"[{str(self.pt1)}, {str(self.pt2)}, {str(self.pt3)}]"

    def __repr__(self):        # "Triangle(x1, y1, x2, y2, x3, y3)"
        return f"Triangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y}, {self.pt3.x}, {self.pt3.y})"
    
    def __eq__(self, other):   # obsługa tr1 == tr2
        # Trójkąty powinny być równe, jeżeli mają ten sam zbiór wierzchołków,
        # niezależnie od kolejności pt1, pt2, pt3.
        set_self = {self.pt1, self.pt2, self.pt3}
        set_other = {other.pt1, other.pt2, other.pt3}
        return set_self == set_other

    def __ne__(self, other):   # obsługa tr1 != tr2
        return not self == other

    def center(self):          # zwraca środek (masy) trójkąta
        return Point((self.pt1.x + self.pt2.x + self.pt3.x)/3, (self.pt1.y + self.pt2.y + self.pt3.y)/3)
    
    def area(self):            # pole powierzchni
        v1 = self.pt2 - self.pt1
        v2 = self.pt3 - self.pt1
        cross = v1.cross(v2)
        return abs(cross)/2

    def move(self, x, y):      # przesunięcie o (x, y)
        v = Point(x, y)
        self.pt1 += v
        self.pt2 += v
        self.pt3 += v