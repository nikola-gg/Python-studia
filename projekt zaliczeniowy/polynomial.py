class Polynomial:
    """
    Wielomian gęsty reprezentowany jako lista współczynników.
    [a0, a1, ..., an] oznacza a0 + a1*x + ... + an*x^n
    """

    # kontruktor
    def __init__(self, coefficients):
        if not coefficients:
            raise ValueError("Lista współczynników nie może być pusta")
    
        self.coefficients = list(coefficients)
        self._normalize()

    # usuwanie zbędnych zer z końca listy
    def _normalize(self):
        while len(self.coefficients) > 1 and self.coefficients[-1] == 0:
            self.coefficients.pop()

    # zamiana 'other' na wielomian, jeśli jeszcze nim nie jest
    @staticmethod
    def _as_poly(other):
        if isinstance(other, Polynomial):
            return other
        try:
            return Polynomial([other])
        except Exception:
            return NotImplemented
        

    # przydatne funkcje

    def is_zero(self):
        for coef in self.coefficients:
            if coef != 0:
                return False
        return True

    def degree(self):
        if self.is_zero():
            return -1
        return len(self.coefficients) - 1

    # dostęp przez []
    def __getitem__(self, power):
        if power < 0:
            raise IndexError("Potęga musi być >= 0")
        if power >= len(self.coefficients):
            return 0
        return self.coefficients[power]

    # dodawanie 
    def __add__(self, other):
        other = self._as_poly(other)
        if other is NotImplemented:
            return NotImplemented

        max_len = max(len(self.coefficients), len(other.coefficients))
        result = []
        for i in range(max_len):
            result.append(self[i] + other[i])

        return Polynomial(result)

    # odejmowanie
    def __sub__(self, other):
        other = self._as_poly(other)
        if other is NotImplemented:
            return NotImplemented

        max_len = max(len(self.coefficients), len(other.coefficients))
        result = []
        for i in range(max_len):
            result.append(self[i] - other[i])

        return Polynomial(result)

    # mnożenie
    def __mul__(self, other):
        other = self._as_poly(other)
        if other is NotImplemented:
            return NotImplemented

        size = len(self.coefficients) + len(other.coefficients) - 1
        result = [0] * size

        for i in range(len(self.coefficients)):
            for j in range(len(other.coefficients)):
                result[i + j] += self.coefficients[i] * other.coefficients[j]

        return Polynomial(result)

    # porównanie ====
    def __eq__(self, other):
        other = self._as_poly(other)
        if other is NotImplemented:
            return NotImplemented
        return (self - other).is_zero()

    # porównanie !=
    def __ne__(self, other):
        eq = self.__eq__(other)
        if eq is NotImplemented:
            return NotImplemented
        return not eq

    # Horner
    def __call__(self, x):
        value = 0
        for coef in reversed(self.coefficients):
            value = value * x + coef
        return value

    # wyświetlanie
    def __str__(self):
        if self.is_zero():
            return "0"

        parts = []

        for power, coef in enumerate(self.coefficients):
            if coef == 0:
                continue

            if power == 0:
                parts.append(str(coef))

            elif power == 1:
                if coef == 1:
                    parts.append("x")
                elif coef == -1:
                    parts.append("-x")
                else:
                    parts.append(f"{coef}x")

            else:
                if coef == 1:
                    parts.append(f"x^{power}")
                elif coef == -1:
                    parts.append(f"-x^{power}")
                else:
                    parts.append(f"{coef}x^{power}")

        return " + ".join(parts)

    # techniczna reprezentacja
    def __repr__(self):
        return f"Polynomial({self.coefficients})"
    
    # pochodna
    def derivative(self):
        if self.degree() <= 0:
            return Polynomial([0])

        result = []

        for power in range(1, len(self.coefficients)):
            result.append(power * self.coefficients[power])

        return Polynomial(result)

    # metody do obsługi: liczba + wielomian, liczba - wielomian, liczba * wielomian
    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        other = self._as_poly(other)
        if other is NotImplemented:
            return NotImplemented
        return other.__sub__(self)

    def __rmul__(self, other):
        return self.__mul__(other)