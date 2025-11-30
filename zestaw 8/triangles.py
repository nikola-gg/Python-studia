"""
W pliku triangles.py zdefiniować klasę Triangle wraz z potrzebnymi metodami.
Wykorzystać wyjątek ValueError do obsługi błędów.
Napisać kod testujący moduł triangles.

"""
from points import Point

class Triangle:
    """Klasa reprezentująca trójkąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        # Należy zabezpieczyć przed sytuacją, gdy punkty są współliniowe.
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

        AB = self.pt2 - self.pt1
        AC = self.pt3 - self.pt1
        cross_value = AB.cross(AC)
        if cross_value == 0:
            raise ValueError("Punkty trójkąta są współliniowe")
        
    @classmethod
    def from_points(cls, points):
        try:
            point1, point2, point3 = points
        except (TypeError, ValueError):
            raise ValueError("Należy podać iterowalny obiekt z dokładnie trzema punktami")

        if not all(isinstance(p, Point) for p in (point1, point2, point3)):
            raise TypeError("Elementy muszą być instancjami klasy Point")

        return cls(point1.x, point1.y, point2.x, point2.y, point3.x, point3.y)

    def __str__(self):         # "[(x1, y1), (x2, y2), (x3, y3)]"
        return f"[{str(self.pt1)}, {str(self.pt2)}, {str(self.pt3)}]"
    
    def __repr__(self):        # "Triangle(x1, y1, x2, y2, x3, y3)"
        return f"Triangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y}, {self.pt3.x}, {self.pt3.y})"
    
    def __eq__(self, other):   # obsługa tr1 == tr2
        # Trójkąty powinny być równe, jeżeli mają ten sam zbiór wierzchołków,
        # niezależnie od kolejności pt1, pt2, pt3.
        if not isinstance(other, Triangle):
            return NotImplemented
        set_self = {self.pt1, self.pt2, self.pt3}
        set_other = {other.pt1, other.pt2, other.pt3}
        return set_self == set_other

    def __ne__(self, other):        # obsługa tr1 != tr2
        return not self == other

    @property
    def center(self):          # zwraca środek trójkąta
        return Point((self.pt1.x + self.pt2.x + self.pt3.x)/3, (self.pt1.y + self.pt2.y + self.pt3.y)/3)
    
    def area(self):            # pole powierzchni
        v1 = self.pt2 - self.pt1
        v2 = self.pt3 - self.pt1
        cross = v1.cross(v2)
        return abs(cross)/2
    
    def move(self, x, y):      # przesunięcie o (x, y)
        return Triangle(
        self.pt1.x + x, self.pt1.y + y,
        self.pt2.x + x, self.pt2.y + y,
        self.pt3.x + x, self.pt3.y + y
    )

    def make4(self):           # zwraca krotkę czterech mniejszych
#     A       po podziale    A
#    / \                    / \
#   /   \                  +---+
#  /     \                / \ / \
# C-------B              C---+---B

        A = self.pt1
        B = self.pt2
        C = self.pt3
        m_AB = Point((A.x + B.x)/2, (A.y + B.y)/2)
        m_BC = Point((B.x + C.x)/2, (B.y + C.y)/2)
        m_AC = Point((A.x + C.x)/2, (A.y + C.y)/2)

        t1 = Triangle(A.x, A.y, m_AB.x, m_AB.y, m_AC.x, m_AC.y)
        t2 = Triangle(m_AC.x, m_AC.y, m_BC.x, m_BC.y, C.x, C.y)
        t3 = Triangle(m_AB.x, m_AB.y, m_AC.x, m_AC.y, m_BC.x, m_BC.y)
        t4 = Triangle(m_AB.x, m_AB.y, B.x, B.y, m_BC.x, m_BC.y)
        return (t1, t2, t3, t4)
    

    @property
    def left(self):
        return min(self.pt1.x, self.pt2.x, self.pt3.x)

    @property
    def right(self):
        return max(self.pt1.x, self.pt2.x, self.pt3.x)

    @property
    def bottom(self):
        return min(self.pt1.y, self.pt2.y, self.pt3.y)

    @property
    def top(self):
        return max(self.pt1.y, self.pt2.y, self.pt3.y)

    @property
    def width(self):
        return self.right - self.left

    @property
    def height(self):
        return self.top - self.bottom

    @property
    def topleft(self):
        return Point(self.left, self.top)

    @property
    def bottomleft(self):
        return Point(self.left, self.bottom)

    @property
    def topright(self):
        return Point(self.right, self.top)

    @property
    def bottomright(self):
        return Point(self.right, self.bottom)