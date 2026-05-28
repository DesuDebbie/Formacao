import tkinter as tk
from tkinter import messagebox


def contar_caracteres():
    texto = entrada_texto.get()
    contagem = {}

    for caractere in texto:
        if caractere in contagem:
            contagem[caractere] += 1
        else:
            contagem[caractere] = 1

    resultado = "Contagem:\n"
    for chave, valor in contagem.items():
        resultado += f"'{chave}': {valor}\n"

    messagebox.showinfo("Resultado", resultado)


root = tk.Tk()
root.title("Contador")
root.geometry("350x250")
root.configure(bg="#fff3e0")

tk.Label(root, text="Introduza o texto:", bg="#fff3e0").pack(pady=20)
entrada_texto = tk.Entry(root, width=30)
entrada_texto.pack()

tk.Button(root, text="Contar", command=contar_caracteres).pack(pady=20)

root.mainloop()
