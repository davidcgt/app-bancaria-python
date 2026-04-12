import hashlib


def encriptar_contraseña(contraseña):
    hash = hashlib.sha256(contraseña.encode()).hexdigest()
    return hash