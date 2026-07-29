# Solicitar datos del desarrollador
nombre = input("Ingrese el nombre del desarrollador: ")
cantidad_proyectos = int(input("Ingrese la cantidad de proyectos asignados: "))

# Lista para almacenar las horas de cada proyecto
horas_proyectos = []

# Solicitar las horas de cada proyecto
for i in range(cantidad_proyectos):
    horas = float(input(f"Ingrese las horas dedicadas al proyecto {i + 1}: "))
    horas_proyectos.append(horas)

# Calcular métricas
total_horas = sum(horas_proyectos)
promedio_horas = total_horas / cantidad_proyectos

# Mostrar reporte
print("\n" + "=" * 60)
print(f"Reporte de trabajo del desarrollador: {nombre}")
print("=" * 60)
print(f"{'Proyecto':<12}{'Horas':<12}{'% del Total':<15}")
print("-" * 60)

for i, horas in enumerate(horas_proyectos):
    porcentaje = (horas / total_horas) * 100
    print(f"{i + 1:<12}{horas:<12.2f}{porcentaje:<15.2f}")

print("-" * 60)
print(f"Total de horas: {total_horas:.2f}")
print(f"Promedio por proyecto: {promedio_horas:.2f}")