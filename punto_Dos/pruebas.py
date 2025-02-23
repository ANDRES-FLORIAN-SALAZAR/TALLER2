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

class TestCalcularPuntuacion(unittest.TestCase):
    def test_puntos_120_con_bono(self):
        self.assertEqual(calcular_puntuacion(120, True), "Oro")

    def test_puntos_120_sin_bono(self):
        self.assertEqual(calcular_puntuacion(120, False), "Bronce")

    def test_puntos_80_con_bono(self):
        self.assertEqual(calcular_puntuacion(80, True), "Plata")

    def test_puntos_30_con_bono(self):
        self.assertEqual(calcular_puntuacion(30, True), "Bronce")

    def test_puntos_49_sin_bono(self):
        self.assertEqual(calcular_puntuacion(49, False), "Bronce")

    # Pruebas adicionales
    def test_puntos_100_con_bono(self):
        self.assertEqual(calcular_puntuacion(100, True), "Oro")

    def test_puntos_50_con_bono(self):
        self.assertEqual(calcular_puntuacion(50, True), "Plata")

    def test_puntos_99_con_bono(self):
        self.assertEqual(calcular_puntuacion(99, True), "Plata")

    def test_puntos_51_sin_bono(self):
        self.assertEqual(calcular_puntuacion(51, False), "Bronce")

    def test_puntos_0_sin_bono(self):
        self.assertEqual(calcular_puntuacion(0, False), "Bronce")

if __name__ == '__main__':
    unittest.main()
