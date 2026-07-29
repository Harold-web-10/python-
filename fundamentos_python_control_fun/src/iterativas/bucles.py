# Solicitar texto
texto = input("Ingrese una frase o parrafo: ")

# Convertir a minusculas
texto = texto.lower()

# Eliminar signos de puntuacion basicos
for signo in [",", ".", ";", "!", "?", ":"]:
    texto = texto.replace(signo, "")

# Separar palabras
palabras = texto.split()

# Crear diccionario de frecuencias
frecuencias = {}

for palabra in palabras:
    if palabra in frecuencias:
        frecuencias[palabra] += 1
    else:
        frecuencias[palabra] = 1

# Buscar la palabra mas frecuente
palabra_mas_frecuente = ""
mayor = 0

for palabra, cantidad in frecuencias.items():
    if cantidad > mayor:
        mayor = cantidad
        palabra_mas_frecuente = palabra

# Mostrar resultados
print("\nFrecuencia de palabras")

for palabra, cantidad in frecuencias.items():
    print(f"{palabra}: {cantidad}")

print(f"\nLa palabra mas frecuente es '{palabra_mas_frecuente}' con {mayor} apariciones.")