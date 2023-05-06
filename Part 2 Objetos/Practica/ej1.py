class rectangulo:
    def __init__(self,base, altura) -> None: #contructor, el objeto siempre tiene que tener un init
        self.base=base
        self.altura=altura
        pass
    def operacion(self, areaoperimetro=""):
        print(f"operacion de base {self.base} y altura {self.altura}")
        if(areaoperimetro=="area"):
            return self.base*self.altura
        elif(areaoperimetro=="perimetro"): #else if
            return self.base+self.base+self.altura+self.altura
        else:
            return "Error"
        
    #def get(self): #obtener 
    #    print(self.especie)

    #def set(self, especie): #sobre editar valores ya definidos por el constructor
    #    self.especie=especie

op1=rectangulo(3,2) 
op2=rectangulo(4,9)

print(op1.operacion("area"))
print(op2.operacion("perimetro"))