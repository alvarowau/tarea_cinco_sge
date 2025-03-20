import csv

from parte_dos_cinco.conexion_odoo import ConexionOdoo


class StockOdoo:
    def __init__(self, conexion_odoo):
        self.conexion = conexion_odoo
        self.db = self.conexion.db
        self.uid = self.conexion.uid
        self.password = self.conexion.password
        self.models = self.conexion.models

    def obtener_stock_productos(self):
        try:
            productos = self.models.execute_kw(
                self.db, self.uid, self.password,
                'product.product', 'search_read',
                [[]],  # sin filtros
                {'fields': ['default_code', 'name', 'qty_available']}
            )
            return sorted(productos, key=lambda p: p['name'].lower())
        except Exception as e:
            print(f"Error al obtener el stock de productos: {e}")
            return []

    def mostrar_productos(self, productos):
        print("\nListado de productos:\n")
        for idx, producto in enumerate(productos, start=1):
            print(f"{idx}. {producto['name']}")
        while True:
            try:
                seleccion = int(input("\nSelecciona un producto (número): ")) - 1
                if seleccion < 0 or seleccion >= len(productos):
                    print("Número fuera de rango, inténtalo de nuevo.")
                    continue
                producto_seleccionado = productos[seleccion]
                print("\nInformación del producto seleccionado:")
                print(f"Código: {producto_seleccionado['default_code']}")
                print(f"Descripción: {producto_seleccionado['name']}")
                print(f"Stock actual: {producto_seleccionado['qty_available']}")
                break
            except ValueError:
                print("Entrada inválida, ingresa un número válido.")

    def guardar_csv_stock(self, productos, nombre_archivo="stock_productos.csv"):
        try:
            with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as file:
                campos = ['Código', 'Descripción', 'Stock']
                writer = csv.DictWriter(file, fieldnames=campos)
                writer.writeheader()
                for producto in productos:
                    writer.writerow({
                        'Código': producto['default_code'] or 'Sin código',
                        'Descripción': producto['name'],
                        'Stock': producto['qty_available']
                    })
            print(f"\nCSV generado correctamente: {nombre_archivo}")
        except Exception as e:
            print(f"Error al guardar el archivo CSV: {e}")

# Ejemplo de uso:
if __name__ == "__main__":
    # Crear una instancia de la clase ConexionOdoo
    conexion = ConexionOdoo()
    conexion.conectar()

    # Crear una instancia de la clase StockOdoo
    stock = StockOdoo(conexion)

    # Obtener el stock de productos
    productos = stock.obtener_stock_productos()

    # Mostrar los productos
    stock.mostrar_productos(productos)

    # Guardar el stock en un archivo CSV
    stock.guardar_csv_stock(productos)
