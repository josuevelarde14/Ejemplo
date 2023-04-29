def buscar_palabra(lista, palabra):
    for i in range(len(lista)):
        if lista[i] == palabra:
            return i
    return -1
def buscar_palabra(lista, palabra):
    for i in range(len(lista)):
        if lista[i] == palabra:
            return i
    return -1

lista = input("Ingrese una lista de palabras separadas por comas: ").split(",")
palabra = input("Ingrese una palabra a buscar: ")

posicion = buscar_palabra(lista, palabra)

if posicion == -1:
    print("-1 La palabra no se encontró en la lista.")
else:
    print(f"La palabra se encontró en la posición {posicion} de la lista.")