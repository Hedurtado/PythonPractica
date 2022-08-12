print("Vamos a calcular su indice de masa corporal\n")

kg = float(input("Introduzca su peso en Kg\n"))
h = float(input("Introduzca su altura en metros\n"))

imc = round(kg/h**2, 2
)

print("Tu indice de masa corporal es ", imc)