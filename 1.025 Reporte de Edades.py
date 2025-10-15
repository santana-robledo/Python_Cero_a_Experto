""""
Crear un archivo en formato CSV, con datos provenientes de una lista
Sumar los datos numericos y colocarlos en la ultima fila
"""

import csv
import gc

gc.collect() ##garbage collector
nombre_archivo="datos.csv"
datos=[
["Nombre","Edad"],
["Juan",25],
["Maria",19],
["Pedro",45],
["Armando",43],
]

#Sumar la columna Edad
total_edades= sum(row[1] for row in datos[1:])
print(total_edades)

fila_total= len(datos)-1
promedio_edades=total_edades/fila_total

datos.append(["Total",total_edades])
datos.append(["Promedio Edades",promedio_edades])

print(datos)


##Escribir datos en el archivo
with open(nombre_archivo,"w",newline="")as file:
    writer=csv.writer(file)
    writer.writerows(datos)

##Mostrar los datos

with open(nombre_archivo,"r")as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)

