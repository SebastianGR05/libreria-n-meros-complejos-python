# complex_library.py

import math

# --- Operaciones Básicas ---

def suma_complejos(c1, c2):
    """
    Suma dos números complejos en representación cartesiana.
    c1: Tupla (real, imaginaria)
    c2: Tupla (real, imaginaria)
    Retorna: Tupla (real, imaginaria) de la suma.
    """
    return (c1[0] + c2[0], c1[1] + c2[1])

def resta_complejos(c1, c2):
    """
    Resta dos números complejos en representación cartesiana.
    c1: Tupla (real, imaginaria) del minuendo.
    c2: Tupla (real, imaginaria) del sustraendo.
    Retorna: Tupla (real, imaginaria) de la resta.
    """
    return (c1[0] - c2[0], c1[1] - c2[1])

def producto_complejos(c1, c2):
    """
    Multiplica dos números complejos en representación cartesiana.
    (a + bi) * (c + di) = (ac - bd) + (ad + bc)i
    c1: Tupla (a, b)
    c2: Tupla (c, d)
    Retorna: Tupla (real, imaginaria) del producto.
    """
    real = c1[0] * c2[0] - c1[1] * c2[1]
    imaginaria = c1[0] * c2[1] + c1[1] * c2[0]
    return (real, imaginaria)

def division_complejos(c1, c2):
    """
    Divide dos números complejos en representación cartesiana.
    (a + bi) / (c + di) = [(ac + bd) / (c^2 + d^2)] + [(bc - ad) / (c^2 + d^2)]i
    c1: Tupla (a, b) (dividendo)
    c2: Tupla (c, d) (divisor)
    Retorna: Tupla (real, imaginaria) de la división.
    """
    denominador = c2[0]**2 + c2[1]**2
    if denominador == 0:
        raise ValueError("División por cero no permitida.")
    
    real = (c1[0] * c2[0] + c1[1] * c2[1]) / denominador
    imaginaria = (c1[1] * c2[0] - c1[0] * c2[1]) / denominador
    return (real, imaginaria)

# --- Propiedades y Conversiones ---

def modulo_complejo(c):
    """
    Calcula el módulo (magnitud) de un número complejo.
    |a + bi| = sqrt(a^2 + b^2)
    c: Tupla (real, imaginaria)
    Retorna: Float con el valor del módulo.
    """
    return math.sqrt(c[0]**2 + c[1]**2)

def conjugado_complejo(c):
    """
    Calcula el conjugado de un número complejo.
    El conjugado de (a + bi) es (a - bi).
    c: Tupla (real, imaginaria)
    Retorna: Tupla (real, imaginaria) del conjugado.
    """
    return (c[0], -c[1])

def fase_complejo(c):
    """
    Calcula la fase (ángulo) de un número complejo en radianes.
    fase = atan2(imaginaria, real)
    c: Tupla (real, imaginaria)
    Retorna: Float con el valor de la fase en radianes.
    """
    return math.atan2(c[1], c[0])

def cartesiano_a_polar(c):
    """
    Convierte un número complejo de representación cartesiana a polar.
    c: Tupla (real, imaginaria)
    Retorna: Tupla (magnitud, fase en radianes).
    """
    magnitud = modulo_complejo(c)
    fase = fase_complejo(c)
    return (magnitud, fase)

def polar_a_cartesiano(p):
    """
    Convierte un número complejo de representación polar a cartesiana.
    p: Tupla (magnitud, fase en radianes)
    Retorna: Tupla (real, imaginaria).
    """
    real = p[0] * math.cos(p[1])
    imaginaria = p[0] * math.sin(p[1])
    return (real, imaginaria)