import tkinter as tk
from tkinter import messagebox

notas = []


def adicionar_nota():
    try:
        nota = float(entrada_nota.get())

        if 0 <= nota <= 20:
            if len(notas) < 4:
                notas.append(nota)
                entrada_nota.delete(0, tk.END)
                lbl_lista.config(text=f"Notas: {', '.join(map(str, notas))}")

                if len(notas) == 4:
                    media = sum(notas) / 4
                    lbl_media.config(text=f"Média final: {media:.2f}")
            else:
                messagebox.showinfo("Aviso", "Já introduziste as 4 notas!")
        else:
            messagebox.showerror("Erro", "Nota inválida (0 a 20)")
    except ValueError:
        messagebox.showerror("Erro", "Introduz um número válido")


def limpar():
    global notas
    notas = []
    lbl_lista.config(text="Notas: ")
    lbl_media.config(text="Média final: 0.00")
    entrada_nota.delete(0, tk.END)


root = tk.Tk()
root.title("Cálculo de Média")
root.geometry("400x300")
root.configure(bg="#e9f5db")

tk.Label(root, text="Cálculo de Média (4 notas)",
         font=("Arial", 14), bg="#e9f5db").pack(pady=15)

entrada_nota = tk.Entry(root, font=("Arial", 12))
entrada_nota.pack(pady=5)

f_botoes = tk.Frame(root, bg="#e9f5db")
f_botoes.pack(pady=10)

tk.Button(f_botoes, text="Adicionar Nota", bg="#90be6d",
          command=adicionar_nota).pack(side=tk.LEFT, padx=5)
tk.Button(f_botoes, text="Limpar", bg="#f48c94", fg="white",
          command=limpar).pack(side=tk.LEFT, padx=5)

lbl_lista = tk.Label(root, text="Notas: ", bg="#ecf5e3")
lbl_lista.pack(pady=10)

lbl_media = tk.Label(root, text="Média final: 0.00", font=(
    "Arial", 12, "bold"), bg="#e1ebd6", fg="#a1be88")
lbl_media.pack(pady=5)

root.mainloop()
