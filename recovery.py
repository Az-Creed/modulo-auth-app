def recuperar_contrasena(correo):
    if correo == "usuario@ups.edu.ec":
        print("Enlace de recuperacion enviado a:", correo)
    else:
        print("El correo ingresado no se encuentra registrado.")

# Prueba de recuperacion
recuperar_contrasena("usuario@ups.edu.ec")