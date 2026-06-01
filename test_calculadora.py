# test_calculadora.py
# Pruebas automáticas para la calculadora
# Estudiante: Miguel Angel Patino Garcia
# Documento: 1000547947
# Estas pruebas son las que GitHub Actions ejecutará automáticamente

import unittest
from calculadora import sumar, restar, multiplicar, dividir, potencia, modulo

class TestCalculadora(unittest.TestCase):

    def test_sumar(self):
        """Prueba que la suma funciona correctamente."""
        self.assertEqual(sumar(2, 3), 5)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(0, 0), 0)
        print("Prueba de suma: PASADA")

    def test_restar(self):
        """Prueba que la resta funciona correctamente."""
        self.assertEqual(restar(10, 4), 6)
        self.assertEqual(restar(0, 5), -5)
        print("Prueba de resta: PASADA")

    def test_multiplicar(self):
        """Prueba que la multiplicación funciona correctamente."""
        self.assertEqual(multiplicar(3, 4), 12)
        self.assertEqual(multiplicar(0, 100), 0)
        print("Prueba de multiplicacion: PASADA")

    def test_dividir(self):
        """Prueba que la división funciona correctamente."""
        self.assertEqual(dividir(10, 2), 5)
        self.assertEqual(dividir(9, 3), 3)
        print("Prueba de division: PASADA")

    def test_dividir_por_cero(self):
        """Prueba que se detecta la división por cero."""
        with self.assertRaises(ValueError):
            dividir(5, 0)
        print("Prueba de division por cero: PASADA")

    def test_potencia(self):
        """Prueba que la potencia funciona correctamente."""
        self.assertEqual(potencia(2, 3), 8)
        self.assertEqual(potencia(5, 0), 1)
        print("Prueba de potencia: PASADA")

    def test_modulo(self):
        """Prueba que el módulo funciona correctamente."""
        self.assertEqual(modulo(10, 3), 1)
        self.assertEqual(modulo(15, 5), 0)
        print("Prueba de modulo: PASADA")

if __name__ == "__main__":
    unittest.main(verbosity=2)