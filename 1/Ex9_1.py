print("Procederemos a calcular el capital obtenido por una inversion\n")

c = float(input("Ingrese la cantidad a invertir\n"))
i = float(input("Ingrese el interes anual\n"))
t = int(input("Ingrese el numero de años\n"))


print("Su capital obtenido en la inversión es de " + str(c*(1+i)**t))