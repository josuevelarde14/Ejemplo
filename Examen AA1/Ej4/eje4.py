def positivo_negativo_cero(num):
    if num > 0:
        print("El número es positivo.")
    elif num < 0:
        print("El número es negativo.")
    else:
        print("El número es cero.")

while True:
    num = float(input("Ingresa un número: "))
    positivo_negativo_cero(num)
    otro_num = input("¿Deseas ingresar otro número? responde solo S si es que si o N si es que NO): ")
    if otro_num.lower() != "s":
        break