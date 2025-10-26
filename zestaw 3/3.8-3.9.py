"""
Zadanie 3.8
Dla dwóch sekwencji liczb lub znaków znaleźć:
(a) listę elementów występujących jednocześnie w obu sekwencjach (bez powtórzeń),
(b) listę wszystkich elementów z obu sekwencji (bez powtórzeń).

"""
def ex_3_8():
    seq1 = [1, 2, 3, 6, 5, 0, 19]
    seq2 = [3, 4, 10, 2, 8]
    set1 = set(seq1)
    set2 = set(seq2)
    a = set1.intersection(set2) # lub set1 & set2
    b = set1.union(set2) # lub set1 | set2
    print("Zadanie 3.8 a):", list(a))
    print("Zadanie 3.8 b):", list(b))

"""
Zadanie 3.9
Mamy daną listę sekwencji (listy lub krotki) różnej długości zawierających liczby.
Znaleźć listę zawierającą sumy liczb z tych sekwencji.
Przykładowa sekwencja [[],[4],(1,2),[3,4],(5,6,7)], spodziewany wynik [0,4,3,7,18].
"""
def ex_3_9():
    seqs = [[], [4], (1,2), [3,4], (5,6,7)]
    mapped_sums = map(sum, seqs)
    result = list(mapped_sums)
    print("Zadanie 3.9:", result)


ex_3_8()
ex_3_9()