import unittest

from pruebas_Validacion_Usuario import (

    test_validar_usuario_nombre_corto,
    test_validar_usuario_nombre_largo,
    test_validar_usuario_nombre_con_espacio,
    test_validar_usuario_nombre_con_caracteres_invalidos,
    test_validar_usuario_nombre_valido,
    test_validar_usuario_nombre_con_num_al_final,
    test_validar_usuario_nombre_con_num_al_inicio,
    test_validar_usuario_nombre_con_num_en_medio,
    test_validar_usuario_nombre_con_num_y_letra,
    test_validar_usuario_nombre_con_num_y_caracteres_invalidos
)

class TestValidarUsuario(unittest.TestCase):
    def test_validar_usuario(self):
        """
        Ejecuta todos los casos de prueba importados del módulo pruebas_validacion_usuario.
        """
        test_cases = [
            test_validar_usuario_nombre_corto,
            test_validar_usuario_nombre_largo,
            test_validar_usuario_nombre_con_espacio,
            test_validar_usuario_nombre_con_caracteres_invalidos,
            test_validar_usuario_nombre_valido,
            test_validar_usuario_nombre_con_num_al_final,
            test_validar_usuario_nombre_con_num_al_inicio,
            test_validar_usuario_nombre_con_num_en_medio,
            test_validar_usuario_nombre_con_num_y_letra,
            test_validar_usuario_nombre_con_num_y_caracteres_invalidos
        ]
        for test_case in test_cases:
            test_case()

print("felicitaciones, usuarios validados correctamente")

if __name__ == '__main__':
    unittest.main()

"""
Este módulo contiene pruebas unitarias para validar nombres de usuario.
Las pruebas se importan del módulo `pruebas_validacion_usuario` e incluyen varios escenarios como:
- Nombres cortos
- Nombres largos
- Nombres con espacios
- Nombres con caracteres inválidos
- Nombres válidos
- Nombres con números al final
- Nombres con números al inicio
- Nombres con números en medio
- Nombres con números y letras
- Nombres con números y caracteres inválidos
"""