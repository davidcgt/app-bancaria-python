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
    def transferir(self, monto, cuenta_destino):
        if self.retirar(monto):
            cuenta_destino.consignar(monto)
            cuenta_destino.historial_transacciones.append(f"Transferencia recibida: +{monto} desde cuenta {self.numero_cuenta}")
            self.historial_transacciones.append(f"Transferencia enviada: -{monto} a cuenta {cuenta_destino.numero_cuenta}")
            return True
        return False
        