import tkinter as tk
from tkinter import messagebox

def agregar_tarea(entrada,lista):
    tarea = entrada.get()
    if tarea:
        lista.insert(tk.END,tarea)
        entrada.delete(0,tk.END)

def eliminar_tarea(lista):
    tarea_seleccionada=lista.curselection()
    if tarea_seleccionada:
        lista.delete(tarea_seleccionada)

def salir(ventana):
    if messagebox.askokcancel("Salir","Estas seguro?"):
        ventana.destroy()



def principal():
    ventana=tk.Tk()
    ventana.title("Lista Tareas")

    marco_lista=tk.Frame(ventana)
    marco_lista.pack(pady=10)

    lista_tareas=tk.Listbox(marco_lista,width=50,height=10)
    lista_tareas.pack(side=tk.LEFT,fill=tk.BOTH)

    scrollbar=tk.Scrollbar(marco_lista,orient=tk.VERTICAL)
    scrollbar.config(command=lista_tareas.yview)
    scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
    lista_tareas.config(yscrollcommand=scrollbar.set)

    marco_entrada=tk.Frame(ventana)
    marco_entrada.pack(pady=5)

    etiqueta_tarea=tk.Label(marco_entrada,text="Nueva Tarea")
    etiqueta_tarea.pack(side=tk.LEFT)
    entrada_tarea = tk.Entry(marco_entrada,width=40)
    entrada_tarea.pack(side=tk.LEFT)

    boton_agregar=tk.Button(marco_entrada,text="Agregar",command=lambda:agregar_tarea(entrada_tarea,lista_tareas))
    boton_agregar.pack(pady=5)

    boton_eliminar=tk.Button(marco_entrada,text="Eliminar",command=lambda:eliminar_tarea(lista_tareas))
    boton_eliminar.pack(pady=5)

    boton_salir=tk.Button(marco_entrada,text="Salir",command=lambda:salir(ventana))
    boton_salir.pack(pady=5)

    ventana.mainloop()

if __name__ == '__main__':
    principal()


