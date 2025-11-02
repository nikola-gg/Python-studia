"""
Mamy daną sekwencję, w której niektóre z elementów mogą okazać się podsekwencjami, a takie zagnieżdżenia mogą się nakładać do nieograniczonej głębokości.
Napisać funkcję flatten(sequence), która zwróci spłaszczoną listę wszystkich elementów sekwencji.
Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie czy element jest sekwencją, wykonać przez isinstance(item, (list, tuple)).

sequence = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print(flatten(sequence))   # [1,2,3,4,5,6,7,8,9]

"""

def flatten(sequence):
    if not isinstance(sequence, (list, tuple)):
        raise ValueError("Argument nie jest sekwencją.")
    
    def inner_flatten(seq):
        L = []
        for item in seq:
            if isinstance(item, (list, tuple)):
                L.extend(inner_flatten(item))
            elif isinstance(item, (float, int)):
                    L.append(item)
            else:
                raise ValueError(f"Nieobsługiwany element {item!r}")  
        return L      
    return inner_flatten(sequence)

print(flatten([1, 2, (2, 3, [], [2, [3, 1]])]))