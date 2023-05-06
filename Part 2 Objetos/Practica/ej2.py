class Circulo:
    def __init__(self,radio) -> None: #contructor, el objeto siempre tiene que tener un init
        self.radio=radio
        pass
    def operacion(self, areaoperimetro=""):
        print(f"operacion de radio {self.radio}")
        if(areaoperimetro=="area"):
            print(f"el area es {self.radio*self.radio*self.radio*3.1416}") 
        elif(areaoperimetro=="perimetro"): #else if
            print(f"el perimetro es {self.radio*2*3.1416}")
        else:
            return "Error"
        
    #def get(self): #obtener 
    #    print(self.especie)

    #def set(self, especie): #sobre editar valores ya definidos por el constructor
    #    self.especie=especie

op1=Circulo(3) 
op2=Circulo(4)

print(op1.operacion("area"))
print(op2.operacion("perimetro"))