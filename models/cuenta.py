"""
esta parte se encarga de almacenar la informacion de las cuentas bancarias
cada cuenta debe tener
tipo de cuenta
numero de cuenta
saldo
historial de transacciones
"""


class Cuenta:
    def __init__(self, tipo_cuenta, numero_cuenta, saldo=0):
        self.tipo_cuenta = tipo_cuenta
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
        self.historial_transacciones = []

    def consignar(self, monto):
        self.saldo += monto
        self.historial_transacciones.append(f"Consignación: +{monto}")

    def retirar(self, monto):
        if monto > self.saldo:
            print("Saldo insuficiente para realizar el retiro.")
            return False
        self.saldo -= monto
        self.historial_transacciones.append(f"Retiro: -{monto}")
        return True
