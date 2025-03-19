from parte_dos.recoger_persona import recoger_datos_persona
from parte_dos.gestion_archivo import guardar_datos_en_csv, recuperar_datos_desde_csv

class DatosTablaUsuario:

    def __init__(self) -> None:
        self.datos_tabla = recuperar_datos_desde_csv()

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
            print("La tabla aún está vacía.")

    def mostrar_datos_persona(self, persona):
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

    def recoger_datos(self):
        self.datos_tabla.append(recoger_datos_persona())

    def add_to_csv(self, filename="tabla_datos_usuarios.csv"):
        guardar_datos_en_csv(self.datos_tabla, filename)

    def recuperar_datos_csv(self, filename="tabla_datos_usuarios.csv"):
        self.datos_tabla = recuperar_datos_desde_csv(filename)

    def show_menu(self):
        """Muestra el menú de opciones."""
        print("\n--- Menú Tabla de Datos ---")
        print("1. Solicitar datos de persona")
        print("2. Buscar persona")
        print("3. Añadir tabla a CSV")
        print("4. Recuperar tabla desde CSV")
        print("5. Mostrar tabla completa (¡Solo para pruebas!)")
        print("6. Salir del menú Tabla de Datos")

    def execute_menu(self):
        """Ejecuta el menú interactivo."""
        option = ""
        recuperar_datos_desde_csv()
        while option != "6":
            self.show_menu()
            option = input("Selecciona una opción: ")
            if option == "1":
                self.recoger_datos()
            elif option == "2":
                self.buscar_persona()
            elif option == "3":
                self.add_to_csv()
            elif option == "4":
                guardar_datos_en_csv(self.datos_tabla)
            elif option == "5":
                print("\n--- Tabla de Datos Completa (¡Solo para pruebas!) ---")
                if self.datos_tabla:
                    for person in self.datos_tabla:
                        self.mostrar_datos_persona(person)
                else:
                    print("La tabla está vacía.")
            elif option == "6":
                print("Saliendo del menú Tabla de Datos...")
            else:
                print("Opción no válida. Inténtalo de nuevo.")


def main_activity4():
    """Función principal para ejecutar la actividad 4."""
    my_table = DatosTablaUsuario()
    my_table.execute_menu()

if __name__ == "__main__":
    main_activity4()
