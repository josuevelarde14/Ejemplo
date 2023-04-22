numbers_str = input("Escribe una secuencia de numeros separados por coma: ").split(',')
number = [int(x) for x in numbers_str]
print(number)
mayor = 0 
menor = 0
mayor = max(number)
menor = min(number)
print(sum(number))
print("Mayor: ", mayor)
print("Menor: ", menor)
