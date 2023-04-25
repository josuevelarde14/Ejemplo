def esprimo (num):
    for n in range(2, num):
        if num % n == 0:
            print("No es primo" , n, "es divisor")
            return False
        print("Es primo")
        return True
    
print("Ingresa un numero")
numero = int(input())
esprimo(numero)
