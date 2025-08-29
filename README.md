# Librería de Números Complejos en Python

Este proyecto es una librería simple en Python para realizar operaciones aritméticas con números complejos. Los números complejos se representan como tuplas de Python, evitando el uso del tipo de dato `complex` nativo para fines educativos y de práctica.

## Características

La librería soporta las siguientes operaciones:

* **Suma, resta, multiplicación y división** de números complejos.
* Cálculo del **módulo** y el **conjugado**.
* Obtención de la **fase** (ángulo).
* **Conversión** entre representaciones cartesianas (real, imaginaria) y polares (magnitud, fase).

## Estructura del Proyecto

```
complejos/
├── .gitignore
├── README.md
├── complex_library.py      # La librería principal con las funciones
└── test_complex_library.py # Pruebas unitarias para la librería
```

## Requisitos

* Python 3.x

## Cómo Usar la Librería

Para usar las funciones, importa el módulo `complex_library` en tu archivo de Python.

```python
import complex_library as cl

# Ejemplo de uso
c1 = (3, 2)  # Representa 3 + 2i
c2 = (1, 7)  # Representa 1 + 7i

# Suma
suma = cl.suma_complejos(c1, c2)
print(f"Suma: {suma}")  # Salida: (4, 9)

# Módulo
mod = cl.modulo_complejo(c1)
print(f"Módulo de c1: {mod}") # Salida: 3.6055...

# Conversión a polar
polar = cl.cartesiano_a_polar(c1)
print(f"Forma polar de c1: {polar}")
```

## Cómo Ejecutar las Pruebas

Este proyecto incluye un conjunto de pruebas automáticas para asegurar que la librería funciona correctamente. Para ejecutarlas, navega a la raíz del directorio del proyecto en tu terminal y ejecuta el siguiente comando:

```bash
python -m unittest test_complex_library.py
```
