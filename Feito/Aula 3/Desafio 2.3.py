import tkinter as tk


def calcular_peso_ideal(altura):
    peso_ideal_homem = (72.7 * altura) - 58
    peso_ideal_mulher = (62.1 * altura) - 44.7
    return peso_ideal_homem, peso_ideal_mulher


def executar_calculo():
    try:
        altura = float(entrada_altura.get())
        peso_h, peso_m = calcular_peso_ideal(altura)
        label_homem.config(text=f"Homem: {peso_h:.2f} kg")
        label_mulher.config(text=f"Mulher: {peso_m:.2f} kg")
    except ValueError:
        label_homem.config(text="Erro: Insira altura válida")


root = tk.Tk()
root.title("Calculadora de Peso Ideal")
root.geometry("350x250")
root.configure(bg="#add8e6")

tk.Label(root, text="Digite a altura da pessoa (em metros):",
         bg="#add8e6").pack(pady=10)
entrada_altura = tk.Entry(root)
entrada_altura.pack(pady=5)

tk.Button(root, text="Calcular Peso Ideal",
          command=executar_calculo).pack(pady=10)

label_homem = tk.Label(root, text="", bg="#add8e6")
label_homem.pack(pady=5)
label_mulher = tk.Label(root, text="", bg="#add8e6")
label_mulher.pack(pady=5)

root.mainloop()
