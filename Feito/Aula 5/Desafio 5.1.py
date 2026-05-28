import tkinter as tk
from tkinter import messagebox


def gerar_triangulo_simples(linhas):
    triangulo = ""
    for i in range(1, linhas + 1):
        for j in range(1, i + 1):
            triangulo += str(j)
        triangulo += "\n"
    return triangulo


def gerar_triangulo_espacos(linhas):
    triangulo = ""
    for i in range(1, linhas + 1):
        espacos = " " * (linhas - i)
        triangulo += espacos
        for j in range(1, i + 1):
            triangulo += str(j)
        triangulo += "\n"
    return triangulo


def processar_clique():
    try:
        num_linhas = int(entrada_linhas.get())
        if num_linhas <= 0:
            messagebox.showerror("Erro", "Insira um número > 0")
            return

        if opcao.get() == "simples":
            resultado = gerar_triangulo_simples(num_linhas)
        else:
            resultado = gerar_triangulo_espacos(num_linhas)

        messagebox.showinfo("Triângulo", resultado)

    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida.")


root = tk.Tk()
root.title("Triângulos de Números")
root.geometry("400x300")
root.configure(bg="#fdfce9")

tk.Label(root, text="Gerador de Triângulos", font=(
    "Arial", 14), bg="#fdfce9").pack(pady=15)
tk.Label(root, text="Digite o número de linhas:", bg="#fdfce9").pack()
entrada_linhas = tk.Entry(root, width=10)
entrada_linhas.pack(pady=5)

opcao = tk.StringVar(value="simples")
tk.Radiobutton(root, text="Simples", variable=opcao,
               value="simples", bg="#fdfce9").pack()
tk.Radiobutton(root, text="Com Espaços", variable=opcao,
               value="espacos", bg="#fdfce9").pack()

tk.Button(root, text="Exibir Triângulo",
          command=processar_clique).pack(pady=20)

root.mainloop()
