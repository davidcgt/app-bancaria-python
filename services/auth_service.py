from models.usuario import Usuario
from services.database import registrar_usuario_db
from helpers.helpers import encriptar_contraseña

def registrar_usuario(usuarios_aplicacion, nombre, apellido, cedula, username, contraseña):
    if username in usuarios_aplicacion:
        return {"success": False, "mensaje": "El nombre de usuario ya existe. Por favor, elija otro."}
    elif cedula in [usuario.cedula for usuario in usuarios_aplicacion.values()]:
        return {"success": False, "mensaje": "La cédula ya está registrada. Por favor, verifique su información."}
    else:
        nuevo_usuario = Usuario(nombre, apellido, cedula, username, encriptar_contraseña(contraseña))
        usuarios_aplicacion[username] = nuevo_usuario
        registrar_usuario_db(nuevo_usuario)
        return {"success": True, "mensaje": "Usuario registrado exitosamente."}
    
def iniciar_sesion(usuarios_aplicacion, username, contraseña):
    
    usuario_encontrado = usuarios_aplicacion.get(username)
    if usuario_encontrado and usuario_encontrado.contraseña == encriptar_contraseña(contraseña):
        return usuario_encontrado
    return None