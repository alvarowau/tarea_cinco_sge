import re

patron = r"^[a-zA-Z0-9ñÑ]+$"

def validacion(nombre: str):
    """
    Valida si un nombre de usuario cumple con los siguientes requisitos:
    - Longitud mínima de 6 caracteres.
    - Longitud máxima de 12 caracteres.
    - Solo puede contener letras (mayúsculas y minúsculas), números y los caracteres 'ñ' o 'Ñ'.

    Parámetros:
    nombre (str): El nombre de usuario a validar.

    Retorna:
    tuple: Una tupla donde el primer elemento es un código de error (0 si es válido) y el segundo es un mensaje descriptivo.
           - (0, "El nombre de usuario es válido") si cumple con todos los requisitos.
           - (1, "El nombre de usuario debe contener al menos 6 caracteres") si es demasiado corto.
           - (2, "El nombre de usuario no puede contener más de 12 caracteres") si es demasiado largo.
           - (3, "El nombre de usuario puede contener solo letras y números") si contiene caracteres no permitidos.
    """
    if len(nombre) < 6:
        return (1, "El nombre de usuario debe contener al menos 6 caracteres")
    if len(nombre) > 12:
        return (2, "El nombre de usuario no puede contener más de 12 caracteres")
    if not re.match(patron, nombre):
        return (3, "El nombre de usuario puede contener solo letras y números")
    return (0, "El nombre de usuario es válido")
