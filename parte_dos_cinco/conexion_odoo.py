import xmlrpc.client
from curses.ascii import isdigit

class ConexionOdoo:
    def __init__(self, url='http://localhost:8069', db='odoo', user='alvaro@gmail.com', password='admin'):
        self.url = url
        self.db = db
        self.user = user
        self.password = password
        self.uid = None
        self.models = None

    def conectar(self):
        try:
            common = xmlrpc.client.ServerProxy(f"{self.url}/xmlrpc/2/common")
            self.uid = common.authenticate(self.db, self.user, self.password, {})
            if not self.uid:
                print("Error de autenticación.")
                self.solicitar_nuevos_datos()
            else:
                self.models = xmlrpc.client.ServerProxy(f"{self.url}/xmlrpc/2/object")
                print("Conexión establecida correctamente.")
        except Exception as e:
            print(f"Error al conectar: {e}")
            self.solicitar_nuevos_datos()

    def solicitar_nuevos_datos(self):
        while True:
            print("\nLa conexión falló. Opciones:")
            print("1. Ingresar nuevos datos de conexión")
            print("2. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion.isdigit():
                if opcion == '1':
                    self.url = input("Nueva URL (por ejemplo, http://localhost:8069): ")
                    self.db = input("Base de datos: ")
                    self.user = input("Correo de usuario Odoo: ")
                    self.password = input("Contraseña: ")
                    self.conectar()
                    break
                elif opcion == '2':
                    print("Saliendo...")
                    exit()
                else:
                    print("Opción no válida. Intenta de nuevo.")
            else:
                print("Entrada no válida. Ingresa un número.")

# Ejemplo de uso:
if __name__ == "__main__":
    conexion = ConexionOdoo()
    conexion.conectar()
