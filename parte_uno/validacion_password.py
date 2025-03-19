def validacion(password: str):
    """
    Valida si una contraseña cumple con los siguientes requisitos:
    - Longitud mínima de 8 caracteres.
    - No contiene espacios.
    - Al menos una letra minúscula.
    - Al menos una letra mayúscula.
    - Al menos un dígito.
    - Al menos un carácter especial (no alfanumérico).

    Parámetros:
    password (str): La contraseña a validar.

    Retorna:
    bool: True si la contraseña es válida, False en caso contrario.
    """
    if len(password) < 8:
        return False
    if " " in password:
        return False

    minuscula = any(c.islower() for c in password)
    mayuscula = any(c.isupper() for c in password)
    digito = any(c.isdigit() for c in password)
    especial = any(not c.isalnum() for c in password)

    return minuscula and mayuscula and digito and especial
