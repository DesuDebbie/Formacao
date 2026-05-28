import tkinter as tk
from tkinter import messagebox


def e_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True


def verificar_primo_gui():
    try:
        num = int(entrada_num.get())
        if e_primo(num):
            messagebox.showinfo("Resultado", f"{num} é um número primo!")
        else:
            messagebox.showinfo("Resultado", f"{num} não é um número primo.")
    except ValueError:
        messagebox.showerror("Erro", "Digite um número inteiro válido.")


root = tk.Tk()
root.title("Verificador de Números Primos")
root.geometry("350x200")
root.configure(bg="#f5f5f5")

tk.Label(root, text="Escreve um número inteiro:", bg="#f5f5f5").pack(pady=15)
entrada_num = tk.Entry(root)
entrada_num.pack()

tk.Button(root, text="Verificar", bg="#1976d2", fg="white",
          command=verificar_primo_gui).pack(pady=20)

root.mainloop()
