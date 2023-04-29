def numMayor(lista):
    max_val = -1
    for num in lista:
        if num > max_val:
            max_val = num
            res = num
    print(res)

lista1 = [555,232,66,123]
numMayor(lista1)