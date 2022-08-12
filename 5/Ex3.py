
materias = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
notas = []

for materia in materias:
    nota = input("Que nota ha sacado en " + materia + "? ")
    notas.append(nota)
for i in range(len(notas)):
    print("En ", materias[i], " has sacado ", notas[i])
