
inventario={
    "Manzana":{"cantidad":100,"precio":0.5},
    "Platano":{"cantidad":150,"precio":0.3},
"Naranjas":{"cantidad":80,"precio":0.4}
}

def lista_inventario(inventario):
    for nombre,detalles in inventario.items():
        print(f"Producto: {nombre}, Cantidad:{detalles["cantidad"]},Precios:{detalles["precio"]}")

def agregar_producto(inventario,nombre,cantidad,precio):
    if nombre in inventario:
        inventario[nombre]["cantidad"]=cantidad
    else:
        inventario[nombre]={"cantidad":cantidad,"precio":precio}

def eliminar_producto(inventario,nombre):
    if nombre in inventario:
        del inventario[nombre]
    else:
        return "El producto no existe"

def actualizar_producto(inventario,nombre,cantidad):
    if nombre in inventario:
        inventario[nombre]["cantidad"]=cantidad
    else:
        return "El producto no existe"

def consultar_producto(inventario,nombre):
    if nombre in inventario:
        detalles=inventario[nombre]
        print(f"Producto: {nombre}, Cantidad:{detalles["cantidad"]},Precios:{detalles["precio"]}")
    else:
        return "El producto no existe"
    
lista_inventario(inventario)
agregar_producto(inventario,"Peras",50,0.6)
eliminar_producto(inventario,"Naranjas")
actualizar_producto(inventario,"Manzanas",120)
consultar_producto(inventario,"Platano")
lista_inventario(inventario)