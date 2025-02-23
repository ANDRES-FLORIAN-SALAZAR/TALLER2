import unittest
from pruebas_Validar_Email import validar_email

def test_email_valido():
    assert validar_email("juan.perez@empresa.com") == True

def test_email_sin_extension():
    assert validar_email("maria@dominio") == False

def test_email_caracter_no_permitido():
    assert validar_email("pedro#2024@mail.org") == False

def test_email_con_caracteres_especiales_usuario():
    assert validar_email("usuario.especial_123@dominio.com") == True

def test_email_con_guiones_dominio():
    assert validar_email("usuario@sub-dominio.com") == True

def test_email_extension_larga():
    assert validar_email("usuario@dominio.comar") == False

def test_email_extension_corta():
    assert validar_email("usuario@dominio.c") == False

def test_email_sin_arroba():
    assert validar_email("usuariodominiocom") == False

def test_email_con_espacios():
    assert validar_email("usuario @dominio.com") == False

def test_email_extension_no_alfabetica():
    assert validar_email("usuario@dominio.123") == False

class TestValidarEmail(unittest.TestCase):
    def test_validar_todos_los_emails(self):
        """
        Ejecuta todos los casos de prueba importados para validar emails.
        """
        test_cases = [
            test_email_valido,
            test_email_sin_extension,
            test_email_caracter_no_permitido,
            test_email_con_caracteres_especiales_usuario,
            test_email_con_guiones_dominio,
            test_email_extension_larga,
            test_email_extension_corta,
            test_email_sin_arroba,
            test_email_con_espacios,
            test_email_extension_no_alfabetica
        ]
        for test_case in test_cases:
            test_case()
            
print("Todos los tests son correctos")

if __name__ == '__main__':
    unittest.main()