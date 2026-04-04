import json


def usuario_a_dict(usuario):
    return {
        "nombre" : usuario.nombre,
        "apellido" : usuario.apellido,
        "cedula" : usuario.cedula,
        "username" : usuario.usuario,
        "contraseña" : usuario.contraseña,
        "cuentas_bancarias": [cuenta.__dict__ for cuenta in usuario.cuentas_bancarias]
        
    }
   


def guardar_datos(usuarios_aplicacion):
    with open("usuarios.json","w") as archivo_usuarios:
        datos = {username: usuario_a_dict(usuario) for username, usuario in usuarios_aplicacion.items()}
        json.dump(datos, archivo_usuarios)

def cargar_datos():
    with open("usuarios.json", "r") as archivo_usuarios:
        datos = json.load(archivo_usuarios)
        return datos