import tkinter as tk


def processar_entrada():
    entrada = entrada_texto.get().strip()

    if not entrada:
        label_resultado.config(text="Erro: Por favor, insira números.")
        return

    try:
        lista_numeros = [int(numero) for numero in entrada.split(",")]
    except ValueError:
        label_resultado.config(
            text="Erro: Apenas números inteiros e vírgulas.")
        return

    res_str = f"Lista: {lista_numeros}\n"
    res_str += f"Tipo: {type(lista_numeros)}\n"

    if lista_numeros:
        res_str += f"Primeiro valor: {lista_numeros[0]}\n"
        res_str += f"Último valor: {lista_numeros[-1]}"

    label_resultado.config(text=res_str)


# GUI setup
root = tk.Tk()
root.title("Lista de Números")
root.geometry("400x250")
root.configure(bg="#f0f0f0")

tk.Label(root, text="Introduza números inteiros separados por vírgulas:",
         bg="#f0f0f0").pack(pady=10)
entrada_texto = tk.Entry(root)
entrada_texto.pack(pady=5)

tk.Button(root, text="Processar", command=processar_entrada).pack(pady=15)

label_resultado = tk.Label(root, text="", bg="#f0f0f0", justify=tk.LEFT)
label_resultado.pack()

root.mainloop()
