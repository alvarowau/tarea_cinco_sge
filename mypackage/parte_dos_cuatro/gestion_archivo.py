import csv
import os


def guardar_datos_en_csv(datos, filename="tabla_datos_usuarios.csv"):
    """
    Guarda los datos de usuarios en un archivo CSV.

    Args:
        datos (list): Lista de diccionarios, donde cada diccionario contiene los datos de un usuario.
        filename (str, optional): Nombre del archivo CSV. Por defecto es "tabla_datos_usuarios.csv".

    Raises:
        Exception: Si ocurre un error durante la escritura del archivo CSV.
    """
    try:
        # Abrir el archivo CSV en modo escritura
        with open(filename, "w", newline="", encoding="utf-8") as csv_file:
            # Definir las columnas del CSV
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
                "codigo_postal",
                "tipo",
            ]
            # Crear un escritor CSV
            csv_writer = csv.DictWriter(csv_file, fieldnames=column_names)
            # Escribir la cabecera y los datos
            csv_writer.writeheader()
            csv_writer.writerows(datos)
            print(f"Tabla de datos guardada en '{filename}' correctamente.")
    except Exception as e:
        print(f"Error al guardar en CSV: {e}")


def recuperar_datos_desde_csv(filename="tabla_datos_usuarios.csv"):
    """
    Recupera los datos de usuarios desde un archivo CSV.

    Args:
        filename (str, optional): Nombre del archivo CSV. Por defecto es "tabla_datos_usuarios.csv".

    Returns:
        list: Lista de diccionarios, donde cada diccionario contiene los datos de un usuario.
              Retorna una lista vacía si el archivo no existe o hay un error.

    Raises:
        Exception: Si ocurre un error durante la lectura del archivo CSV.
    """
    try:
        # Verificar si el archivo existe
        if not os.path.exists(filename):
            print(f"El fichero CSV '{filename}' no existe. Se creará uno nuevo al guardar.")
            return []

        datos = []
        # Abrir el archivo CSV en modo lectura
        with open(filename, "r", newline="", encoding="utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            # Leer cada fila y agregarla a la lista de datos
            for row in csv_reader:
                datos.append(dict(row))
        print(f"Datos recuperados de '{filename}' correctamente.")
        return datos
    except Exception as e:
        print(f"Error al recuperar datos desde CSV: {e}")
        return []
