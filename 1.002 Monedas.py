
def calcular_cambio(costo, pagado):
    cambio=pagado - costo
    billetes_y_monedas=[100,50,20,10,5,1,0.5,0.25,0.1,0.05,0.01]
    desglose={}

    for valor in billetes_y_monedas:
        cantidad=int(cambio//valor)
        cambio=round(cambio%valor,2)
        if cantidad > 0:
            desglose[valor]=cantidad
    return desglose

costo=23.75
pagado=50
print(calcular_cambio(costo,pagado))