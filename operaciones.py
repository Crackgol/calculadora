"""Funciones matemáticas de la calculadora."""

import math


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


def potencia(base, exponente):
    """Devuelve la base elevada al exponente."""
    if base == 0 and exponente < 0:
        raise ValueError("No se puede elevar cero a un exponente negativo.")
    if base < 0 and not float(exponente).is_integer():
        raise ValueError("Una base negativa requiere un exponente entero.")
    return base ** exponente


def modulo(dividendo, divisor):
    """Devuelve el residuo de la división."""
    if divisor == 0:
        raise ZeroDivisionError("No se puede calcular el módulo con divisor cero.")
    return dividendo % divisor


def raiz_cuadrada(numero):
    """Devuelve la raíz cuadrada de un número no negativo."""
    if numero < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
    return math.sqrt(numero)


def porcentaje(cantidad, tanto_por_ciento):
    """Devuelve el porcentaje indicado de una cantidad."""
    return cantidad * tanto_por_ciento / 100


def valor_absoluto(numero):
    """Devuelve el valor absoluto de un número."""
    return abs(numero)


def factorial(numero):
    """Devuelve el factorial de un entero no negativo."""
    if isinstance(numero, bool) or not isinstance(numero, int):
        raise TypeError("El factorial solo acepta números enteros.")
    if numero < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    return math.factorial(numero)
