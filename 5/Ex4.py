
lotes = []

n = 1
number = int(input("Cuantos numeros tiene su loteria primivita?: "))

while n <= number:
    n += 1
    lote = input("Ingrese los numeros de la loteria primitiva uno por uno: ")
    lotes.append(lote)
    lotes.sort()

print(lotes)
