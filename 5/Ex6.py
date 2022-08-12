
materias = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
pasadas = []

for materia in materias:
    nota = int(input("Que nota tienes en " + materia + "?: "))
    if nota >= 7:
        pasadas.append(materia)
for x in pasadas:
    materias.remove(x)

print("El estudiante tiene que repetir: " + str(materias))







