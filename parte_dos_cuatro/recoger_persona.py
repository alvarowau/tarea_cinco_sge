from parte_uno.validacion_nombre import nombre_validacion
from parte_uno.validacion_password import password_validacion


def recoger_datos_persona():
    """
    Recoge los datos personales del cliente y realiza las validaciones necesarias.

    Esta función solicita al usuario que ingrese información personal como nombre, apellidos,
    nombre de usuario, contraseña, dirección, teléfono, email, página web, población y código postal.
    Realiza validaciones en tiempo real para asegurar que los datos ingresados cumplan con los requisitos.

    Retorna:
        dict: Un diccionario con los datos personales del cliente validados.
    """
    datos_personales = {}
    print("\nIntroduce los datos del cliente:")

    # Recoger datos básicos
    datos_personales["nombre"] = input("Introduce el nombre del cliente: ")
    datos_personales["primer_apellido"] = input("Introduce el primer apellido del cliente: ")
    datos_personales["segundo_apellido"] = input("Introduce el segundo apellido del cliente: ")

    # Validar nombre de usuario
    while True:
        user_name = input("Introduce el nombre a mostrar (nombre de usuario): ")
        response_user = nombre_validacion(user_name)
        if response_user[0] == 0:
            datos_personales["username"] = user_name
            break
        else:
            print(response_user[1])

    # Validar contraseña
    while True:
        print("La contraseña debe tener más de 8 caracteres, una mayúscula, una minúscula, un dígito y un carácter especial como mínimo.")
        password = input("Introduce la contraseña: ")
        if password_validacion(password):
            datos_personales["password"] = password
            break
        else:
            print("La contraseña no es válida.")

    # Recoger dirección
    datos_personales["direccion"] = input("Introduce la dirección: ")

    # Validar teléfono
    while True:
        telefono = input("Introduce el teléfono: ")
        if telefono.isdigit() and len(telefono) >= 7:
            datos_personales["telefono"] = telefono
            break
        else:
            print("El teléfono debe contener solo números y tener al menos 7 caracteres.")

    # Validar email
    while True:
        email = input("Introduce el email: ")
        if "@" in email and "." in email:
            datos_personales["email"] = email
            break
        else:
            print("Por favor, introduce un email válido.")

    # Recoger página web (opcional)
    datos_personales["pagina_web"] = input("Introduce la página web (opcional): ")

    # Recoger población
    datos_personales["poblacion"] = input("Introduce la población: ")

    # Validar código postal
    while True:
        codigo_postal = input("Introduce el código postal: ")
        if codigo_postal.isdigit() and len(codigo_postal) == 5:
            datos_personales["codigo_postal"] = codigo_postal
            break
        else:
            print("El código postal debe contener 5 dígitos.")

    return datos_personales
