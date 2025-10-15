##Calcular el porcentaje de propina

def calcular_propina(total_cuenta, porcentaje_propina):
    propina= total_cuenta*porcentaje_propina/100
    total_a_pagar=total_cuenta+propina
    return propina,total_a_pagar

total_cuenta=100
porcentaje=15
propina,total_a_pagar= calcular_propina(total_cuenta,porcentaje)
print(f"La propina es: ${propina}, total a pagar: {total_a_pagar}")