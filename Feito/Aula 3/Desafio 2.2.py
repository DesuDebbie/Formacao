import tkinter as tk


def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


def converter_temperatura_gui():
    try:
        temp = float(entrada_temp.get())
        if opcao.get() == 1:
            resultado = celsius_para_fahrenheit(temp)
            label_resultado.config(
                text=f"Temperatura em Fahrenheit: {resultado:.2f}")
        else:
            resultado = fahrenheit_para_celsius(temp)
            label_resultado.config(
                text=f"Temperatura em Celsius: {resultado:.2f}")
    except ValueError:
        label_resultado.config(text="Erro: Introduz um número válido.")


app = tk.Tk()
app.title("Conversor Temperaturas")

opcao = tk.IntVar(value=1)

tk.Label(app, text="Escolha a opção e digite a temperatura:").pack(pady=5)
tk.Radiobutton(app, text="Celsius para Fahrenheit",
               variable=opcao, value=1).pack()
tk.Radiobutton(app, text="Fahrenheit para Celsius",
               variable=opcao, value=2).pack()

entrada_temp = tk.Entry(app)
entrada_temp.pack(pady=5)

tk.Button(app, text="Converter", command=converter_temperatura_gui).pack(pady=5)

label_resultado = tk.Label(app, text="", font=("Arial", 10, "bold"))
label_resultado.pack(pady=10)

app.mainloop()
