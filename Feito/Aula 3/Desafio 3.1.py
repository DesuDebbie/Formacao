import tkinter as tk
from tkinter import messagebox


def factorial_recursivo(n):
    return 1 if n <= 1 else n * factorial_recursivo(n - 1)


def executar_factorial():
    try:
        num = int(entrada_num.get())
        if num >= 0:
            res = factorial_recursivo(num)
            messagebox.showinfo("Sucesso", f"Fatorial: {res}")
            lbl_res.config(text=f"Fatorial de {num} = {res}")
        else:
            messagebox.showerror("Erro", "Número deve ser >= 0")
    except:
        messagebox.showerror("Erro", "Entrada inválida")


app = tk.Tk()
app.title("Fatorial")
app.geometry("300x200")
app.config(bg="#e1f5fe")

tk.Label(app, text="Fatorial", font=("Arial", 12), bg="#e1f5fe").pack(pady=10)
entrada_num = tk.Entry(app)
entrada_num.pack()
tk.Button(app, text="Calcular", command=executar_factorial).pack(pady=10)
lbl_res = tk.Label(app, text="", bg="#e1f5fe")
lbl_res.pack()

app.mainloop()
