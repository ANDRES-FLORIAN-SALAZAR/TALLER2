import unittest
from pruebas_Telefonicas import validar_telefono

def test_telefono_valido():
    assert validar_telefono("+34-600-123-4567") == True

def test_codigo_pais_incorrecto():
    assert validar_telefono("+3-600-123-4567") == False

def test_demasiados_digitos_primer_grupo():
    assert validar_telefono("+34-6000-123-4567") == False

def test_pocos_digitos_segundo_grupo():
    assert validar_telefono("+34-60-123-4567") == False

def test_sin_guiones():
    assert validar_telefono("+346001234567") == False

def test_letras_en_lugar_de_numeros():
    assert validar_telefono("+34-abc-def-ghij") == False

def test_caracteres_especiales():
    assert validar_telefono("+34-600-123-!@#$") == False

def test_telefono_vacio():
    assert validar_telefono("") == False

def test_telefono_con_espacios():
    assert validar_telefono("+34-600-123-4567 ") == False

def test_guion_extra_al_final():
    assert validar_telefono("+34-600-123-4567-") == False

class TestValidarTelefono(unittest.TestCase):
    def test_validar_todos_los_telefonos(self):
        """
        Ejecuta todos los casos de prueba para validar teléfonos.
        """
        test_cases = [
            test_telefono_valido,
            test_codigo_pais_incorrecto,
            test_demasiados_digitos_primer_grupo,
            test_pocos_digitos_segundo_grupo,
            test_sin_guiones,
            test_letras_en_lugar_de_numeros,
            test_caracteres_especiales,
            test_telefono_vacio,
            test_telefono_con_espacios,
            test_guion_extra_al_final
        ]
        for test_case in test_cases:
            test_case()
        print("Todas los numeros de telefono han sido validados correctamente.")

if __name__ == '__main__':
    unittest.main()