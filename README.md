# Fundamentos de Python - Laboratorios y Ejercicios

## Descripción

Este repositorio contiene el desarrollo de los laboratorios y ejercicios propuestos durante el aprendizaje de los fundamentos de Python. En cada actividad se aplican conceptos básicos del lenguaje como la función `print()`, variables, operadores aritméticos, conversión de unidades y evaluación de expresiones matemáticas.

El propósito de este proyecto es fortalecer la lógica de programación y familiarizarse con la sintaxis de Python mediante ejercicios prácticos.

---

# Contenido del proyecto

| Archivo | Descripción |
|---------|-------------|
| `hola_mundo.py` | Primer programa utilizando la función `print()`. |
| `print_sep_end.py` | Uso de los parámetros `sep` y `end` en la función `print()`. |
| `flecha.py` | Ejercicio de impresión de figuras utilizando `print()` y `\n`. |
| `escape.py` | Uso de caracteres de escape (`\"`) para imprimir comillas. |
| `operadores.md` | Desarrollo manual de los ejercicios de operadores matemáticos. |
| `operadores.py` | Verificación de los ejercicios de operadores utilizando Python. |
| `manzanas.py` | Uso de variables y operaciones aritméticas con el problema de las manzanas. |
| `conversion.py` | Conversión entre millas y kilómetros. |
| `expresion.py` | Evaluación de una expresión algebraica en Python. |
| `README.md` | Documentación del proyecto. |

---

# Ejercicio 1 - Hola Mundo

## Objetivo

Aprender a utilizar la función `print()` para mostrar información en pantalla.

## Conceptos aprendidos

- Función `print()`
- Uso de cadenas de texto.
- Comillas simples y dobles.
- Errores de sintaxis.

### Código

```python
print("¡Hola, Mundo!")
print("Jhon Harold Andres Sanchez Criollo")
```

---

# Ejercicio 2 - Uso de sep y end

## Objetivo

Comprender el funcionamiento de los parámetros `sep` y `end` de la función `print()`.

### Código

```python
print("Aprendiendo", "Python", "es", sep=" - ", end=" => ")
print("divertido")
```

### Resultado

```
Aprendiendo - Python - es => divertido
```

---

# Ejercicio 3 - Impresión de una flecha

## Objetivo

Practicar el uso de la función `print()`, los saltos de línea (`\n`) y la impresión de figuras.

### Código

```python
print(
"    *          *\n"
"   * *        * *\n"
"  *   *      *   *\n"
" *     *    *     *\n"
"***   ***  ***   ***\n"
"  *   *      *   *\n"
"  *   *      *   *\n"
"  *****      *****"
)
```

---

# Ejercicio 4 - Caracteres de escape

## Objetivo

Aprender a utilizar caracteres de escape para imprimir comillas.

### Código

```python
print("\"Estoy\"\"\"aprendiendo\"\"\"\"\"Python\"\"\"")
```

### Resultado

```
"Estoy"""aprendiendo"""""Python"""
```

---

# Ejercicio 5 - Operadores Matemáticos

## Objetivo

Resolver expresiones matemáticas manualmente y comprobar los resultados utilizando Python.

## Operadores utilizados

| Operador | Descripción |
|-----------|-------------|
| + | Suma |
| - | Resta |
| * | Multiplicación |
| / | División |
| // | División entera |
| % | Módulo |
| ** | Potencia |

Cada ejercicio fue resuelto respetando el orden de precedencia de los operadores:

1. Paréntesis.
2. Potencias.
3. Multiplicación, división y módulo.
4. Suma y resta.

Los resultados fueron documentados en el archivo `operadores.md` y posteriormente comprobados mediante `operadores.py`.

---

# Ejercicio 6 - Variables (Las Manzanas)

## Objetivo

Aprender a crear variables y realizar operaciones aritméticas.

### Código

```python
john = 3
mary = 5
adam = 6

print(john, mary, adam, sep=", ")

total_apples = john + mary + adam

print("Número total de manzanas:", total_apples)
```

### Resultado

```
3, 5, 6
Número total de manzanas: 14
```

En este ejercicio también se realizaron pruebas con nuevas variables utilizando:

- suma
- resta
- multiplicación
- división
- división entera
- módulo
- potencia

---

# Ejercicio 7 - Conversión de millas y kilómetros

## Objetivo

Aplicar operaciones matemáticas utilizando variables.

### Código

```python
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")
```

### Resultado

