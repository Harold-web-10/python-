# Lista de stock
stock = [12, 0, 5, 23, 2, 0, 8]

# Listas solicitadas
productos_agotados = []
total_criticos = []

print("Estado del inventario\n")

# Clasificar cada producto
for indice, cantidad in enumerate(stock):

    if cantidad == 0:
        print(f"Producto {indice}: Agotado - Reorden Inmediata")
        productos_agotados.append(indice)

    elif 1 <= cantidad <= 5:
        print(f"Producto {indice}: Critico - Reposicion Sugerida")
        total_criticos.append(cantidad)

    else:
        print(f"Producto {indice}: Adecuado")

# Calcular disponibilidad
productos_disponibles = len(stock) - len(productos_agotados)
porcentaje = (productos_disponibles / len(stock)) * 100

print("\nResultados")
print("Productos agotados (indices):", productos_agotados)
print("Stock critico:", total_criticos)
print(f"Disponibilidad general: {porcentaje:.2f}%")