def ex_3_5():
    """
    Napisać program rysujący "miarkę" o zadanej długości.
    Należy prawidłowo obsłużyć liczby składające się z kilku cyfr (ostatnia cyfra liczby ma znajdować się
    pod znakiem kreski pionowej). Należy zbudować pełny string, a potem go wypisać.

    |....|....|....|....|....|....|....|....|....|....|....|....|
    0    1    2    3    4    5    6    7    8    9   10   11   12

    """
    size = int(input("Zadanie 3.5\nPodaj długość miarki: "))
    scale_line = "|"
    labels_line = "0"
    for i in range(1, size+1):
        scale_line += "....|"
        labels_line += f"{i:>{5}}"
    
    result = scale_line + "\n" + labels_line
    print(result)

def ex_3_6():
    """
    Napisać program rysujący prostokąt zbudowany z małych kratek.
    Należy zbudować pełny string, a potem go wypisać.
    Przykładowy prostokąt składający się 2 x 4 pól ma postać:

    +---+---+---+---+
    |   |   |   |   |
    +---+---+---+---+
    |   |   |   |   | 
    +---+---+---+---+

    """
    height = int(input("Zadanie 3.6\nPodaj wysokość prostokąta: "))
    width = int(input("Podaj szerokość prostokąta: "))
    result = ""
    
    for i in range(height):
        result += ("+---"*width) + "+\n"
        result += ("|   "*width) + "|\n"
    result += ("+---"*width) + "+\n"

    print(result)

ex_3_5()
ex_3_6()
    