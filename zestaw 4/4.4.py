"""
Napisać iteracyjną wersję funkcji fibonacci(n) obliczającej n-ty wyraz ciągu Fibonacciego.

"""

def fibonacci(n):
    if not isinstance(n, int):
        raise ValueError("Argument musi być typu int.")
    if n < 0:
        raise ValueError("Argument nie może być ujemny.")
    prev = 0
    current = 1
    result = 0
    for i in range(n-1):
        result = prev + current
        prev = current
        current = result
    return result

print(fibonacci(11))