print("Ingresa numeros separados por comas")
numeros = input().split(',')
suma = 0
for n in numeros:
    suma += int(n)

print(f"La suma de los numeros es igual a {suma}")
