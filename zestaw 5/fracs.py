"""
Stworzyć plik fracs.py i zapisać w nim funkcje do działań na ułamkach.
Ułamek będzie reprezentowany przez listę dwóch liczb całkowitych [licznik, mianownik].
Napisać kod testujący moduł fracs. Nie należy korzystać z klasy Fraction z modułu fractions.
Można wykorzystać funkcję fractions.gcd() [Py2, zwraca liczby dodatnie
lub ujemne] lub math.gcd() [Py3, zwraca liczby nieujemne] implementującą algorytm Euklidesa.

"""

from math import gcd 

def _normalize(frac):
    if not isinstance(frac, list) or len(frac) != 2:
        raise TypeError("Ułamek musi być w postaci listy [licznik, mianownik]")
    
    n, d = frac
    if d == 0:
        raise ZeroDivisionError("Mianownik nie może być zerem.")

    if d < 0:
        n, d = -n, -d

    return [n, d]

def _reduce(frac):
    n, d = _normalize(frac)
    if n == 0:
        return [0, 1]
    nwd = gcd(abs(n), d)
    return [n // nwd, d // nwd]

def add_frac(frac1, frac2):             # frac1 + frac2
    n1, d1 = _normalize(frac1)
    n2, d2 = _normalize(frac2)
    n = n1*d2 + n2*d1
    d = d1*d2
    return _reduce([n, d])

def sub_frac(frac1, frac2):             # frac1 - frac2
    n1, d1 = _normalize(frac1)
    n2, d2 = _normalize(frac2)
    n = n1*d2 - n2*d1
    d = d1*d2
    return _reduce([n, d])

def mul_frac(frac1, frac2):             # frac1 * frac2
    n1, d1 = _normalize(frac1)
    n2, d2 = _normalize(frac2)
    n = n1*n2
    d = d1*d2
    return _reduce([n, d])

def div_frac(frac1, frac2):             # frac1 / frac2
    n1, d1 = _normalize(frac1)
    n2, d2 = _normalize(frac2)
    if n2 == 0:
        raise ZeroDivisionError("Dzielenie przez zero.")
    n = n1*d2
    d = d1*n2
    return _reduce([n, d])

def is_positive(frac):                  # bool, czy dodatni
    n, d = _normalize(frac)
    return n > 0

def is_zero(frac):                      # bool, typu [0, x]
    n, d = _normalize(frac)
    return n == 0

def cmp_frac(frac1, frac2):             # -1 | 0 | +1
    n1, d1 = _normalize(frac1)
    n2, d2 = _normalize(frac2)
    diff = n1*d2 - n2*d1
    if diff == 0:
        return 0
    elif diff < 0:
        return -1
    else:
        return 1

def frac2float(frac):                   # konwersja do float
    n, d = _normalize(frac)
    return n / d