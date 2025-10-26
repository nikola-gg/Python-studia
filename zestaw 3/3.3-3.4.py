def ex_3_3():
    """
    Wypisać w pętli liczby od 0 do 30 z wyjątkiem liczb podzielnych przez 3. Użyć pętli for lub while.
    
    """
    print("Zadanie 3.3:")
    for i in range(31):
        if i % 3 != 0:
            print(i)
    print("\n")

def ex_3_4():
    """
    Napisać program pobierający w pętli od użytkownika liczbę rzeczywistą x (typ float) i wypisujący x oraz trzecią potęgę x.
    Zatrzymanie programu następuje po wpisaniu z klawiatury stop.
    Jeżeli użytkownik wpisze napis zamiast liczby, to program ma wypisać komunikat o błędzie i kontynuować pracę.

    """
    print("Zadanie 3.4:")
    dane = input("Podaj liczbę float, aby przerwać napisz 'stop': ")
    while dane != "stop":
        try:
            x = float(dane)
            print(x, pow(x, 3))
        except ValueError:
            print("Błąd - spróbuj ponownie i wpisz liczbę.")

        dane = input("Podaj liczbę float, aby przerwać napisz 'stop': ")



ex_3_3()
ex_3_4()