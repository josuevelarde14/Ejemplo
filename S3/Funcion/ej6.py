def cadmaslarga(lista):
    max_len = -1
    for cad in lista:
        if len(cad) > max_len:
            max_len = len(cad)
            res = cad
    print(res)

lista1= ["josuee","diegoooo","roman"]

cadmaslarga(lista1)