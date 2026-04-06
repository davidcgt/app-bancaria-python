from models.cuenta import Cuenta
from models.usuario import Usuario
from services.auth_service import registrar_usuario
from services.auth_service import iniciar_sesion
from services.menus import menu_login
from services.menus import menu_usuario_validado
from services.bank_service import creacion_cuentas, consulta_cuentas,realizar_transaccion, mostrar_historial_transacciones
from services.database import inicializar_db,cargar_usuarios_db


# PROYECTO DE APP BANCARIA

# LISTA DE USUARIOS

inicializar_db()


usuarios_aplicacion = cargar_usuarios_db()


def manejar_login(usuarios_aplicacion):
    opcion_menu_login = menu_login()

    if opcion_menu_login == 3:
        print("\nSaliendo de la aplicación...")
        return False

    if opcion_menu_login == 1:
        nombre = input("\nIngrese su nombre: ")
        if len(nombre) < 3:
            print("\nEl nombre debe tener al menos 3 caracteres. Por favor, intente nuevamente.")
            return True
        apellido = input("Ingrese su apellido: ")
        cedula = input("Ingrese su cédula: ")
        if not cedula.isdigit():
            print("\nLa cédula debe contener solo números. Por favor, intente nuevamente.")
            return True
        elif len(cedula) < 7:
            print("\nLa cédula debe tener al menos 7 dígitos. Por favor, intente nuevamente.")
            return True
        username = input("Ingrese su nombre de usuario: ")
        if " " in username:
            print("\nEl nombre de usuario no puede contener espacios. Por favor, intente nuevamente.")
            return True  
        elif len(username) < 6:
            print("\nEl nombre de usuario debe tener al menos 6 caracteres. Por favor, intente nuevamente.")
            return True
        contraseña = input("Ingrese su contraseña: ")
        if not nombre or not apellido or not cedula or not username or not contraseña:
            print("\nTodos los campos son obligatorios. Por favor, intente nuevamente.")
            return True
        elif len(contraseña) < 4:
            print("\nLa contraseña debe tener al menos 4 caracteres. Por favor, intente nuevamente.")
            return True
        elif " " in contraseña:
            print("\nLa contraseña no puede contener espacios. Por favor, intente nuevamente.")
            return True
            

        resultado_registro = registrar_usuario(
            usuarios_aplicacion, nombre, apellido, cedula, username, contraseña
        )

        if resultado_registro["success"]:
            print("\nUsuario registrado exitosamente.")
           
        else:
            print(f"\nError al registrar usuario: {resultado_registro['mensaje']}")

    elif opcion_menu_login == 2:
        username = input("\nIngrese su nombre de usuario: ")
        contraseña = input("Ingrese su contraseña: ")

        usuario_encontrado = iniciar_sesion(
            usuarios_aplicacion, username, contraseña
        )

        if usuario_encontrado:
            print(f"\nBienvenido, {usuario_encontrado.nombre}!")
            manejar_menu_usuario(usuario_encontrado, usuarios_aplicacion)
        else:
            print("\nNombre de usuario o contraseña incorrectos.")

    else:
        print("\nOpción no válida.")

    return True

def manejar_menu_usuario(usuario_encontrado, usuarios_aplicacion):
    while True:
        opcion_menu_usuario = menu_usuario_validado(usuario_encontrado)

        if opcion_menu_usuario == 5:
            print("\nCerrando sesión...")
            break

        elif opcion_menu_usuario == 1:
            creacion_cuentas(usuario_encontrado, usuarios_aplicacion)

        elif opcion_menu_usuario == 2:
            consulta_cuentas(usuario_encontrado)

        elif opcion_menu_usuario == 3:
            realizar_transaccion(usuario_encontrado, usuarios_aplicacion)

        elif opcion_menu_usuario == 4:
            mostrar_historial_transacciones(usuario_encontrado)

        else:
            print("\nOpción no válida.")


while manejar_login(usuarios_aplicacion):
    pass