```
7.38 millas son 11.88 kilómetros
12.25 kilómetros son 7.61 millas
```

En este laboratorio se aprendió el uso de:

- Variables.
- Operaciones aritméticas.
- Función `round()`.
- Conversión de unidades.

---

# Ejercicio 8 - Evaluación de una expresión matemática

## Objetivo

Resolver una expresión algebraica utilizando operadores matemáticos.

La expresión utilizada fue:

```
3x³ - 2x² + 3x - 1
```

### Código

```python
x = float(input("Ingrese el valor de x: "))

y = 3 * x**3 - 2 * x**2 + 3 * x - 1

print("y =", y)
```

### Pruebas realizadas

| x | Resultado |
|---|-----------|
| 0 | -1.0 |
| 1 | 3.0 |
| -1 | -9.0 |

---
Reto 1 - Calculadora de Métricas del Desarrollador
Objetivo

Desarrollar un programa que registre las horas dedicadas por un desarrollador a cada uno de sus proyectos y genere un reporte con estadísticas de trabajo.

Temas aplicados
Entrada y salida de datos.
Variables.
Conversión de datos.
Listas.
Ciclos for.
Función sum().
Formato de salida con f-strings.
Funcionalidades
Solicita el nombre del desarrollador.
Solicita la cantidad de proyectos.
Registra las horas de cada proyecto.
Calcula el total de horas trabajadas.
Calcula el promedio de horas por proyecto.
Calcula el porcentaje de horas por proyecto.
Presenta un reporte tabulado.


Reto 2 - Sistema Simplificado de Calificación e Inventario
Objetivo

Clasificar el estado del inventario de un almacén informático mediante listas y estructuras condicionales.

Temas aplicados
Listas.
Condicionales (if, elif y else).
Ciclos for.
enumerate().
Operaciones matemáticas.
Funcionalidades
Recorre una lista de inventario.
Clasifica cada producto como:
Adecuado.
Crítico.
Agotado.
Genera la lista de productos agotados.
Genera la lista de productos críticos.
Calcula el porcentaje de disponibilidad del inventario.


Reto 3 - Motor de Análisis de Frecuencia de Texto
Objetivo

Analizar un texto ingresado por el usuario para determinar la frecuencia de aparición de cada palabra.

Temas aplicados
Cadenas de texto.
Diccionarios.
Bucles.
Métodos de cadenas.
Conteo de palabras.
Funcionalidades
Solicita una frase o párrafo.
Convierte el texto a minúsculas.
Elimina signos de puntuación básicos.
Cuenta la frecuencia de cada palabra.
Identifica la palabra con mayor número de apariciones.
Muestra el diccionario de frecuencias.

# ¿Cómo ejecutar los programas?

## Requisitos

Tener instalado Python 3.

Comprobar la instalación:

```bash
python --version
```

o

```bash
python3 --version
```

---

## Ejecutar un archivo

Desde la terminal, ubicarse en la carpeta del proyecto y ejecutar:

```bash
python nombre_del_archivo.py
```

Ejemplos:

```bash
python hola_mundo.py
```

```bash
python operadores.py
```

```bash
python conversion.py
```

```bash
python expresion.py
```

---

# Conocimientos adquiridos

Durante el desarrollo de estos laboratorios se aprendieron los siguientes conceptos:

- Sintaxis básica de Python.
- Función `print()`.
- Parámetros `sep` y `end`.
- Caracteres de escape.
- Variables.
- Tipos de datos.
- Operadores matemáticos.
- Prioridad de operadores.
- Función `round()`.
- Conversión de tipos mediante `float()`.
- Conversión de unidades.
- Evaluación de expresiones algebraicas.
- Listas.
- Diccionarios.
- Ciclos for.
- Condicionales (if, elif, else).
- Función enumerate().
- Función sum().
- Métodos para manipular cadenas.
- Formato de salida mediante f-strings.
- Resolución de problemas mediante algoritmos.

---

# Conclusiones

El desarrollo de estos ejercicios permitió comprender los fundamentos de Python y reforzar la lógica de programación mediante la práctica. Se aprendió a utilizar variables, operadores aritméticos, funciones básicas y estructuras simples del lenguaje, comprobando cada resultado con programas ejecutados en Python. Estas actividades constituyen una base sólida para continuar con temas más avanzados del lenguaje.

---

# Autor

**Jhon Harold Andres Sanchez Criollo**

**Análisis y Desarrollo de Software (ADSO) – SENA**

**2026**# python-
