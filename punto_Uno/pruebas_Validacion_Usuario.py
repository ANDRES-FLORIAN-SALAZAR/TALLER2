import unittest

def validar_usuario(nombre):
    """
    Verifica si un nombre de usuario es válido.

    Un nombre de usuario válido debe cumplir con las siguientes reglas:
    - Debe tener entre 3 y 15 caracteres.
    - No debe contener espacios.
    - Debe ser alfanumérico (solo letras y números).

    Args:
        nombre (str): El nombre de usuario a validar.

    Returns:
        bool: True si el nombre de usuario es válido, False en caso contrario.
    """
    if len(nombre) < 3 or len(nombre) > 15:
        return False
    if " " in nombre:
        return False
    if not nombre.isalnum():
        return False
    return True

def test_validar_usuario_nombre_corto():
    """Prueba un nombre de usuario que es demasiado corto."""
    nombre = "an"
    assert not validar_usuario(nombre), f"Error: nombre '{nombre}' es demasiado corto"

def test_validar_usuario_nombre_largo():
    """Prueba un nombre de usuario que es demasiado largo."""
    nombre = "a" * 16
    assert not validar_usuario(nombre), f"Error: nombre '{nombre}' es demasiado largo"

def test_validar_usuario_nombre_con_espacio():
    """Prueba un nombre de usuario que contiene un espacio."""
    nombre = "nombre con espacio"
    assert not validar_usuario(nombre), f"Error: nombre '{nombre}' contiene un espacio"

def test_validar_usuario_nombre_con_caracteres_invalidos():
    """Prueba un nombre de usuario que contiene caracteres inválidos."""
    nombre = "a!@#$"
    assert not validar_usuario(nombre), f"Error: nombre '{nombre}' contiene caracteres invalidos"

def test_validar_usuario_nombre_valido():
    """Prueba un nombre de usuario válido."""
    nombre = "andres"
    assert validar_usuario(nombre), f"Error: nombre '{nombre}' no debería ser válido"

def test_validar_usuario_nombre_con_num_al_final():
    """Prueba un nombre de usuario válido que contiene un número al final."""
    nombre = "Pedro5"
    assert validar_usuario(nombre), f"Error: nombre '{nombre}' debería ser válido"

def test_validar_usuario_nombre_con_num_al_inicio():
    """Prueba un nombre de usuario válido que contiene un número al inicio."""
    nombre = "5Pedro"
    assert validar_usuario(nombre), f"Error: nombre '{nombre}' debería ser válido"

def test_validar_usuario_nombre_con_num_en_medio():
    """Prueba un nombre de usuario válido que contiene números en el medio."""
    nombre = "La92ur4"
    assert validar_usuario(nombre), f"Error: nombre '{nombre}' debería ser válido"

def test_validar_usuario_nombre_con_num_y_letra():
    """Prueba un nombre de usuario válido que contiene números y letras."""
    nombre = "La92ur4"
    assert validar_usuario(nombre), f"Error: nombre '{nombre}' debería ser válido"

def test_validar_usuario_nombre_con_num_y_caracteres_invalidos():
    """Prueba un nombre de usuario que contiene números y caracteres inválidos."""
    nombre = "La92ur4@"
    assert not validar_usuario(nombre), f"Error: nombre '{nombre}' contiene caracteres invalidos"

if __name__ == '__main__':
    unittest.main()