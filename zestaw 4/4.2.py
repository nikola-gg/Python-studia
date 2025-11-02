"""
Rozwiązania zadań 3.5 i 3.6 z poprzedniego zestawu zapisać w postaci funkcji,
które zwracają pełny string przez return. Funkcje nie powinny pytać użytkownika o dane, tylko korzystać z argumentów.

"""

def make_ruler(n):
    if not isinstance(n, int):
        raise ValueError("Argument 'n' musi być typu int.")
    if n < 0:
        raise ValueError("Argument 'n' nie może mieć wartości ujemnej.")
    scale_line = "|"
    labels_line = "0"
    for i in range(1, n+1):
        scale_line += "....|"
        labels_line += f"{i:>{5}}"
    
    result = scale_line + "\n" + labels_line
    return result

def make_grid(rows, cols):
    if not isinstance(rows, int) or not isinstance(cols, int):
        raise ValueError("Argumenty muszą być typu int.")
    if rows <= 0 or cols <= 0:
        raise ValueError("Argumenty muszą być dodatnie.")
    
    result = ""
    for i in range(rows):
        result += ("+---"*cols) + "+\n"
        result += ("|   "*cols) + "|\n"
    result += ("+---"*cols) + "+\n"
    return result

print(make_ruler(12))
print(make_grid(4, 5))