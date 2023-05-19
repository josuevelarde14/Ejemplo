import math
class circulo:
    def __init__(self, radio):
        self.__radio=radio
        self.__area = 0
        self.__perimetro = 0
        self.__figura = "circulo"

    def getArea(self):
        self.__area = math.pi * self.__radio ** 2
        print(f"El area del {self.__figura} es: {self.__area}")

    def getPerimetro(self):
        self.__perimetro = 2 * math.pi * self.__radio
        print(f"El perimetro del {self.__figura} es: {self.__perimetro}")

circulo1 = circulo(3)
circulo1.getArea()
circulo1.getPerimetro()
