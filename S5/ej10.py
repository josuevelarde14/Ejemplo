class banco:
    def __init__(self, listaCuenta):
        self.__listaCuenta = listaCuenta

    def listarCuentas(self):
        i=1
        for cuenta in self.__listaCuenta:
            print(f"{i}.- {cuenta}")
            i+=1

    def agregaCuenta(self, cuenta=""):
        self.__listaCuenta.append(cuenta)
        print(f"Cuenta {cuenta} agregada correctamente")

    def borraCuenta(self,cuenta=""):
        self.__listaCuenta.remove(cuenta)
        print(f"Cuenta {cuenta} eliminada correctamente")

banco1 = banco(["333","666","999","1234567890"])
banco1.listarCuentas()
banco1.agregaCuenta("9669933")
banco1.borraCuenta("333")
banco1.listarCuentas()

