class OdooStockDAO:
    """
    Clase para manejar las operaciones de acceso a la base de datos de Odoo relacionadas con el stock de productos.

    Permite obtener información sobre productos, como su lista completa, detalles específicos por ID,
    y maneja errores durante las operaciones de consulta.

    Atributos:
        conexion (ConexionOdoo): Objeto de conexión a Odoo.
        db (str): Nombre de la base de datos.
        uid (int): ID del usuario autenticado.
        password (str): Contraseña del usuario.
        models (ServerProxy): Objeto para interactuar con los modelos de Odoo.
    """

    def __init__(self, conexion_odoo):
        """
        Inicializa la clase con una conexión a Odoo.

        Args:
            conexion_odoo (ConexionOdoo): Objeto de conexión a Odoo.
        """
        self.conexion = conexion_odoo
        self.db = self.conexion.db
        self.uid = self.conexion.uid
        self.password = self.conexion.password
        self.models = self.conexion.models

    def obtener_stock_productos(self):
        """
        Obtiene todos los productos disponibles en Odoo.

        Returns:
            list: Lista de diccionarios con los campos 'id' y 'name' de cada producto,
                  ordenados alfabéticamente por nombre. Retorna una lista vacía en caso de error.
        """
        try:
            # Obtener todos los productos
            productos = self.models.execute_kw(
                self.db, self.uid, self.password,
                "product.product", "search_read",
                [[]],
                {"fields": ["id", "name"]},
            )
            # Ordenar los productos por nombre (ignorando mayúsculas/minúsculas)
            return sorted(productos, key=lambda p: p["name"].lower())
        except Exception as e:
            print(f"Error al obtener el stock de productos: {e}")
            return []

    def obtener_stock_productos_por_id(self, producto_id):
        """
        Obtiene los detalles de un producto específico por su ID.

        Args:
            producto_id (int): ID del producto a buscar.

        Returns:
            dict: Diccionario con los detalles del producto, incluyendo campos como 'id', 'default_code',
                  'name', 'qty_available', 'weight', 'barcode', 'product_tmpl_id' y 'description'.
                  Retorna None si el producto no se encuentra o hay un error.
        """
        try:
            # Buscar el producto por ID
            producto = self.models.execute_kw(
                self.db, self.uid, self.password,
                "product.product", "search_read",
                [[["id", "=", producto_id]]],
                {"fields": ["id", "default_code", "name", "qty_available", "weight", "barcode", "product_tmpl_id"]},
            )
            if producto:
                producto = producto[0]
                # Obtener la descripción de la plantilla del producto
                plantilla_producto = self.models.execute_kw(
                    self.db, self.uid, self.password,
                    "product.template", "search_read",
                    [[["id", "=", producto["product_tmpl_id"][0]]]],
                    {"fields": ["description"]},
                )
                producto["description"] = plantilla_producto[0].get("description", "Descripción no encontrada")
                return producto
            else:
                print(f"No se encontró el producto con ID {producto_id}")
                return None
        except Exception as e:
            print(f"Error al obtener el producto con ID {producto_id}: {e}")
            return None
