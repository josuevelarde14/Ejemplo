print("Ingresa un numero")
numero = int(input())

print("Numeros impares entre 1 y el numero", numero)
for n in range(1, numero):
    if n%2 != 0:
        print(n)