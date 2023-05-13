archivo=open("./S8/Practica/ej1/datos.txt","w") #"w" para escribir

archivo.write("6    zanahoria\n")
archivo.write("7    fideos\n")
archivo.write("8    camote\n")

archivo.close()

archivo=open("./S8/Practica/ej1/datos.txt","r")
contenido=archivo.read()
print(contenido)
archivo.close()

