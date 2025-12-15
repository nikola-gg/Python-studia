import tkinter as tk
import random

def rzut_kostka():
    wynik = random.randint(1, 6)
    label_wynik.config(text=f"Wynik: {wynik}")

# okno
root = tk.Tk()
root.title("Rzut kostką")
root.geometry("320x220")
root.resizable(False, False)
root.configure(bg="#ffe6f0")

# tytuł
label_tytul = tk.Label(
    root,
    text="Symulator rzutu kostką",
    font=("Arial", 14, "bold"),
    bg="#ffe6f0"
)
label_tytul.pack(pady=15)

# wynik
label_wynik = tk.Label(
    root,
    text="Wynik: -",
    font=("Arial", 24),
    bg="#ffe6f0"
)
label_wynik.pack(pady=20)

# przycisk
button_rzut = tk.Button(
    root,
    text="Rzuć kostką",
    font=("Arial", 14),
    bg="#ff69b4",
    fg="white",
    activebackground="#ff85c1",
    activeforeground="white",
    padx=15,
    pady=5,
    command=rzut_kostka
)
button_rzut.pack(pady=10)

root.mainloop()
