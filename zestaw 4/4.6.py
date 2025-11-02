"""
Napisać funkcję sum_seq(sequence) obliczającą sumę liczb zawartych w sekwencji, która
może zawierać zagnieżdżone podsekwencje.
Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie, czy element
jest sekwencją, wykonać przez isinstance(item, (list, tuple)).

"""

def sum_seq(sequence):
    if not isinstance(sequence, (list, tuple)):
        raise ValueError("Argument nie jest sekwencją.")
    
    def inner_sum(seq):
        total = 0
        for item in seq:
            if isinstance(item, (list, tuple)):
                total += inner_sum(item)
            elif isinstance(item, (float, int)):
                    total += item
            else:
                raise ValueError(f"Nieobsługiwany element {item!r}")        
        return total
    return inner_sum(sequence)

print(sum_seq([1, 2, [3, (9, [1], 5), 1]]))