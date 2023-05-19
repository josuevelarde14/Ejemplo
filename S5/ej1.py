class rectangulo:
    def __init__(self, base, altura):
        self.__base=base
        self.__altura=altura
        self.__area= 0
        self.__perimetro = 0

    def getArea(self):
        self.__area=self.__base * self.__altura
        print(f"El area del rectangulo es: {self.__area}")
    def getPerimetro(self):
        self.__perimetro = 2*(self.__base + self.__altura)
        print(f"El perimetor del rectangulo es: {self.__perimetro}")
    
rectangulo1 = rectangulo(10,20)
rectangulo1.getArea()
rectangulo1.getPerimetro()
