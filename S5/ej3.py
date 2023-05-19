class cuadrado:
    def __init__(self, lado):
        self.__lado=lado
        self.__area = 0
        self.__perimetro = 0
        self.__figura = "cuadrado"

    def getArea(self):
        self.__area = self.__lado ** 2
        print(f"El area del {self.__figura} es: {self.__area}")

    def getPerimetro(self):
        self.__perimetro = 4 * self.__lado
        print(f"El perimetro del {self.__figura} es: {self.__perimetro}")

cuadrado1 = cuadrado(3)
cuadrado1.getArea()
cuadrado1.getPerimetro()
