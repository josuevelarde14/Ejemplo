print("Ingresa un numero 1")
num1 = int(input())

print("Ingresa un numero 2")
num2 = int(input())

if num1 > num2:
    print(f"El numero {num1} es mayor")
elif num2>num1:
    print(f"El numero {num2} es mayor")
else:
    print("Los numeros son iguales")