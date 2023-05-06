#Objetos
#class pokemon:
#    def __init__(self,especie, brazos, poderes, instrumentos) -> None: #contructor, el objeto siempre tiene que tener un init
#        self.esp1=especie
#        self.bra1=brazos
#        self.pod1=poderes
#        self.instrumentos=instrumentos
#        pass

#Objetos
class pokemon:
    def __init__(self,especie, brazos, poderes, instrumentos) -> None: #contructor, el objeto siempre tiene que tener un init
        self.especie=especie
        self.brazos=brazos
        self.poderes=poderes
        self.instrumentos=instrumentos
        pass

    def evolucion(self, piedra="", piedra2=""):
        print(self.especie)
        if(self.especie=="electrico"):
            return "Evoluciona en raichu"
        elif(piedra=="rayo" and piedra2=="agua"): #else if
            return "evaluciona newtwo"
        else:
            return "es un perrito"
        
    def get(self): #obtener 
        print(self.especie)

    def set(self, especie): #sobre editar valores ya definidos por el constructor
        self.especie=especie

pikachu=pokemon("electrico",2,"velocidad","no tiene") # pikachu se esta convirtiendo en un dato complejo
charmander=pokemon("fuego",2,"bala de fuego","no tiene")

print(f"pikachu tiene {pikachu.brazos} brazos")
print(f"charmander es tipo {charmander.especie}")

print(pikachu.evolucion())
print(pikachu.evolucion("rayo","agua"))
pikachu

