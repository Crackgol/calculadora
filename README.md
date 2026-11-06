# Calculadora en Python

Calculadora de consola desarrollada en Python como parte de la Práctica 2 de la materia SIS2420B. El proyecto amplía una calculadora básica con nuevas operaciones matemáticas, validación de entradas, historial de operaciones y documentación.

## Descripción

La calculadora permite realizar operaciones básicas y ampliadas desde un menú interactivo. El programa valida las entradas del usuario, evita errores como la división entre cero, permite repetir operaciones sin reiniciar la aplicación y mantiene un historial de las operaciones exitosas durante la ejecución.

## Operaciones y estado

| N.º | Funcionalidad | Descripción | Estado |
| --- | --- | --- | --- |
| 1 | Potencia | Calcula una base elevada a un exponente. | Completada |
| 2 | Módulo | Obtiene el residuo de una división. | Completada |
| 3 | Raíz cuadrada | Calcula la raíz cuadrada y rechaza valores negativos. | Completada |
| 4 | Porcentaje | Calcula un porcentaje de una cantidad. | Completada |
| 5 | Valor absoluto | Obtiene el valor absoluto de un número. | Completada |
| 6 | Factorial | Calcula el factorial de un entero no negativo. | Completada |
| 7 | Promedio | Calcula el promedio de varios números. | Completada |
| 8 | Redondeo | Redondea un número a la cantidad de decimales indicada. | Completada |
| 9 | Validación de entradas | Controla entradas no numéricas y valores vacíos. | Completada |
| 10 | División por cero | Evita divisiones y módulos con divisor cero. | Completada |
| 11 | Mejorar el menú | Organiza las operaciones en un menú claro. | Completada |
| 12 | Repetir operaciones | Permite realizar varias operaciones sin reiniciar. | Completada |
| 13 | Historial de operaciones | Almacena y muestra las operaciones realizadas. | Completada |
| 14 | Limpiar historial | Permite borrar el historial de operaciones. | Completada |
| 15 | Mejorar documentación | Incluye descripción, tabla, ejemplos de uso y autor. | Completada |

### Operaciones básicas

| Opción | Operación |
| --- | --- |
| 1 | Suma |
| 2 | Resta |
| 3 | Multiplicación |
| 4 | División |

### Menú del programa

```text
1. Suma
2. Resta
3. Multiplicación
4. División
5. Potencia
6. Módulo
7. Raíz cuadrada
8. Porcentaje
9. Valor absoluto
10. Factorial
11. Promedio
12. Redondeo
13. Ver historial
14. Limpiar historial
0. Salir
```

## Tecnologías

- Python 3.10 o superior
- Git
- GitHub Issues
- Markdown

## Instalación y ejecución

1. Clona el repositorio:

```bash
git clone https://github.com/Crackgol/calculadora.git
```

2. Ingresa a la carpeta del proyecto:

```bash
cd calculadora
```

3. Ejecuta el programa:

```bash
python3 calculadora.py
```

El proyecto utiliza únicamente la biblioteca estándar de Python, por lo que no requiere instalar dependencias adicionales.

## Ejemplos de uso

### Potencia

```text
Selecciona una opción: 5

--- Potencia ---
Base: 2
Exponente: 10
Resultado: 1024
```

### Porcentaje

```text
Selecciona una opción: 8

--- Porcentaje ---
Cantidad: 200
Porcentaje (%): 15
Resultado: 30
```

### Promedio

```text
Selecciona una opción: 11

--- Promedio ---
Números separados por espacios o punto y coma: 10 20 30
Resultado: 20
```

### Redondeo

```text
Selecciona una opción: 12

--- Redondeo ---
Número a redondear: 3.14159
Cantidad de decimales: 2
Resultado: 3.14
```

### Historial

```text
Selecciona una opción: 13

--- Historial de operaciones ---
1. Potencia(2, 10) = 1024
2. Porcentaje(200, 15) = 30
3. Promedio([10, 20, 30]) = 20
```

### Limpiar historial

```text
Selecciona una opción: 14

Historial eliminado correctamente.
```

### Validación de entradas

```text
Selecciona una opción: abc

Opción inválida. Elige un número del 0 al 14.
```

## Validaciones implementadas

- Entradas no numéricas en números y opciones del menú.
- Números negativos en la raíz cuadrada.
- Números negativos o no enteros en el factorial.
- División entre cero y módulo con divisor cero.
- Cantidad de decimales negativa en el redondeo.
- Lista vacía en el cálculo del promedio.
- Opciones del menú fuera de rango.

## Estructura del proyecto

```text
calculadora/
├── README.md
├── calculadora.py
└── operaciones.py
```

| Archivo | Responsabilidad |
| --- | --- |
| `calculadora.py` | Muestra el menú, solicita datos, valida entradas, muestra resultados y controla el historial y la repetición. |
| `operaciones.py` | Contiene las funciones matemáticas y sus validaciones. |

## Organización del trabajo

Las tareas se organizaron mediante 15 Issues en GitHub, una por cada funcionalidad obligatoria y adicional. Cada Issue incluye descripción, lista de tareas, criterios de aceptación y asignación al estudiante. Los avances se registraron con commits descriptivos y se cerraron las Issues a medida que cada funcionalidad quedó implementada y probada.

## Autor

Crackgol
