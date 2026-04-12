import sqlite3
from models.usuario import Usuario
from models.cuenta import Cuenta


def inicializar_db():
    conexion = sqlite3.connect("data/base_usuarios.db")
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nombre TEXT,
                   apellido TEXT,
                   cedula INTEGER,
                   username TEXT,
                   contraseña TEXT
                   )
    """)
    conexion.commit()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cuentas(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   tipo_cuenta TEXT,
                   numero_cuenta INTEGER,
                   saldo INTEGER,
                   usuario_id INTEGER, 
                   FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
                   )
    """)
    conexion.commit()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS historial_transacciones(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   descripcion TEXT,
                   cuenta_id INTEGER,
                   FOREIGN KEY (cuenta_id) REFERENCES cuentas(id)
                   )
    """)
    conexion.commit()
    conexion.close()

def registrar_usuario_db(usuario):
    conexion = sqlite3.connect("data/base_usuarios.db")
    cursor = conexion.cursor()

    cursor.execute("""
    INSERT INTO usuarios (nombre, apellido, cedula, username, contraseña)
    VALUES (?, ?, ?, ?, ?)
    """, (usuario.nombre, usuario. apellido, 
          usuario.cedula, usuario.usuario, usuario.contraseña))

    conexion.commit()
    conexion.close()

def cargar_usuarios_db():
    conexion = sqlite3.connect("data/base_usuarios.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM usuarios")
    resultado = cursor.fetchall()
    usuarios = {}
    
    for resultado in resultado:
        usuario_cargado=Usuario(resultado[1],resultado[2],resultado[3],resultado[4],resultado[5])
        cursor.execute("SELECT * FROM cuentas WHERE usuario_id = ?", (resultado[0],))
        cuentas = cursor.fetchall()
        for cuenta in cuentas:
            cuenta_cargada =Cuenta(cuenta[1],cuenta[2],cuenta[3])
            cursor.execute("SELECT descripcion FROM historial_transacciones WHERE cuenta_id = ?", (cuenta[0],))
            historial = cursor.fetchall()
            for movimiento in historial:
                cuenta_cargada.historial_transacciones.append(movimiento[0])
            
            usuario_cargado.agregar_cuenta(cuenta_cargada)
        usuarios[resultado[4]] = usuario_cargado
    conexion.close()
    return usuarios
    
def guardar_cuenta_db(cuenta,usuario):
    conexion = sqlite3.connect("data/base_usuarios.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT id FROM usuarios WHERE username = ?", (usuario.usuario,))
    resultado = cursor.fetchone()
    usuario_id = resultado[0]

    cursor.execute("""
    INSERT INTO cuentas (tipo_cuenta, numero_cuenta, saldo, usuario_id)
    VALUES (?, ?, ?, ?)
    """, (cuenta.tipo_cuenta, cuenta.numero_cuenta, cuenta.saldo, usuario_id))

    conexion.commit()

def actualizar_saldo_db(cuenta):
    conexion = sqlite3.connect("data/base_usuarios.db")
    cursor = conexion.cursor()

    cursor.execute("""
        
        UPDATE cuentas SET saldo = ? WHERE numero_cuenta = ?
    """, (cuenta.saldo , cuenta.numero_cuenta))
    conexion.commit()


    conexion.close()

def actualizar_historial(descripcion, cuenta):
    conexion = sqlite3.connect("data/base_usuarios.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT id FROM cuentas WHERE numero_cuenta = ?", (cuenta.numero_cuenta,))
    resultado = cursor.fetchone()

    cursor.execute("""
    INSERT INTO historial_transacciones (descripcion, cuenta_id)
    VALUES (?, ?)
    """, (descripcion, resultado[0]))

    conexion.commit()
    conexion.close()