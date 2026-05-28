import tkinter as tk
from tkinter import messagebox


def calcular():
    try:
        x = float(entrada_x.get())
        y = float(entrada_y.get())
        resultados = f"""
Soma: {x + y}
Multiplicação: {x * y}
Divisão: {x / y if y != 0 else 'Divisão por zero'}
Subtração: {x - y}
Área do triângulo: {(x * y) / 2}
"""
        resultado_label.config(text=resultados)
    except ValueError:
        messagebox.showerror("Erro", "Por favor insira números válidos.")


# Janela principal
janela = tk.Tk()
janela.title("Calculadora GUI")

# Layout
tk.Label(janela, text="Número x:").grid(row=0, column=0, padx=10, pady=5)
entrada_x = tk.Entry(janela)
entrada_x.grid(row=0, column=1)
tk.Label(janela, text="Número y:").grid(row=1, column=0, padx=10, pady=5)
entrada_y = tk.Entry(janela)
entrada_y.grid(row=1, column=1)
btn_calcular = tk.Button(janela, text="Calcular", command=calcular)
btn_calcular.grid(row=2, column=0, columnspan=2, pady=10)
resultado_label = tk.Label(janela, text="", justify="left")
resultado_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
janela.mainloop()
