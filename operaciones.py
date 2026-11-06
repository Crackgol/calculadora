"""Funciones matemáticas de la calculadora."""


def suma(a, b):
    """Devuelve la suma de dos números."""
    return a + b


def resta(a, b):
    """Devuelve la resta de dos números."""
    return a - b


def multiplicacion(a, b):
    """Devuelve el producto de dos números."""
    return a * b


def division(a, b):
    """Devuelve la división de dos números."""
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero.")
    return a / b
