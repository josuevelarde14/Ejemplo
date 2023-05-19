import os

current_directory = os.getcwd()

print(current_directory)

def calcular_total(archivo):
    total = 0
    with open(archivo, "r") as f:
        for linea in f:
            producto, precio = linea.strip().split(",")
            total += float(precio)
    return total

archivo ="S4_Proy/lista_compras.txt"
total_compra = calcular_total(archivo)
print(f"el total de la compra es: {total_compra}")
