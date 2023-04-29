print("Ingresa una frase")
frase = input()
cantidad_vocales = 0
for l in frase:
    if l in "aeiou":
        cantidad_vocales += 1

    print("la frase",frase, f"tiene{cantidad_vocales} vocales")
