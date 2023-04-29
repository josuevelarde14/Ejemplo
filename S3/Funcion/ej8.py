def listaMod3 (lista):
    lista3 = []
    for n in lista:
        if n%3 == 0:
            lista3.append(n)
        print(lista3)

lista1 = [9,8,7,6,5,4,3]
lista2 = range(1,100)

listaMod3(lista1)
