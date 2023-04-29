print("Ingresa dos numeros separados por coma")
numeros = input().split(',')
num1 = int(numeros[0])
num2 = int(numeros[1])

print(f"Numeros pares entre {num1} y {num2}")
for n in range(num1, num2):
    if n%2 == 0:
        print(n)