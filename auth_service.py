def validar_credenciales(usuario, clave):
    if usuario == "admin" and clave == "admin2026":
        return True
    return False

# Prueba basica del modulo de autenticacion
if validar_credenciales("admin", "admin2026"):
    print("Autenticacion exitosa: Acceso concedido")
else:
    print("Error: Credenciales invalidas")