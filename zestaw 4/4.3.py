"""
Napisać iteracyjną wersję funkcji factorial(n) obliczającej silnię.

"""

def factorial(n):
    if not isinstance(n, int):
        raise ValueError("Argument musi być typu int.")
    if n < 0:
        raise ValueError("Argument nie może być ujemny.")
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

print(factorial(3))