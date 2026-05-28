import tkinter as tk
from tkinter import messagebox


def criar_tuplo_clique():
    try:
        entrada = entrada_texto.get().strip()
        if not entrada:
            messagebox.showerror("Erro", "Entrada vazia!")
            return

        meu_tuplo = tuple(int(n) for n in entrada.split())
        quantidade = len(meu_tuplo)

        res = f"O tuplo inserido é: {meu_tuplo}\nO tuplo contém {quantidade} elementos."
        messagebox.showinfo("Resultado", res)
    except ValueError:
        messagebox.showerror("Erro", "Use apenas números inteiros e espaços.")


root = tk.Tk()
root.title("Criar Tuple")
root.geometry("400x250")
root.configure(bg="#f08080")

tk.Label(root, text="Introduza os números:",
         bg="#f08080", fg="white").pack(pady=20)
entrada_texto = tk.Entry(root, width=30)
entrada_texto.pack()

tk.Button(root, text="Criar Tuple", command=criar_tuplo_clique).pack(pady=20)

root.mainloop()
