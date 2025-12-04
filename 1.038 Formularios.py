import tkinter as tk
from tkinter import messagebox

class SumadorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Sumador")

        # Número 1
        self.label1 = tk.Label(master, text="Número 1")
        self.label1.grid(column=0, row=0)

        self.entry1 = tk.Entry(master)
        self.entry1.grid(column=1, row=0)

        # Número 2
        self.label2 = tk.Label(master, text="Número 2")
        self.label2.grid(column=0, row=1)

        self.entry2 = tk.Entry(master)
        self.entry2.grid(column=1, row=1)

        # Resultado
        self.label3 = tk.Label(master, text="Resultado:")
        self.label3.grid(column=0, row=2, columnspan=2)

        # Botón
        self.boton = tk.Button(master, text="Sumar", command=self.sumar)
        self.boton.grid(column=0, row=3, columnspan=2)

        self.salir = tk.Button(master, text="Salir", command=self.salir)
        self.salir.grid( row=4, columnspan=2)

    def sumar(self):
        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
            resultado = num1 + num2
            self.label3.config(text=f"Resultado: {resultado}")
        except ValueError:
            self.label3.config(text="Error: Ingresa números válidos")

    def salir(self):
        if messagebox.askokcancel("Salir", "Desea salir?"):
            self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SumadorApp(root)
    root.mainloop()
