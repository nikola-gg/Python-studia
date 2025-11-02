"""
Napisać funkcję odwracanie(L, left, right) odwracającą kolejność elementów na liście od numeru left do right włącznie.
Lista jest modyfikowana w miejscu (in place).
Rozważyć wersję iteracyjną i rekurencyjną.

"""
# wersja iteracyjna
def odwracanie_it(L, left, right):
    if not isinstance(L, list):
        raise ValueError("Argument 'L' musi być typu list.")
    if not isinstance(left, int) or not isinstance(right, int):
        raise ValueError("Argumenty 'left' oraz 'right' muszą być typu int.")
    if left < 0 or right < left or right < 0 or right >= len(L):
        raise ValueError("Nieprawidłowy zakres indeksów.")
    
    while(left < right):
        L[left], L[right] = L[right], L[left]
        left +=1
        right -= 1
    
    return L

print(odwracanie_it([1, 2, 3, 4, 5, 6], 1, 5))

# wersja rekurencyjna
def odwracanie_rek(L, left, right, _first=True):
    if _first:
        if not isinstance(L, list):
            raise ValueError("Argument 'L' musi być typu list.")
        if not isinstance(left, int) or not isinstance(right, int):
            raise ValueError("Argumenty 'left' oraz 'right' muszą być typu int.")
        if left < 0 or right < left or right < 0 or right >= len(L):
            raise ValueError("Nieprawidłowy zakres indeksów.")
    
    if left >= right:
        return L
    
    L[left], L[right] = L[right], L[left]
    return odwracanie_rek(L, left+1, right-1, _first=False)

print(odwracanie_rek([1, 2, 3, 4, 5, 6], 1, 5))    