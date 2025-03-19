from validacion_nombre import nombre_validacion
from validacion_password import password_validacion

def main():
    """
    Función principal que solicita al usuario un nombre de usuario y una contraseña,
    los valida utilizando las funciones importadas y muestra los resultados.

    - Importa las funciones `nombre_validacion` y `password_validacion` desde los módulos correspondientes.
    - Solicita al usuario que ingrese un nombre de usuario y una contraseña.
    - Valida el nombre de usuario y la contraseña utilizando las funciones importadas.
    - Muestra un mensaje indicando si el nombre de usuario es válido o no.
    - Muestra un mensaje indicando si la contraseña es válida o no.
    """
    nombre = input("Digite su nombre: ")
    password = input("Digite su contraseña: ")

    response_nombre = nombre_validacion(nombre)
    response_password = password_validacion(password)

    print(response_nombre[1])
    print("Contraseña válida" if response_password else "Contraseña no válida")

if __name__ == "__main__":
    main()
