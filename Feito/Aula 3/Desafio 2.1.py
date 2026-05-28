import tkinter as tk


def verificar_maior():
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
        n3 = float(entrada3.get())

        if n1 >= n2 and n1 >= n3:
            maior = n1
        elif n2 >= n1 and n2 >= n3:
            maior = n2
        else:
            maior = n3

        resultado_label.config(text=f"{maior} é o maior número.")
    except ValueError:
        resultado_label.config(text="Erro: Insira apenas números.")


janela = tk.Tk()
janela.title("Desafio: Maior de 3")

tk.Label(janela, text="Digite o primeiro número:").pack(pady=5)
entrada1 = tk.Entry(janela)
entrada1.pack()

tk.Label(janela, text="Digite o segundo número:").pack(pady=5)
entrada2 = tk.Entry(janela)
entrada2.pack()

tk.Label(janela, text="Digite o terceiro número:").pack(pady=5)
entrada3 = tk.Entry(janela)
entrada3.pack()

tk.Button(janela, text="Verificar Maior",
          command=verificar_maior).pack(pady=15)

resultado_label = tk.Label(janela, text="", font=("Arial", 10, "bold"))
resultado_label.pack(pady=5)

janela.mainloop()
