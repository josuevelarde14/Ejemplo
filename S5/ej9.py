class cuenta:
    def __init__(self, numerocuenta, importe=0):
        self.__numerocuenta = numerocuenta
        self.__saldo = importe 

    def depositar(self,importe=0):
        self.__saldo += importe
        self.saldo()

    def retirar(self,importe=0):
        self.__saldo -= importe
        self.saldo()

    def saldo(self):
        print(f"El saldo en su cuenta {self.__numerocuenta} es: {self.__saldo}")

cuenta1 = cuenta("123456789",300)
cuenta1.depositar(600)
cuenta1.retirar(900)
