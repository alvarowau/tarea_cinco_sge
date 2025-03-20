import xmlrpc.client
import csv


def conectar_odoo(url='http://localhost:8069', db='odoo', user='alvaro@gmail.com', password='admin'):
    common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
    uid = common.authenticate(db, user, password, {})
    if not uid:
        raise Exception("Error de autenticación")
    models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
    return db, uid, password, models


def obtener_stock_productos(db, uid, password, models):
    productos = models.execute_kw(
        db, uid, password,
        'product.product', 'search_read',
        [[]],  # sin filtros
        {'fields': ['default_code', 'name', 'qty_available']}
    )
    return sorted(productos, key=lambda p: p['name'].lower())


def mostrar_productos(productos):
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


def guardar_csv_stock(productos, nombre_archivo="stock_productos_xmlrpc.csv"):
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


def main_stock_xmlrpc():
    db, uid, password, models = conectar_odoo()
    productos = obtener_stock_productos(db, uid, password, models)
    mostrar_productos(productos)
    guardar_csv_stock(productos)


if __name__ == "__main__":
    main_stock_xmlrpc()
