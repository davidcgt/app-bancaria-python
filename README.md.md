# 🏦 App Bancaria en Python

Aplicación bancaria desarrollada en **Python** usando **Programación Orientada a Objetos (POO)** y una **arquitectura modular por carpetas**, pensada como base para evolucionar hacia una **interfaz web con Flask**.

---

## 🚀 Funcionalidades actuales

- ✅ Registro de nuevos usuarios
- ✅ Inicio de sesión
- ✅ Validación de usuario único
- ✅ Validación de cédula única
- ✅ Creación de cuentas de **ahorros** y **corriente**
- ✅ Generación aleatoria de número de cuenta único
- ✅ Consulta de cuentas bancarias
- ✅ Consignaciones
- ✅ Retiros con validación de saldo
- ✅ Historial de transacciones por cuenta
- ✅ Estructura lista para persistencia en JSON

---

## 📂 Estructura del proyecto

```text
APP BANCARIA/
│
├── data/
│   └── usuarios.json
│
├── helpers/
│   └── helpers.py
│
├── models/
│   ├── cuenta.py
│   └── usuario.py
│
├── services/
│   ├── auth_service.py
│   ├── bank_service.py
│   └── file_service.py
│
├── main.py
└── .gitignore
```

---

## 🧠 Tecnologías usadas

- **Python 3**
- **POO (Clases y Objetos)**
- **Git**
- **GitHub**
- Próximamente: **Flask + HTML + CSS + Bootstrap**

---

## ▶️ Cómo ejecutar

Desde la terminal, dentro de la carpeta del proyecto:

```bash
python main.py
```

---

## 🔥 Próximas mejoras

- 💾 Guardado y carga automática desde JSON
- 🌐 Migración a interfaz web con Flask
- 🔐 Mejor manejo de autenticación
- 📊 Dashboard con resumen de cuentas
- 💸 Transferencias entre usuarios
- 🧾 Exportación de historial

---

## 👨‍💻 Autor

**David Cardona**  
Proyecto personal de aprendizaje enfocado en backend, lógica de negocio y futura migración a desarrollo web.

