import tkinter as tk
from tkinter import messagebox

inventario = {
    "Cadernos": 10,
    "Canetas": 50,
    "Lápis": 30
}


def consultar_produto():
    produto = entrada_produto.get().strip()

    if produto in inventario:
        messagebox.showinfo("Resultado", f"O produto '{produto}' existe.")
    else:
        messagebox.showwarning(
            "Resultado", f"O produto '{produto}' não existe.")


root = tk.Tk()
root.title("Consulta Inventário")
root.geometry("300x200")

tk.Label(root, text="Nome do Produto:").pack(pady=10)
entrada_produto = tk.Entry(root)
entrada_produto.pack()

tk.Button(root, text="Verificar", command=consultar_produto).pack(pady=20)

root.mainloop()
