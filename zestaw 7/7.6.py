"""
Stworzyć następujące iteratory nieskończone:
(a) zwracający 0, 1, 0, 1, 0, 1, ...,
(b) zwracający przypadkowo jedną wartość z ("N", "E", "S", "W") [błądzenie przypadkowe na sieci kwadratowej 2D],
(c) zwracający 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, ... [numery dni tygodnia].

"""
import random

class IteratorA:
    def __iter__(self):
        self.value = 0
        return self
    
    def __next__(self):
        current = self.value
        if self.value == 0:
            self.value = 1
        else:
            self.value = 0
        return current
    
class IteratorB:
    def __init__(self):
        self.directions = ["N", "E", "S", "W"]

    def __iter__(self):
        return self
    
    def __next__(self):
        return random.choice(self.directions)
    
class IteratorC:
    def __iter__(self):
        self.day = 0
        return self
    
    def __next__(self):
        current = self.day
        self.day = (self.day + 1) % 7
        return current
    
if __name__ == "__main__":
    print("test IteratorA:")
    itA = iter(IteratorA())
    for _ in range(10):
        print(next(itA), end=" ")
    print("\n")

    print("test IteratorB:")
    itB = iter(IteratorB())
    for _ in range(10):
        print(next(itB), end=" ")
    print("\n")

    print("test IteratorC:")
    itC = iter(IteratorC())
    for _ in range(10):
        print(next(itC), end=" ")
    print("\n")