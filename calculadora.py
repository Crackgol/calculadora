"""Interfaz de usuario de la calculadora."""

import operaciones


def formatear_numero(valor):
    """Devuelve una representación legible del número."""
    if isinstance(valor, int):
        return str(valor)
    if isinstance(valor, float):
        if valor.is_integer():
            return str(int(valor))
        texto = f"{valor:.10f}".rstrip("0").rstrip(".")
        if texto == "0" and valor != 0:
            return str(valor)
        return texto if texto else "0"
    return str(valor)


def leer_numero(mensaje):
    """Solicita un número y repite hasta recibir una entrada válida."""
    while True:
        entrada = input(mensaje).strip().replace(",", ".")
        try:
            return float(entrada)
        except ValueError:
            print("Entrada inválida. Ingresa un número, por ejemplo: 12, 3.5 o -2.")


def ejecutar_binaria(historial, nombre, funcion, etiqueta_a, etiqueta_b):
    """Solicita dos números, calcula y registra una operación binaria."""
    print(f"\n--- {nombre} ---")
    a = leer_numero(f"{etiqueta_a}: ")
    b = leer_numero(f"{etiqueta_b}: ")
    resultado = funcion(a, b)
    historial.append(
        f"{nombre}({formatear_numero(a)}, {formatear_numero(b)}) = "
        f"{formatear_numero(resultado)}"
    )
    print(f"Resultado: {formatear_numero(resultado)}")


def ejecutar_unaria(historial, nombre, funcion, etiqueta="Número"):
    """Solicita un número, calcula y registra una operación unaria."""
    print(f"\n--- {nombre} ---")
    numero = leer_numero(f"{etiqueta}: ")
    resultado = funcion(numero)
    historial.append(
        f"{nombre}({formatear_numero(numero)}) = {formatear_numero(resultado)}"
    )
    print(f"Resultado: {formatear_numero(resultado)}")


def mostrar_menu():
    """Muestra las operaciones disponibles."""
    print("\n" + "=" * 44)
    print("CALCULADORA EN PYTHON".center(44))
    print("=" * 44)
    print("Operaciones básicas")
    print("  1. Suma")
    print("  2. Resta")
    print("  3. Multiplicación")
    print("  4. División")
    print("Operaciones ampliadas")
    print("  5. Potencia")
    print("  6. Módulo")
    print("  7. Raíz cuadrada")
    print("  0. Salir")
    print("=" * 44)


def leer_opcion():
    """Solicita una opción del menú y devuelve un entero o None."""
    entrada = input("Selecciona una opción: ").strip()
    try:
        return int(entrada)
    except ValueError:
        return None


def main():
    """Ejecuta el ciclo principal de la calculadora."""
    historial = []
    print("Bienvenido a la calculadora. Escribe 0 para salir.")
    while True:
        try:
            mostrar_menu()
            opcion = leer_opcion()
            if opcion == 0:
                print("\nGracias por usar la calculadora. ¡Hasta pronto!")
                break
            if opcion == 1:
                ejecutar_binaria(
                    historial,
                    "Suma",
                    operaciones.suma,
                    "Primer número",
                    "Segundo número",
                )
            elif opcion == 2:
                ejecutar_binaria(
                    historial,
                    "Resta",
                    operaciones.resta,
                    "Primer número",
                    "Segundo número",
                )
            elif opcion == 3:
                ejecutar_binaria(
                    historial,
                    "Multiplicación",
                    operaciones.multiplicacion,
                    "Primer número",
                    "Segundo número",
                )
            elif opcion == 4:
                ejecutar_binaria(
                    historial,
                    "División",
                    operaciones.division,
                    "Dividendo",
                    "Divisor",
                )
            elif opcion == 5:
                ejecutar_binaria(
                    historial,
                    "Potencia",
                    operaciones.potencia,
                    "Base",
                    "Exponente",
                )
            elif opcion == 6:
                ejecutar_binaria(
                    historial,
                    "Módulo",
                    operaciones.modulo,
                    "Dividendo",
                    "Divisor",
                )
            elif opcion == 7:
                ejecutar_unaria(
                    historial,
                    "Raíz cuadrada",
                    operaciones.raiz_cuadrada,
                )
            else:
                print("\nOpción inválida. Elige un número del 0 al 7.")
        except (ValueError, ZeroDivisionError, TypeError, OverflowError) as error:
            print(f"\nError: {error}")
        except (KeyboardInterrupt, EOFError):
            print("\n\nSaliendo de la calculadora...")
            break


if __name__ == "__main__":
    main()
