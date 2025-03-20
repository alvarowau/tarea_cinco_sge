import xmlrpc.client


class ConexionOdoo:
    """
    Clase para gestionar la conexión con un servidor Odoo utilizando XML-RPC.

    Permite establecer una conexión con Odoo, autenticar al usuario y manejar errores de conexión.
    Si la conexión falla, el usuario puede ingresar nuevos datos de conexión o salir del programa.

    Atributos:
        url (str): URL del servidor Odoo.
        db (str): Nombre de la base de datos.
        user (str): Correo electrónico del usuario.
        password (str): Contraseña del usuario.
        uid (int): ID del usuario autenticado.
        models (ServerProxy): Objeto para interactuar con los modelos de Odoo.
    """

    def __init__(self, url="http://localhost:8069", db="odoo", user="alvaro@gmail.com", password="admin"):
        """
        Inicializa la conexión con Odoo.

        Args:
            url (str, optional): URL del servidor Odoo. Por defecto es "http://localhost:8069".
            db (str, optional): Nombre de la base de datos. Por defecto es "odoo".
            user (str, optional): Correo electrónico del usuario. Por defecto es "alvaro@gmail.com".
            password (str, optional): Contraseña del usuario. Por defecto es "admin".
        """
        self.url = url
        self.db = db
        self.user = user
        self.password = password
        self.uid = None
        self.models = None

    def conectar(self):
        """
        Establece la conexión con el servidor Odoo y autentica al usuario.

        Si la autenticación falla, solicita nuevos datos de conexión al usuario.
        """
        try:
            # Conectar al endpoint común de Odoo
            common = xmlrpc.client.ServerProxy(f"{self.url}/xmlrpc/2/common")
            # Autenticar al usuario
            self.uid = common.authenticate(self.db, self.user, self.password, {})
            if not self.uid:
                print("Error de autenticación.")
                self.solicitar_nuevos_datos()
            else:
                # Conectar al endpoint de modelos de Odoo
                self.models = xmlrpc.client.ServerProxy(f"{self.url}/xmlrpc/2/object")
                print("Conexión establecida correctamente.")
        except Exception as e:
            print(f"Error al conectar: {e}")
            self.solicitar_nuevos_datos()

    def solicitar_nuevos_datos(self):
        """
        Solicita nuevos datos de conexión al usuario si la conexión falla.

        Permite al usuario ingresar una nueva URL, base de datos, usuario y contraseña,
        o salir del programa.
        """
        while True:
            print("\nLa conexión falló. Opciones:")
            print("1. Ingresar nuevos datos de conexión")
            print("2. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion.isdigit():
                if opcion == "1":
                    # Solicitar nuevos datos de conexión
                    self.url = input("Nueva URL (por ejemplo, http://localhost:8069): ")
                    self.db = input("Base de datos: ")
                    self.user = input("Correo de usuario Odoo: ")
                    self.password = input("Contraseña: ")
                    # Intentar conectar nuevamente
                    self.conectar()
                    break
                elif opcion == "2":
                    print("Saliendo...")
                    exit()
                else:
                    print("Opción no válida. Intenta de nuevo.")
            else:
                print("Entrada no válida. Ingresa un número.")
