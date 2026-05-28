import tkinter as tk
from tkinter import messagebox


def my_numero_perfeito(numero):
    if numero <= 0:
        return False
    soma_divisores = sum(i for i in range(1, numero) if numero % i == 0)
    return soma_divisores == numero


def verificar_clique():
    try:
        n = int(entrada_num.get())
        if my_numero_perfeito(n):
            messagebox.showinfo("Resultado", f"{n} é um número perfeito!")
        else:
            messagebox.showinfo("Resultado", f"{n} não é um número perfeito.")
    except ValueError:
        messagebox.showerror("Erro", "Introduza um número válido.")


root = tk.Tk()
root.title("Verificador de Números Perfeitos")
root.geometry("350x200")
root.configure(bg="#e3f2fd")

tk.Label(root, text="Escreve um número inteiro:", bg="#e3f2fd").pack(pady=15)
entrada_num = tk.Entry(root)
entrada_num.pack()

tk.Button(root, text="Verificar", bg="#42a5f5", fg="white",
          command=verificar_clique).pack(pady=20)

root.mainloop()
