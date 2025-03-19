import csv
import os

def guardar_datos_en_csv(datos, filename="tabla_datos_usuarios.csv"):
    """
    Guarda los datos en un archivo CSV.

    Args:
        datos (list): Lista de diccionarios con los datos de usuarios.
        filename (str): Nombre del archivo CSV.
    """
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
            csv_writer.writerows(datos)
            print(f"Tabla de datos guardada en '{filename}' correctamente.")
    except Exception as e:
        print(f"Error al guardar en CSV: {e}")


def recuperar_datos_desde_csv(filename="tabla_datos_usuarios.csv"):
    """
    Recupera los datos desde un archivo CSV.

    Args:
        filename (str): Nombre del archivo CSV.

    Returns:
        list: Lista de diccionarios con los datos recuperados.
    """
    try:
        if not os.path.exists(filename):
            print(
                f"El fichero CSV '{filename}' no existe. Se creará uno nuevo al guardar."
            )
            return []

        datos = []
        with open(filename, "r", newline="", encoding="utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                datos.append(dict(row))
        print(f"Datos recuperados de '{filename}' correctamente.")
        return datos
    except Exception as e:
        print(f"Error al recuperar datos desde CSV: {e}")
        return []
