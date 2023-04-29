print("Ingresa tu edad")
edad = int(input())
if edad >= 18 and edad < 60:
    print("Eres mayor edad pero no jubilado")
elif edad >= 18 and edad >= 60:
    print("Eres jubilado")
else:
    print("Eres menor")