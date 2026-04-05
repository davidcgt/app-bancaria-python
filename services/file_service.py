import json
from models.usuario import Usuario
from models.cuenta import Cuenta


def usuario_a_dict(usuario):
    return {
        "nombre" : usuario.nombre,
        "apellido" : usuario.apellido,
        "cedula" : usuario.cedula,
        "username" : usuario.usuario,
        "contraseña" : usuario.contraseña,
        "cuentas_bancarias": [cuenta.__dict__ for cuenta in usuario.cuentas_bancarias]
        
    }


def dict_a_usuario(datos):
    
    objeto_creado = Usuario(datos["nombre"], datos["apellido"],datos["cedula"],datos["username"],datos["contraseña"])
    for cuentas in datos["cuentas_bancarias"]:
        cuenta_creada = Cuenta(cuentas["tipo_cuenta"], cuentas["numero_cuenta"], cuentas["saldo"], cuentas["historial_transacciones"])
        objeto_creado.agregar_cuenta(cuenta_creada)
    return objeto_creado
    

def guardar_datos(usuarios_aplicacion):
    with open("usuarios.json","w") as archivo_usuarios:
        datos = {username: usuario_a_dict(usuario) for username, usuario in usuarios_aplicacion.items()}
        json.dump(datos, archivo_usuarios)


def cargar_datos():
    try:
        with open("usuarios.json", "r") as archivo_usuarios:
            datos = json.load(archivo_usuarios)
            objeto_cargado = {username: dict_a_usuario(datos) for username, datos in datos.items()}
            return objeto_cargado
    except (FileNotFoundError, json.JSONDecodeError):
        return {}