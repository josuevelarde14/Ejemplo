peso = float(input("Ingrese su peso en kilogramos:"))
altura = float(input("Ingrese su altura en metros:"))
imc = peso / altura ** 2
print("Su IMC es: ",imc)

if imc<18.5:
    print("Peso Insuficiente")
elif imc<25:
    print("Peso Saludable")
elif imc<30:
    print("Sobrepeso")
else:
    print("Obesidad")