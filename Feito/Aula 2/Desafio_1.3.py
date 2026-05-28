import tkinter as tk
import math


def calcular():
    try:
        r = float(entrada_raio.get())
        area = math.pi * (r ** 2)
        resultado_label.config(text=f"A área da pizza é: {area:.2f}")

    except ValueError:
        resultado_label.config(text="Erro: Usa números (ex: 5 ou 5.5)")


janela = tk.Tk()
janela.title("Área do Círculo")

tk.Label(janela, text="Qual o raio do círculo?").pack(pady=10)
entrada_raio = tk.Entry(janela)
entrada_raio.pack(pady=5)

tk.Button(janela, text="Calcular Área", command=calcular).pack(pady=10)

resultado_label = tk.Label(janela, text="")
resultado_label.pack(pady=10)

janela.mainloop()
