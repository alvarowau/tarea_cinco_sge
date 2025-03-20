import csv
from html import unescape
import re
from parte_dos_cinco.conexion_odoo import ConexionOdoo
from parte_dos_cinco.stock_dao import OdooStockDAO


class OdooStock:
    """
    Clase que maneja la interacción con el inventario de productos de Odoo.

    Permite listar productos, obtener detalles de un producto específico y generar un archivo CSV
    con la información del stock de productos.
    """

    def __init__(self, conexion_odoo):
        """
        Inicializa la conexión a Odoo y el acceso a la base de datos.

        Args:
            conexion_odoo (ConexionOdoo): Objeto de conexión a Odoo.
        """
        self.dao = OdooStockDAO(conexion_odoo)
        self.listado_productos = []

    def __obtener_productos(self):
        """Carga los productos desde Odoo y los organiza en un listado."""
        dict_productos = self.dao.obtener_stock_productos()
        self.listado_productos = [
            {"index": idx, "producto": producto} for idx, producto in enumerate(dict_productos, start=1)
        ]
    def __limpiar_html(self, texto_html):
        texto_plano = re.sub(r'<[^>]*>', '', texto_html)
        return unescape(texto_plano.strip())

    def __listar_productos(self):
        """Muestra el listado de productos disponibles."""
        print("\nListado de productos:\n")
        if self.listado_productos:
            for producto in self.listado_productos:
                print(f"{producto['index']} {self.__limpiar_html(producto['producto']['name'])}")
        else:
            print("No se pudo listar productos.")

    def __obtener_descripcion(self):
        """Muestra la descripción de un producto seleccionado por el usuario."""
        self.__listar_productos()
        try:
            seleccion = int(input("\nSelecciona un producto (número): ")) - 1
            if 0 <= seleccion < len(self.listado_productos):
                producto_seleccionado = self.listado_productos[seleccion]["producto"]
                producto_base_datos = self.dao.obtener_stock_productos_por_id(producto_seleccionado["id"])
                if producto_base_datos:
                    print("\nInformación del producto seleccionado:")
                    print(f"Nombre: {self.__limpiar_html(producto_base_datos['name'])}")
                    print(f"Código: {self.__limpiar_html(producto_base_datos['default_code'])}")
                    print(f"Descripción: {self.__limpiar_html(producto_base_datos['description'])}")
                    print(f"Stock actual: {producto_base_datos['qty_available']}")
                else:
                    print("Error al obtener la información del producto.")
            else:
                print("Número fuera de rango, inténtalo de nuevo.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

    def show_menu(self):
        """Muestra el menú de opciones."""
        print("\n--- Menú Stock ---")
        print("1. Listado de productos")
        print("2. Obtener información del producto")
        print("3. Generar archivo CSV")
        print("4. Salir")

    def execute_menu(self):
        """Ejecuta el menú principal y maneja las opciones del usuario."""
        option = ""
        self.__obtener_productos()
        while option != "4":
            self.show_menu()
            option = input("Selecciona una opción: ")
            if option == "1":
                self.__listar_productos()
            elif option == "2":
                self.__obtener_descripcion()
            elif option == "3":
                self.generar_archivo()
            elif option == "4":
                print("Saliendo...")
            else:
                print("Opción no válida. Inténtalo de nuevo.")

    def generar_archivo(self, nombre_archivo="stock_productos.csv"):
        """
        Genera un archivo CSV con los productos y su información.

        Args:
            nombre_archivo (str, optional): Nombre del archivo CSV. Por defecto es "stock_productos.csv".
        """
        try:
            with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as file:
                campos = ["Código", "Descripción", "Stock"]
                writer = csv.DictWriter(file, fieldnames=campos)
                writer.writeheader()
                for producto in self.listado_productos:
                    p = producto["producto"]
                    pro = self.dao.obtener_stock_productos_por_id(p["id"])
                    if pro:
                        writer.writerow(
                            {
                                "Código": pro["default_code"] or "Sin código",
                                "Descripción": pro["description"],
                                "Stock": pro["qty_available"],
                            }
                        )
            print(f"\nCSV generado correctamente: {nombre_archivo}")
        except Exception as e:
            print(f"Error al guardar el archivo CSV: {e}")




if __name__ == "__main__":
    conexion = ConexionOdoo()
    conexion.conectar()
    stock = OdooStock(conexion)
    stock.execute_menu()
