def validar_email(email):
    """
    Valida si un email tiene el formato usuario@dominio.extension.

    Args:
        email (str): El email a validar.

    Returns:
        bool: True si el email es válido, False en caso contrario.
    """
    if "@" not in email:
        return False

    partes = email.split("@")
    if len(partes) != 2:
        return False

    usuario, dominio_extension = partes
    if "." not in dominio_extension:
        return False

    dominio, extension = dominio_extension.split(".")
    if not (2 <= len(extension) <= 4):
        return False

    for char in usuario:
        if not (char.isalnum() or char in "._-"):
            return False

    for char in dominio:
        if not (char.isalnum() or char == "-"):
            return False

    if not extension.isalpha():
        return False

    return True

def test_validar_email():
    assert validar_email("juan.perez@empresa.com") == True, "Email válido"
    assert validar_email("maria@dominio") == False, "Email sin extensión"
    assert validar_email("pedro#2024@mail.org") == False, "Caracter no permitido"
    assert validar_email("usuario.especial_123@dominio.com") == True, "Caracteres especiales en usuario"
    assert validar_email("usuario@sub-dominio.com") == True, "Guiones en dominio"
    assert validar_email("usuario@dominio.comar") == False, "Extensión larga"
    assert validar_email("usuario@dominio.c") == False, "Extensión corta"
    assert validar_email("usuariodominiocom") == False, "Sin arroba"
    assert validar_email("usuario @dominio.com") == False, "Espacios en email"
    assert validar_email("usuario@dominio.123") == False, "Extension no alfabetica"
    print("Todas las pruebas pasaron")

if __name__ == '__main__':
    test_validar_email()