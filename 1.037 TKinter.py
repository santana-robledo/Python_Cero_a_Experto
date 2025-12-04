import tkinter as tk
#
# def mostrar_mensaje():
#     etiqueta.config(text="Botón presionado")
#
# def mostrar_texto():
#     texto=entrada.get()#Capturar el texto ingresado
#     etiqueta.config(text=f"Texto ingresado: {texto}")
#
# #Crear una ventana
# ventana = tk.Tk()
# ventana.title("Ventana Básica")
#
# #Tamaño de la ventana
# ventana.geometry("300x200")
#
# #Crear etiqueta
# etiqueta=tk.Label(ventana, text="Etiqueta desde TKinter")
# etiqueta.pack()
#
# entrada = tk.Entry(ventana)
# entrada.pack()
#
# #Crear botón
# bboton=tk.Button(ventana, text="Presioname", command=mostrar_texto)
# bboton.pack()
#
# #Iniciar bucle de la aplicación
# ventana.mainloop()

ventana=tk.Tk()
ventana.title("Uso de frame y Grid")

frame=tk.Frame(ventana,borderwidth=2,relief="groove")
frame.pack(padx=100,pady=100,fill="both",expand=True)

#Crear widgets en el marco
etiqueta1=tk.Label(frame,text="Etiqueta 1")
etiqueta1.grid(row=0,column=0)

etiqueta2=tk.Label(frame,text="Etiqueta 2")
etiqueta2.grid(column=1,row=0)

boton1=tk.Button(frame,text="Boton1")
boton1.grid(column=0,row=1)

boton2=tk.Button(frame,text="Boton2")
boton2.grid(column=1,row=1)


ventana.mainloop()

