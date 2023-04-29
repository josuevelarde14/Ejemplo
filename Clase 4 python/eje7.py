print("Ingresa palabras separadas por comas")
palabras = input().split(',')

for p in palabras:
    print("Longitud de la palabra", p, "es ", len(p))
    