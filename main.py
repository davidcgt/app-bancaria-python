import random

from models.cuenta import Cuenta
from models.usuario import Usuario

# PROYECTO DE APP BANCARIA

# LISTA DE USUARIOS

usuarios_aplicacion = {
    "admin": Usuario("David", "Cardona", "123456789", "admin", "1234")
}

usuarios_aplicacion["admin"].agregar_cuenta(Cuenta("Ahorros", 1234567890, 850000))

usuarios_aplicacion["admin"].agregar_cuenta(Cuenta("Corriente", 9876543210, 2300000))


# MENU DE OPCIONES

while True:
    print("\n--- APP BANCARIA ---")
    print("1. Registrar nuevo usuario")
    print("2. iniciar sesión")
    print("3. Salir")

    opcion_menu_login = int(input("Seleccione una opción: "))

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

        if username in usuarios_aplicacion:
            print("\nEl nombre de usuario ya existe. Por favor, elija otro.")

        elif cedula in [usuario.cedula for usuario in usuarios_aplicacion.values()]:
            print(
                "\nLa cédula ya está registrada. Por favor, verifique su información."
            )

        else:
            nuevo_usuario = Usuario(nombre, apellido, cedula, username, contraseña)
            usuarios_aplicacion[username] = nuevo_usuario
            print("\nUsuario registrado exitosamente.")

    # inicio de sesion
    elif opcion_menu_login == 2:
        username = input("\nIngrese su nombre de usuario: ")
        contraseña = input("Ingrese su contraseña: ")
        usuario_encontrado = usuarios_aplicacion.get(username)
        if usuario_encontrado and usuario_encontrado.contraseña == contraseña:
            print(f"\nBienvenido, {usuario_encontrado.nombre}!")
            # Aquí se puede agregar el menú de opciones para el usuario autenticado

            while True:
                print(
                    f"\n--- QUE QUIERES HACER EL DIA DE HOY {usuario_encontrado.nombre} ---"
                )
                print("\n1. Crear Cuentas")
                print("2. Consultar Cuentas")
                print("3. Hacer Transacciones")
                print("4. Historial de Transacciones")
                print("5. Cerrar Sesión")

                opcion_usuario_validado = int(input("Seleccione una opción: "))

                if opcion_usuario_validado == 5:
                    print("\nCerrando sesión...")
                    break
                # CREACION DE CUENTAS
                elif opcion_usuario_validado == 1:
                    print("\n--- CREAR CUENTA ---")
                    print("\n1. Ahorros")
                    print("2. Corriente")
                    tipo_cuenta_crear = int(input("Seleccione el tipo de cuenta: "))

                    if tipo_cuenta_crear == 1:
                        tipo_cuenta = "Ahorros"

                    elif tipo_cuenta_crear == 2:
                        tipo_cuenta = "Corriente"
                    else:
                        print("\nOpción no válida. Volviendo al menú principal.")
                        continue

                    while True:
                        numero_cuenta_random = random.randint(1000000000, 9999999999)
                        if not any(
                            cuenta.numero_cuenta == numero_cuenta_random
                            for usuario in usuarios_aplicacion.values()
                            for cuenta in usuario.cuentas_bancarias
                        ):
                            break
                    nueva_cuenta = Cuenta(tipo_cuenta, numero_cuenta_random)
                    usuario_encontrado.agregar_cuenta(nueva_cuenta)
                    print(
                        f"\nCuenta {tipo_cuenta} creada exitosamente con número: {numero_cuenta_random}."
                    )
                # IMPRESION CUENTAS DE USUARIOS
                elif opcion_usuario_validado == 2:
                    print("\n--- CONSULTAR CUENTAS ---")
                    if not usuario_encontrado.cuentas_bancarias:
                        print("\nNo tienes cuentas bancarias registradas.")
                    else:
                        print("\nTus cuentas bancarias:")
                        for i, cuenta in enumerate(
                            usuario_encontrado.cuentas_bancarias, start=1
                        ):
                            print(
                                f"{i}. Tipo: {cuenta.tipo_cuenta}, Número: {cuenta.numero_cuenta}, Saldo: {cuenta.saldo}"
                            )
                elif opcion_usuario_validado == 3:
                    print("\n--- HACER TRANSACCIONES ---")
                    if not usuario_encontrado.cuentas_bancarias:
                        print("\nNo tienes cuentas bancarias registradas.")
                    else:
                        print("\nTus cuentas bancarias:")
                        for i, cuenta in enumerate(
                            usuario_encontrado.cuentas_bancarias, start=1
                        ):
                            print(
                                f"{i}. Tipo: {cuenta.tipo_cuenta}, Número: {cuenta.numero_cuenta}, Saldo: {cuenta.saldo}"
                            )
                        cuenta_seleccionada = int(
                            input("Seleccione la cuenta para realizar la transacción: ")
                        )
                        if cuenta_seleccionada < 1 or cuenta_seleccionada > len(
                            usuario_encontrado.cuentas_bancarias
                        ):
                            print("\nOpción no válida. Volviendo al menú principal.")
                            continue
                        cuenta_elegida = usuario_encontrado.cuentas_bancarias[
                            cuenta_seleccionada - 1
                        ]
                        print("\n1. Consignar")
                        print("2. Retirar")
                        tipo_transaccion = int(
                            input("Seleccione el tipo de transacción: ")
                        )

                        if tipo_transaccion not in [1, 2]:
                            print("\nOpción no válida. Volviendo al menú principal.")
                            continue
                        monto = float(input("Ingrese el monto de la transacción: "))

                        if monto <= 0:
                            print(
                                "\nEl monto debe ser mayor a cero. Volviendo al menú principal."
                            )
                            continue
                        if tipo_transaccion == 1:
                            cuenta_elegida.consignar(monto)
                            print(f"\nConsignación de {monto} realizada exitosamente.")
                        elif tipo_transaccion == 2:
                            if cuenta_elegida.retirar(monto):
                                print(f"\nRetiro de {monto} realizado exitosamente.")
                elif opcion_usuario_validado == 4:
                    print("\n--- HISTORIAL DE TRANSACCIONES ---")
                    for i, cuenta in enumerate(
                        usuario_encontrado.cuentas_bancarias, start=1
                    ):
                        print(
                            f"Cuenta {i} - Tipo: {cuenta.tipo_cuenta}, Número: {cuenta.numero_cuenta}"
                        )
                    cuenta_consultada = int(
                        input(
                            "\nSeleccione la cuenta para ver el historial de transacciones: "
                        )
                    )
                    if cuenta_consultada < 1 or cuenta_consultada > len(
                        usuario_encontrado.cuentas_bancarias
                    ):
                        print("\nOpción no válida. Volviendo al menú principal.")
                        continue
                    cuenta_consultada = usuario_encontrado.cuentas_bancarias[
                        cuenta_consultada - 1
                    ]
                    if not cuenta_consultada.historial_transacciones:
                        print("\nNo hay transacciones registradas para esta cuenta.")
                    else:
                        print("\nHistorial de transacciones:")
                        for movimiento in cuenta_consultada.historial_transacciones:
                            print(movimiento)
                else:
                    print(
                        "\nOpción no válida. Por favor, seleccione una opción del menú."
                    )

        else:
            print("\nNombre de usuario o contraseña incorrectos.")

    else:
        print("\nOpción no válida. Por favor, seleccione una opción del menú.")
