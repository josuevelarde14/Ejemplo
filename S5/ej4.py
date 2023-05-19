class triangulo:
    def __init__(self, altura, lado1, lado2, lado3):
        self.__base = lado1
        self.__lado2 = lado2
        self.__lado3 = lado3
        self.__altura = altura
        self.__area = 0
        self.__perimetro = 0
        self.__figura = "triangulo"

    def getArea(self):
        self.__area = self.__base = self.__altura / 2
        print(f"El area del {self.__figura} es: {self.__area}")

    def getPerimetro(self):
        self.__perimetro = self.__base + self.__lado2 + self.__lado3
        print(f"El perimetro del {self.__figura} es: {self.__perimetro}")

triangulo1 = triangulo(3,3,6,9)
triangulo1.getArea()
triangulo1.getPerimetro()
