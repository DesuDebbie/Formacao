import tkinter as tk


def verificar():
    try:
        num = int(entrada.get())

        if num % 2 == 0:
            resultado_label.config(text=f"{num} é um número PAR.", fg="blue")
        else:
            resultado_label.config(text=f"{num} é um número ÍMPAR.", fg="red")

    except ValueError:
        resultado_label.config(text="Ei! Escreve um número, por favor.")

janela = tk.Tk()
janela.title("O Jogo do Par ou Ímpar") 
janela.geometry("300x200") 

tk.Label(janela, text="Escreve aqui um número:").pack(pady=10)

entrada = tk.Entry(janela)
entrada.pack(pady=5)

btn_verificar = tk.Button(janela, text="Verificar agora!", command=verificar)
btn_verificar.pack(pady=10)

resultado_label = tk.Label(janela, text="")
resultado_label.pack(pady=10)

janela.mainloop()