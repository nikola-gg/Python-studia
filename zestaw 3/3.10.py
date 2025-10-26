"""
Stworzyć słownik tłumaczący liczby zapisane w systemie rzymskim (z literami I, V, X, L, C, D, M)
na liczby arabskie (podać kilka sposobów tworzenia takiego słownika).
Mile widziany kod tłumaczący całą liczbę [funkcja roman2int()].
"""

# 1 sposób 
dictionary = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
}

"""
2 sposób:
symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
values  = [1, 5, 10, 50, 100, 500, 1000]
combined = zip(symbols, values)
dictionary = dict(combined)
"""

def roman2int(roman):
    total = 0
    for i in range(len(roman)):
        if(i+1 < len(roman) and dictionary[roman[i]] < dictionary[roman[i+1]]):
            total -= dictionary[roman[i]]
        else:
            total += dictionary[roman[i]]
    return total


roman = str(input("Podaj liczbę rzymską: "))
arabic = roman2int(roman)
print(f"Liczba {roman} w systemie arabskim to {arabic}")

