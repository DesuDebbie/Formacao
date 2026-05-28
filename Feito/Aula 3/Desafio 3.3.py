import tkinter as tk
from tkinter import messagebox


def listar_ate_zero():
    try:
        n = int(entrada_n.get())
        if n >= 0:
            lista_numeros = [str(i) for i in range(n, -1, -1)]
            resultado_final = "\n".join(lista_numeros)
            messagebox.showinfo("Resultado", resultado_final)
        else:
            messagebox.showerror("Erro", "Indique um número >= 0")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida")


root = tk.Tk()
root.title("Contagem Decrescente")
root.geometry("300x200")
root.configure(bg="#b2fab4")

tk.Label(root, text="Indica um número (n):", bg="#b2fab4").pack(pady=10)
entrada_n = tk.Entry(root)
entrada_n.pack(pady=5)

tk.Button(root, text="Listar", command=listar_ate_zero).pack(pady=15)

root.mainloop()
