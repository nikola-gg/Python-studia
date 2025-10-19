def ex_2_10():
    line = "To  przykladowy., napis..\tbede     robic\nna\njego przykladzie\nzadanie."
    words = line.split()
    print("2.10:")
    print("Liczba slów w stringu line:",len(words),"\n")

def ex_2_11():
    word = "abcdefghijklmnopqrstuvwxyz"
    new_word = ""
    for x in word:
        if x != word[-1]:
            new_word = new_word + x + "_"
        else:
            new_word = new_word + x
    print("2.11:")
    print(new_word)
    print("_".join(word),"\n")

def ex_2_12():
    line = "to jest string skladajacy sie z wielu slow"
    words = line.split()
    first_letters = ""
    last_letters = ""
    for x in words:
        first_letters += x[0]
        last_letters += x[-1]
    print("2.12:")
    print("String z pierwszych liter:", first_letters)
    print("String z ostatnich liter:", last_letters,"\n")

def ex_2_13():
    line = "to jest string skladajacy sie z wielu slow"
    words = line.split()
    print("2.13:")
    print("Łączna długość wyrazów:", sum(len(x) for x in words), "\n")

def ex_2_14():
    line = "to jest string skladajacy sie z wielu slow"
    words = line.split()
    print("2.14:")
    print("Najdłuższy wyraz:", max(words,key=len))
    print("Długość najdłuższego wyrazu:", len(max(words,key = len)), "\n")

def ex_2_15():
    L = [22, 32, 190, 2, 18]
    print("2.15:")
    print("".join(map(str, L)), "\n")

def ex_2_16():
    line = "to jest string GvR skladajacy sie z wielu slow"
    print("2.16:")
    print(line.replace("GvR", "Guido van Rossum"),"\n")

def ex_2_17():
    line = "to jest string skladajacy sie z wielu slow"
    words = line.split()
    sorted_alphabetically = sorted(words)
    sorted_by_length = sorted(words, key = len)
    print("2.17:")
    print("Posortowane alfabetycznie:", sorted_alphabetically)
    print("posortowane wg długości:", sorted_by_length, "\n")

def ex_2_18():
    a = 1129230393002939302908
    word = str(a)
    zero_count = word.count("0")
    print("2.18:")
    print("Liczba wystąpień cyfry 0:", zero_count, "\n")

def ex_2_19():
    L = [1, 22, 333, 43, 19, 8]
    str_numbers = [str(x) for x in L]
    filled = [x.zfill(3) for x in str_numbers]
    result = "".join(filled)
    print("2.19:")
    print("Ciąg trzycyfrowych liczb:", result, "\n")


ex_2_10()
ex_2_11()
ex_2_12()
ex_2_13()
ex_2_14()
ex_2_15()
ex_2_16()
ex_2_17()
ex_2_18()
ex_2_19()