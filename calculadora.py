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


def leer_entero(mensaje, minimo=None):
    """Solicita un número entero y repite hasta recibir una entrada válida."""
    while True:
        entrada = input(mensaje).strip()
        try:
            numero = int(entrada)
        except ValueError:
            print("Entrada inválida. Ingresa un número entero.")
            continue
        if minimo is not None and numero < minimo:
            print(f"El número debe ser mayor o igual que {minimo}.")
            continue
        return numero


def leer_lista_numeros(mensaje):
    """Solicita varios números separados por espacios o punto y coma."""
    while True:
        entrada = input(mensaje).strip()
        if not entrada:
            print("Ingresa al menos un número.")
            continue
        partes = entrada.replace(";", " ").split()
        try:
            return [float(parte.replace(",", ".")) for parte in partes]
        except ValueError:
            print("Entrada inválida. Separa los números con espacios o punto y coma.")


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


def ejecutar_factorial(historial):
    """Solicita un entero no negativo y calcula su factorial."""
    print("\n--- Factorial ---")
    numero = leer_entero("Número entero no negativo: ", minimo=0)
    resultado = operaciones.factorial(numero)
    historial.append(f"Factorial({numero}) = {resultado}")
    print(f"Resultado: {resultado}")


def ejecutar_promedio(historial):
    """Solicita varios números y calcula su promedio."""
    print("\n--- Promedio ---")
    numeros = leer_lista_numeros("Números separados por espacios o punto y coma: ")
    resultado = operaciones.promedio(numeros)
    lista = ", ".join(formatear_numero(numero) for numero in numeros)
    historial.append(f"Promedio([{lista}]) = {formatear_numero(resultado)}")
    print(f"Resultado: {formatear_numero(resultado)}")


def ejecutar_redondeo(historial):
    """Solicita un número y la cantidad de decimales para redondearlo."""
    print("\n--- Redondeo ---")
    numero = leer_numero("Número a redondear: ")
    decimales = leer_entero("Cantidad de decimales: ", minimo=0)
    resultado = operaciones.redondear(numero, decimales)
    historial.append(
        f"Redondeo({formatear_numero(numero)}, {decimales}) = "
        f"{formatear_numero(resultado)}"
    )
    print(f"Resultado: {formatear_numero(resultado)}")


def mostrar_historial(historial):
    """Muestra las operaciones registradas durante la ejecución."""
    print("\n--- Historial de operaciones ---")
    if not historial:
        print("El historial está vacío.")
        return
    for indice, operacion in enumerate(historial, start=1):
        print(f"{indice}. {operacion}")


def limpiar_historial(historial):
    """Elimina todas las operaciones del historial."""
    if not historial:
        print("\nEl historial ya está vacío.")
        return
    historial.clear()
    print("\nHistorial eliminado correctamente.")


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
    print("  8. Porcentaje")
    print("  9. Valor absoluto")
    print(" 10. Factorial")
    print(" 11. Promedio")
    print(" 12. Redondeo")
    print("Historial")
    print(" 13. Ver historial")
    print(" 14. Limpiar historial")
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
            elif opcion == 8:
                ejecutar_binaria(
                    historial,
                    "Porcentaje",
                    operaciones.porcentaje,
                    "Cantidad",
                    "Porcentaje (%)",
                )
            elif opcion == 9:
                ejecutar_unaria(
                    historial,
                    "Valor absoluto",
                    operaciones.valor_absoluto,
                )
            elif opcion == 10:
                ejecutar_factorial(historial)
            elif opcion == 11:
                ejecutar_promedio(historial)
            elif opcion == 12:
                ejecutar_redondeo(historial)
            elif opcion == 13:
                mostrar_historial(historial)
            elif opcion == 14:
                limpiar_historial(historial)
            else:
                print("\nOpción inválida. Elige un número del 0 al 14.")
        except (ValueError, ZeroDivisionError, TypeError, OverflowError) as error:
            print(f"\nError: {error}")
        except (KeyboardInterrupt, EOFError):
            print("\n\nSaliendo de la calculadora...")
            break


if __name__ == "__main__":
    main()
