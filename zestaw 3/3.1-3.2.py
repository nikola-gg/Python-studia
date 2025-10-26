"""
Zadanie 3.1
Czy podany kod jest poprawny składniowo w Pythonie? Jeśli nie, to dlaczego?

x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;

-> Nie jest poprawny, bo w pythonie nie używamy średników.
-------------------------------------------------------------------------

for i in "axby": if ord(i) < 100: print (i)

-> Nie, brakuje wcięcia
-------------------------------------------------------------------------

for i in "axby": print (ord(i) if ord(i) < 100 else i)

-> Tak, to poprawne wyrażenie warunkowe zapisane w jednej linii.

"""



"""
Zadanie 3.2
Co jest złego w kodzie:

L = [3, 5, 4] ; L = L.sort() -> nadpisanie listy L wartością None, którą zwraca .sort()
-------------------------------------------------------------------------

x, y = 1, 2, 3 -> dwie zmienne i 3 wartości
-------------------------------------------------------------------------

X = 1, 2, 3 ; X[1] = 4 -> X to krotka i nie da się zmienić jego wartości
-------------------------------------------------------------------------

X = [1, 2, 3] ; X[3] = 4 -> indeksy są od zera, czyli [3] jest poza zakresem
-------------------------------------------------------------------------

X = "abc" ; X.append("d") -> metoda .append() nie działa na stringach
-------------------------------------------------------------------------

L = list(map(pow, range(8))) -> funkcja pow() dostaje 1 argument, a potrzebuje dwóch

"""