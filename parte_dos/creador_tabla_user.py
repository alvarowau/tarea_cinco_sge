from parte_uno.validacion_nombre import nombre_validacion
from parte_uno.validacion_password import password_validacion
import csv
import os

class DatosTablaUsuario:

    def __init__(self) -> None:
        self.datos_tabla = []


    def buscar_persona(self):
        if self.datos_tabla:
            termino_buscar = input(
            "Introduce nombre de usuario, nombre o apellido a buscar: "
        ).lower()
            resultados = []
            for persona in self.datos_tabla:
                if(
                    termino_buscar in persona['nombre'].lower() or
                    termino_buscar in persona['primer_apellido'].lower() or
                    termino_buscar in persona['segundo_apellido'].lower() or
                    termino_buscar in persona['username'].lower()
                ):
                    resultados.append(persona)

            if resultados:
                print("\nResultados de la búsqueda:")
                for persona in resultados:
                    self.mostrar_datos_persona(persona)
            else:
                print("No se encontraron coincidencias.")
        else:
            print("la tabla aun esta vacia")

    def mostrar_datos_persona(self, persona):
        """
        Muestra los datos de la persona almacenados en el diccionario 'persona'.
        """
        print("-" * 30)
        print(f"Nombre del cliente: {persona['nombre']} {persona['primer_apellido']} {persona['segundo_apellido']}")
        print(f"Nombre de usuario: {persona['username']}")
        print(f"Contraseña: {persona['password']}")
        print(f"Dirección: {persona['direccion']}")
        print(f"Teléfono: {persona['telefono']}")
        print(f"Email: {persona['email']}")
        print(f"Población: {persona['poblacion']}")
        print(f"Código Postal: {persona['codigo_postal']}")
        print(f"Página web: {persona['pagina_web'] if persona['pagina_web'] else 'No proporcionada'}")
        print("-" * 30)


    def recoger_datos_persona(self):
        """
        Recoge los datos personales del cliente y realiza las validaciones necesarias.
        """
        datos_personales = {}
        print("\nIntroduce los datos del cliente:")
        datos_personales["nombre"] = input("Introduce el nombre del cliente: ")
        datos_personales["primer_apellido"] = input("Introduce el primer apellido del cliente: ")
        datos_personales["segundo_apellido"] = input("Introduce el segundo apellido del cliente: ")

        # Recoger y validar el nombre de usuario
        while True:
            user_name = input("Introduce el nombre a mostrar (nombre de usuario): ")
            response_user = nombre_validacion(user_name)
            if response_user[0] == 0:
                datos_personales["username"] = user_name
                break
            else:
                print(response_user[1])

        # Recoger y validar la contraseña
        while True:
            print("La contraseña debe tener más de 8 caracteres, una mayúscula, una minúscula, un dígito y un carácter especial como mínimo.")
            password = input("Introduce la contraseña: ")
            if password_validacion(password):
                datos_personales["password"] = password
                break
            else:
                print("La contraseña no es válida.")

        # Recoger la dirección
        datos_personales["direccion"] = input("Introduce la dirección: ")

        # Recoger y validar el teléfono
        while True:
            telefono = input("Introduce el teléfono: ")
            if telefono.isdigit() and len(telefono) >= 7:
                datos_personales["telefono"] = telefono
                break
            else:
                print("El teléfono debe contener solo números y tener al menos 7 caracteres.")

        # Recoger y validar el email
        while True:
            email = input("Introduce el email: ")
            if "@" in email and "." in email:
                datos_personales["email"] = email
                break
            else:
                print("Por favor, introduce un email válido.")

        # Recoger la página web (opcional)
        datos_personales["pagina_web"] = input("Introduce la página web (opcional): ")

        # Recoger la población
        datos_personales["poblacion"] = input("Introduce la población: ")

        # Recoger y validar el código postal
        while True:
            codigo_postal = input("Introduce el código postal: ")
            if codigo_postal.isdigit() and len(codigo_postal) == 5:
                datos_personales["codigo_postal"] = codigo_postal
                break
            else:
                print("El código postal debe contener 5 dígitos.")

        self.datos_tabla.append(datos_personales)


    def add_to_csv(self, filename="tabla_datos_usuarios.csv"):
        try:
            with open(filename, "w", newline="", encoding="utf-8") as csv_file:
                column_names = [
                    "nombre",
                    "primer_apellido",
                    "segundo_apellido",
                    "username",
                    "password",
                    "direccion",
                    "telefono",
                    "email",
                    "pagina_web",
                    "poblacion",
                    "codigo_postal"
                ]
                csv_writer = csv.DictWriter(csv_file, fieldnames=column_names)
                csv_writer.writeheader()
                csv_writer.writerows(self.datos_tabla)
                print(f"Tabla de datos guardada en '{filename}' correctamente.")
        except Exception as e:
            print(f"Error al guardar en CSV: {e}")


    def recuperar_datos_csv(self, filename="tabla_datos_usuarios.csv"):
        """Recupera los datos desde un archivo CSV.

        Args:
            filename (str): Nombre del archivo CSV desde donde se recuperarán los datos.
        """
        try:
            if not os.path.exists(filename):
                print(
                    f"El fichero CSV '{filename}' no existe. Se creará uno nuevo al guardar."
                )
                self.data_table = []
                return

            self.data_table = []
            with open(filename, "r", newline="", encoding="utf-8") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    self.data_table.append(dict(row))
            print(f"Datos recuperados de '{filename}' correctamente.")
        except Exception as e:
            print(f"Error al recuperar datos desde CSV: {e}")
