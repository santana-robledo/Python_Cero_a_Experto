import csv
from collections import defaultdict

def analizar_ventas(archivo_csv):
    ventas_por_producto = defaultdict(float)
    ingresos_por_dia = defaultdict(float)

    with open(archivo_csv, mode="r") as archivo:
        lector_csv = csv.DictReader(archivo)
        for fila in lector_csv:
            try:
                producto = fila["Producto"].strip()
                fecha = fila["Fecha"].strip()
                cantidad = int(fila["Cantidad"].strip())
                precio = float(fila["Precio"].strip())

                total_venta = cantidad * precio
                ventas_por_producto[producto] += total_venta
                ingresos_por_dia[fecha] += total_venta
            except Exception as e:
                print(f"Error procesando fila: {fila}")
                print(f"Detalles: {e}")

    print("\n🛒 Total de ventas por producto:")
    for producto, total in ventas_por_producto.items():
        print(f"{producto}: ${total:.2f}")

    print("\n📅 Ingresos totales por día:")
    for fecha, total in sorted(ingresos_por_dia.items()):
        print(f"{fecha}: ${total:.2f}")

archivo_csv = "ventas.csv"
analizar_ventas(archivo_csv)
