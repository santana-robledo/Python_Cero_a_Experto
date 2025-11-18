class Cuenta_Bancaria:
    def __init__(self,titular,saldo_inicial):
        self.tirular=titular
        self.__saldo=saldo_inicial
    def depositar(self,monto):
        if monto>0:
            self._saldo+=monto
            print(f"Deposito exitoso. Nuevo saldo: {self.__saldo:.2f} ")
        else:
            print("El monto debe ser mayor a 0")

    def retirar(self,monto):
        if 0<monto <=self.__saldo:
            self.__saldo-=monto
            print(f"Retiro exitoso. Nuevo saldo: {self.__saldo:.2f} ")
        else:
            print("Monto invalido o saldo insuficiente")
    def consultar_saldo(self):
        return print(f"Saldo actual {self.__saldo:.2f}")

cuenta=Cuenta_Bancaria("Armando",100)
cuenta.depositar(200)
print(cuenta.consultar_saldo())
cuenta.retirar(400)
print(cuenta.consultar_saldo())

