"""un cliente bancario debe tener datos basicos
nombre
apellido
cedula
usuario
contraseña
saldo bancario
historial de movimientos
tipo de cuenta
numero de cuenta
"""


class Usuario:
    def __init__(self, nombre, apellido, cedula, usuario, contraseña):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.usuario = usuario
        self.contraseña = contraseña
        self.cuentas_bancarias = []

    def agregar_cuenta(self, cuenta):
        self.cuentas_bancarias.append(cuenta)
