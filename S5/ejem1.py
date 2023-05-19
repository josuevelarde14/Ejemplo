class pokemon:
    def __init__(self, especie, brazos, poderes, instrumentos):
        self.especie=especie
        self.brazos=brazos
        self.poderes=poderes
        self.instrumentos=instrumentos

    def evolucion(self, piedra=False, piedra2=False):
        print(self.especie)

        if (self.especie=="electrico"):
            return "Evoluciona a raichu"
        elif (piedra=="rayo" and piedra2=="agua"):
            return "Evoluciona a mewtwo"
        else:
            return "No es un pokemon registrado"
        
    def get(self):
        print(self.especie)

    def set(self,especie):
        self.especie = especie

picachu=pokemon("electrico",2,"velocidad","no tiene")
charmander=pokemon("fuego",2,"bola de fuego","no tiene")
volbasour=pokemon("agua",2,"chorro de agua","no tiene")

print(f"picachu tiene {picachu.brazos} brazos")

print(f"Charmander es tipo {charmander.especie}")

print(picachu.evolucion())

print(charmander.evolucion("rayo","agua"))

print(volbasour.evolucion())



