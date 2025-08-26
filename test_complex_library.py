# test_complex_library.py

import unittest
import math
from complex_library import (
    suma_complejos, resta_complejos, producto_complejos, division_complejos,
    modulo_complejo, conjugado_complejo, fase_complejo,
    cartesiano_a_polar, polar_a_cartesiano
)

class TestComplexLibrary(unittest.TestCase):

    def test_suma_complejos(self):
        self.assertEqual(suma_complejos((3, 2), (1, 7)), (4, 9))
        self.assertEqual(suma_complejos((-1, -4), (3, 2)), (2, -2))

    def test_resta_complejos(self):
        self.assertEqual(resta_complejos((5, 4), (3, 2)), (2, 2))
        self.assertEqual(resta_complejos((2, 5), (5, 1)), (-3, 4))

    def test_producto_complejos(self):
        self.assertEqual(producto_complejos((3, 2), (1, 4)), (-5, 14))
        self.assertEqual(producto_complejos((1, 1), (1, 1)), (0, 2))

    def test_division_complejos(self):
        # Usamos assertAlmostEqual para comparar flotantes
        resultado1 = division_complejos((2, 8), (1, 2))
        self.assertAlmostEqual(resultado1[0], 3.6)
        self.assertAlmostEqual(resultado1[1], 0.8)
        
        resultado2 = division_complejos((10, 2), (2, 1))
        self.assertAlmostEqual(resultado2[0], 4.4)
        self.assertAlmostEqual(resultado2[1], -1.2)
        
    def test_modulo_complejo(self):
        self.assertEqual(modulo_complejo((3, 4)), 5)
        self.assertAlmostEqual(modulo_complejo((1, 1)), math.sqrt(2))

    def test_conjugado_complejo(self):
        self.assertEqual(conjugado_complejo((3, 4)), (3, -4))
        self.assertEqual(conjugado_complejo((-1, -5)), (-1, 5))

    def test_fase_complejo(self):
        self.assertAlmostEqual(fase_complejo((1, 1)), math.pi / 4)
        self.assertAlmostEqual(fase_complejo((-1, 0)), math.pi)

    def test_cartesiano_a_polar(self):
        mag, fase = cartesiano_a_polar((1, 1))
        self.assertAlmostEqual(mag, math.sqrt(2))
        self.assertAlmostEqual(fase, math.pi / 4)

        mag, fase = cartesiano_a_polar((0, 2))
        self.assertAlmostEqual(mag, 2)
        self.assertAlmostEqual(fase, math.pi / 2)
        
    def test_polar_a_cartesiano(self):
        real, imag = polar_a_cartesiano((2, math.pi))
        self.assertAlmostEqual(real, -2)
        self.assertAlmostEqual(imag, 0, places=7) # Aumentamos la precisión para evitar errores de punto flotante
        
        real, imag = polar_a_cartesiano((math.sqrt(2), math.pi/4))
        self.assertAlmostEqual(real, 1)
        self.assertAlmostEqual(imag, 1)


if __name__ == '__main__':
    unittest.main()