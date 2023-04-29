def palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    if palabra == palabra[::-1]:
        return True
    else:
        return False

palabra = input("Ingrese una palabra o frase: ")
if palindromo(palabra):
    print(f"{palabra} es un palíndromo")
else:
    print(f"{palabra} no es un palíndromo")

