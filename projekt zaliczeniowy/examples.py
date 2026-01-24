from polynomial import Polynomial

# Przykłady użycia klasy Polynomial

p = Polynomial([1, 2, 3]) # 1 + 2x + 3x^2
q = Polynomial([0, 1, -3]) # x - 3x^2

print("Wielomiany:")
print("p(x) =", p)
print("q(x) =", q)
print()

print("Operacje arytmetyczne:")
print("p + q =", p + q)
print("p - q =", p - q)
print("p * q =", p * q)
print()

x = 2
print("Obliczanie wartości:")
print(f"p({x}) =", p(x))
print()

print("Dostęp do współczynników wielomianu p:")
print("współczynnik przy x^2:", p[2])
print("współczynnik przy x^5:", p[5])   # poza stopniem = 0
print()

print("Informacje o wielomianie:")
print("stopień p:", p.degree())
print("czy p jest zerowy?", p.is_zero())
print()

r = Polynomial([1, 2, 3, 0, 0])

print("Porównywanie:")
print("p =", p)
print("r =", r)
print("p == r ?", p == r)
print("p != r ?", p != r)
print()


print("Pochodna wielomianu p:")
print("p'(x) =", p.derivative())
print()


print("Operacje z liczbą:")
print("p + 5 =", p + 5)
print("5 + p =", 5 + p)
print("p - 2 =", p - 2)
print("2 - p =", 2 - p)
print("p * 3 =", p * 3)
print("3 * p =", 3 * p)
print()

print("Porównywanie z liczbą:")
print("p == 5 ?", p == 5)
print("5 == Polynomial([5]) ?", 5 == Polynomial([5]))
print()