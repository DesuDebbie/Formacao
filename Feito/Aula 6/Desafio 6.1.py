import tkinter as tk
from tkinter import messagebox

caderneta = {
    "Ana": [15, 18, 14],
    "João": [10, 12, 11],
    "Maria": [20, 19, 20]
}


def calcular_media_aluno():
    nome = entrada_nome.get().strip()

    if nome in caderneta:
        notas = caderneta[nome]
        media = sum(notas) / len(notas)
        messagebox.showinfo("Resultado", f"Média de {nome}: {media:.2f}")
    else:
        messagebox.showerror("Erro", "Aluno não encontrado.")


root = tk.Tk()
root.title("Média de Notas")
root.geometry("350x200")
root.configure(bg="#e8f5e9")

tk.Label(root, text="Nome do Aluno:", bg="#e8f5e9").pack(pady=15)
entrada_nome = tk.Entry(root)
entrada_nome.pack()

tk.Button(root, text="Verificar Média",
          command=calcular_media_aluno).pack(pady=20)

root.mainloop()
