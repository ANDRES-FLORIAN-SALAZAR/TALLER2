import unittest

def calcular_puntuacion(puntuacion, es_premium):
    """
    Calcula la puntuación basada en la puntuación y si el usuario es premium.

    Args:
        puntuacion (int): La puntuación del usuario.
        es_premium (bool): Indica si el usuario es premium.

    Returns:
        str: La categoría de puntuación ("Oro", "Plata", "Bronce").
    """
    if puntuacion >= 100 and es_premium:
        return "Oro"
    elif puntuacion >= 50 and es_premium:
        return "Plata"
    else:
        return "Bronce"

def test_puntuacion_oro_premium():
    assert calcular_puntuacion(120, True) == "Oro"

def test_puntuacion_bronce_nopremium():
    assert calcular_puntuacion(120, False) == "Bronce"

def test_puntuacion_plata_premium():
    assert calcular_puntuacion(80, True) == "Plata"

def test_puntuacion_bronce_premium_bajo():
    assert calcular_puntuacion(30, True) == "Bronce"

def test_puntuacion_bronce_nopremium_limite_inferior():
    assert calcular_puntuacion(49, False) == "Bronce"

def test_puntuacion_oro_premium_limite_superior():
    assert calcular_puntuacion(100, True) == "Oro"

def test_puntuacion_plata_premium_limite_superior():
    assert calcular_puntuacion(50, True) == "Plata"

def test_puntuacion_plata_premium_limite_inferior():
    assert calcular_puntuacion(99, True) == "Plata"

def test_puntuacion_bronce_nopremium_limite_superior_51():
    assert calcular_puntuacion(51, False) == "Bronce"

def test_puntuacion_bronce_nopremium_cero():
    assert calcular_puntuacion(0, False) == "Bronce"

class TestCalcularPuntuacion(unittest.TestCase):
    def test_validar_todas_las_puntuaciones(self):
        """
        Ejecuta todos los casos de prueba para validar la puntuación.
        """
        test_cases = [
            test_puntuacion_oro_premium,
            test_puntuacion_bronce_nopremium,
            test_puntuacion_plata_premium,
            test_puntuacion_bronce_premium_bajo,
            test_puntuacion_bronce_nopremium_limite_inferior,
            test_puntuacion_oro_premium_limite_superior,
            test_puntuacion_plata_premium_limite_superior,
            test_puntuacion_plata_premium_limite_inferior,
            test_puntuacion_bronce_nopremium_limite_superior_51,
            test_puntuacion_bronce_nopremium_cero
        ]
        for test_case in test_cases:
            test_case()
        print("Todos los tests son correctos")

if __name__ == '__main__':
    unittest.main()

"""
Este módulo contiene una función para calcular la puntuación basada en puntos y un bono, 
y una serie de pruebas unitarias para verificar su correcto funcionamiento.

Funciones:
    calcular_puntuacion(puntos, bonus):
        Calcula la puntuación y devuelve una clasificación basada en los puntos y si hay un bono.

    TestCalcularPuntuacion():
        Realiza pruebas unitarias para la función calcular_puntuacion.
"""