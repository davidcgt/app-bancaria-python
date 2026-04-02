from models.cuenta import Cuenta
from models.usuario import Usuario
from services.auth_service import registrar_usuario
from services.auth_service import iniciar_sesion
from services.menus import menu_login
from services.menus import menu_usuario_validado
from services.bank_service import creacion_cuentas, consulta_cuentas,realizar_transaccion, mostrar_historial_transacciones

# PROYECTO DE APP BANCARIA

# LISTA DE USUARIOS

usuarios_aplicacion = {
    "admin": Usuario("David", "Cardona", "123456789", "admin", "1234")
}

usuarios_aplicacion["admin"].agregar_cuenta(Cuenta("Ahorros", 1234567890, 850000))

usuarios_aplicacion["admin"].agregar_cuenta(Cuenta("Corriente", 9876543210, 2300000))


# MENU DE OPCIONES

while True:
    opcion_menu_login = menu_login()

    # CREACION DE USUARIOS
    if opcion_menu_login == 3:
        print("\nSaliendo de la aplicación...")
        break

    if opcion_menu_login == 1:
        nombre = input("\nIngrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        cedula = input("Ingrese su cédula: ")
        username = input("Ingrese su nombre de usuario: ")
        contraseña = input("Ingrese su contraseña: ")

        resultado_registro = registrar_usuario(
            usuarios_aplicacion, nombre, apellido, cedula, username, contraseña
        ) 
        if resultado_registro["success"]:
            print("\nUsuario registrado exitosamente.")
        else:
            print(f"\nError al registrar usuario: {resultado_registro['mensaje']}")

    # inicio de sesion
    elif opcion_menu_login == 2:
        username = input("\nIngrese su nombre de usuario: ")
        contraseña = input("Ingrese su contraseña: ")
        
        usuario_encontrado = iniciar_sesion(usuarios_aplicacion, username, contraseña)

        if usuario_encontrado:
            print(f"\nBienvenido, {usuario_encontrado.nombre}!")
            # Aquí se puede agregar el menú de opciones para el usuario autenticado

            while True:
                
                opcion_usuario_validado = menu_usuario_validado(usuario_encontrado)

                if opcion_usuario_validado == 5:
                    print("\nCerrando sesión...")
                    break
                # CREACION DE CUENTAS
                elif opcion_usuario_validado == 1:

                    creacion_cuentas(usuario_encontrado, usuarios_aplicacion)


                # IMPRESION CUENTAS DE USUARIOS
                elif opcion_usuario_validado == 2:
                    consulta_cuentas(usuario_encontrado)

                elif opcion_usuario_validado == 3:
                    
                        cuenta_elegida = realizar_transaccion(usuario_encontrado)
                        
                elif opcion_usuario_validado == 4:
                    mostrar_historial_transacciones(usuario_encontrado)
                else:
                    print(
                        "\nOpción no válida. Por favor, seleccione una opción del menú."
                    )

        else:
            print("\nNombre de usuario o contraseña incorrectos.")

    else:
        print("\nOpción no válida. Por favor, seleccione una opción del menú.")
