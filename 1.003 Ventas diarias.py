
def calcular_ventas(ventas):
    total_ventas=0
    total_articulos=0
    for venta in ventas:
        total_ventas += venta["precio"] * venta["cantidad"]
        total_articulos+= venta["cantidad"]
    return total_ventas,total_articulos

ventas= [{"precio":10, "cantidad":2},
{"precio":5, "cantidad":4},{"precio":20, "cantidad":1},]

print(calcular_ventas(ventas))