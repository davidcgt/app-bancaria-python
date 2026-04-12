
from models.cuenta import Cuenta
import random
from services.database import guardar_cuenta_db,actualizar_saldo_db, actualizar_historial

def creacion_cuentas(usuario_encontrado, usuarios_aplicacion):
    
        print("\n--- CREAR CUENTA ---")
        print("1. Ahorros")
        print("2. Corriente")
        tipo_cuenta_crear = int(input("Seleccione el tipo de cuenta: "))
        if tipo_cuenta_crear == 1:
            tipo_cuenta = "Ahorros"

        elif tipo_cuenta_crear == 2:
            tipo_cuenta = "Corriente"
        else:
            print("\nOpción no válida. Volviendo al menú principal.")
            return
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
        guardar_cuenta_db(nueva_cuenta,usuario_encontrado)
        print(
                f"\nCuenta {tipo_cuenta} creada exitosamente con número: {numero_cuenta_random}."
            )
        
def consulta_cuentas(usuario_encontrado):
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

def realizar_transaccion(usuario_encontrado, usuarios_aplicacion):
    print("\n--- HACER TRANSACCIONES ---")
    if not usuario_encontrado.cuentas_bancarias:
        print("\nNo tienes cuentas bancarias registradas.")
        return
    else:
        print("\nTus cuentas bancarias:")
        for i, cuenta in enumerate(
            usuario_encontrado.cuentas_bancarias, start=1):
            print(
                f"{i}. Tipo: {cuenta.tipo_cuenta}, Número: {cuenta.numero_cuenta}, Saldo: {cuenta.saldo}"
        )
        try:
            cuenta_seleccionada = int(
                input("Seleccione la cuenta para realizar la transacción: ")
            )
        except ValueError:
            print("\nOpción no válida. Volviendo al menú principal.")
            return
        if cuenta_seleccionada < 1 or cuenta_seleccionada > len(
            usuario_encontrado.cuentas_bancarias
        ):
            print("\nOpción no válida. Volviendo al menú principal.")
            return
        cuenta_elegida = usuario_encontrado.cuentas_bancarias[
            cuenta_seleccionada - 1]
        
    print("\n1. Consignar")
    print("2. Retirar")
    print("3. Transferir a otra cuenta")
    try:
        tipo_transaccion = int(
            input("Seleccione el tipo de transacción: ")
        )
    except ValueError:
        print("\nOpción no válida. Volviendo al menú principal.")
        return

    if tipo_transaccion not in [1, 2, 3]:
        print("\nOpción no válida. Volviendo al menú principal.")
        return
    try:
        monto = float(input("Ingrese el monto de la transacción: "))
    except ValueError:
        print("\nOpción no válida. Volviendo al menú principal.")
        return

    if monto <= 0:
        print(
            "\nEl monto debe ser mayor a cero. Volviendo al menú principal."
        )
        return
    if tipo_transaccion == 1:
        cuenta_elegida.consignar(monto)
        
        actualizar_saldo_db(cuenta_elegida)
        print(f"\nConsignación de {monto} realizada exitosamente.")
        actualizar_historial(cuenta_elegida.historial_transacciones[-1],cuenta_elegida)
    elif tipo_transaccion == 2:
        if cuenta_elegida.retirar(monto):
            
            actualizar_saldo_db(cuenta_elegida)
            print(f"\nRetiro de {monto} realizado exitosamente.")
            actualizar_historial(cuenta_elegida.historial_transacciones[-1],cuenta_elegida)
    elif tipo_transaccion == 3:
        try:
            numero_cuenta_destino = int(
                input("Ingrese el número de cuenta destino: ")
            )
        except ValueError:
            print("\nOpción no válida. Volviendo al menú principal.")
            return
        cuenta_destino = None
        for usuario in usuarios_aplicacion.values():
            for cuenta in usuario.cuentas_bancarias:
                if cuenta.numero_cuenta == numero_cuenta_destino:
                    cuenta_destino = cuenta
                    break
            if cuenta_destino:
                break
        if not cuenta_destino:
            print("\nCuenta destino no encontrada. Volviendo al menú principal.")
            return
        if cuenta_elegida.transferir(monto, cuenta_destino):
            actualizar_saldo_db(cuenta_elegida)
            actualizar_saldo_db(cuenta_destino)
            print(
                f"\nTransferencia de {monto} a la cuenta {numero_cuenta_destino} realizada exitosamente."
            )
            actualizar_historial(cuenta_elegida.historial_transacciones[-1],cuenta_elegida)
            actualizar_historial(cuenta_destino.historial_transacciones[-1],cuenta_destino)

        

def mostrar_historial_transacciones(usuario_encontrado):
    print("\n--- HISTORIAL DE TRANSACCIONES ---")
    for i, cuenta in enumerate(
        usuario_encontrado.cuentas_bancarias, start=1
    ):
        print(
            f"Cuenta {i} - Tipo: {cuenta.tipo_cuenta}, Número: {cuenta.numero_cuenta}"
        )
    cuenta_consultada = int(
        input("\nSeleccione la cuenta para ver el historial de transacciones: ")
    )
    if cuenta_consultada < 1 or cuenta_consultada > len(
        usuario_encontrado.cuentas_bancarias
    ):
        print("\nOpción no válida. Volviendo al menú principal.")
        return
    cuenta_consultada = usuario_encontrado.cuentas_bancarias[
        cuenta_consultada - 1 ]
    if not cuenta_consultada.historial_transacciones:
        print("\nNo hay transacciones registradas para esta cuenta.")
    else:
        print("\nHistorial de transacciones:")
        for movimiento in cuenta_consultada.historial_transacciones:
            print(movimiento)

