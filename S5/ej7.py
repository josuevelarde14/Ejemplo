class coche:
    def __init__(self, marca, modelo, velocidad):
        self.__marca = marca
        self.__modelo = modelo
        self.__velocidad = velocidad

    def acelerar(self):
        print(f"Acelerando")

    def frenar(self):
        print(f"Frenando")

coche1 = coche("VW","Gol","90km/h")
coche1.acelerar()
coche1.frenar()