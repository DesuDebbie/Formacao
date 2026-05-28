import tkinter as tk
from tkinter import messagebox


def fatorial(num):
    return 1 if num <= 1 else num * fatorial(num - 1)


def calcular():
    try:
        n, p = int(ent_n.get()), int(ent_p.get())
        if n < 0 or p < 0 or p > n:
            messagebox.showerror(
                "Erro", "Valores inválidos (n>=p e positivos).")
            return

        res = fatorial(n) // (fatorial(p) * fatorial(n - p))
        lbl_res.config(text=f"Resultado: {res}")
    except ValueError:
        messagebox.showerror("Erro", "Insira números inteiros.")


root = tk.Tk()
root.title("Calculadora de Combinações")
root.geometry("400x300")
root.configure(bg="#eaf4f4")

tk.Label(root, text="Cálculo de Combinações", font=(
    "Arial", 14), bg="#eaf4f4").pack(pady=20)
ent_n = tk.Entry(root)
ent_n.pack(pady=5)
ent_p = tk.Entry(root)
ent_p.pack(pady=5)

tk.Button(root, text="Calcular", command=calcular).pack(pady=20)
lbl_res = tk.Label(root, text="", bg="#eaf4f4")
lbl_res.pack()

root.mainloop()
