from services.auth_service import registrar_usuario
from services.auth_service import iniciar_sesion

def menu_login():
   while True:
    print("\n--- APP BANCARIA ---")
    print("1. Registrar nuevo usuario")
    print("2. iniciar sesión")
    print("3. Salir")
    try:
        opcion_menu_login = int(input("Seleccione una opción: "))
        if opcion_menu_login in [1, 2, 3]:
            return opcion_menu_login
        else:            
           print("Opción no válida. Por favor, seleccione una opción válida.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")

def menu_usuario_validado(usuario_encontrado):
    print(
        f"\n--- QUE QUIERES HACER EL DIA DE HOY {usuario_encontrado.nombre} ---"
    )
    print("\n1. Crear Cuentas")
    print("2. Consultar Cuentas")
    print("3. Hacer Transacciones")
    print("4. Historial de Transacciones")
    print("5. Cerrar Sesión")

    opcion_usuario_validado = int(input("Seleccione una opción: "))
    return opcion_usuario_validado

