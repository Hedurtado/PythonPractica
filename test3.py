# Bloque de variables globales para uso posterior
n = 1
sum_average = 0
general_average = 0
sobresaliente = 0
muy_bueno = 0
bueno = 0
regular = 0
insuficiente = 0

students = int(input("Cuantos estudiantes desea calcular su notas parciales?: "))

if n <= students:  # condicional en caso de que se pase de estudiantes que dijo que iba a ingresar para salir del programa
    while n <= students:  # para romper el bucle
        n += 1  # cada vez que se repita se sume 1
        name = input("Ingrese el nombre del estudiante: ")
        assign = input("Ingrese el nombre de la asignatura: ")
        note1 = int(input("Ingrese la primera nota parcial: "))
        note2 = int(input("Ingrese la segunda nota parcial: "))
        note3 = int(input("Ingrese la tercera nota parcial: "))
        average = round((note1 + note2 + note3) / 3)  # promedio

        # Bloque condicional para saber en que promedio encaja el estudiante #
        if average == 10:
            sobresaliente += 1
            print(name.capitalize(), ' en ', assign.capitalize(),
                  ' tiene un promedio igual a 10, SOBRESALIENTE')
        elif average == 8 or average == 9:
            muy_bueno += 1
            print(name.capitalize(), ' en ', assign.capitalize(),
                  ' tiene un promedio igual a 8 o 9, MUY BUENO')
        elif average == 7:
            bueno += 1
            print(name.capitalize(), ' en ', assign.capitalize(),
                  ' tiene un promedio igual a 7, BUENO')
        elif average == 5 or average == 6:
            regular += 1
            print(name.capitalize(), ' en ', assign.capitalize(),
                  ' tiene un promedio igual a 5 o 6, REGULAR')
        elif average < 5:
            insuficiente += 1
            print(name.capitalize(), ' en ', assign.capitalize(),
                  ' tiene un promedio menor que 5, INSUFICIENTE')
        sum_average += average

        # Bloque de validacion | en caso de que desee salir antes del programa
        validation = input("Desea seguir sacando promedio de sus estudiantes? (Y,N): ")

        if validation == "Y" or validation == 'y':
            continue
        elif validation == 'N' or validation == 'n':
            break
    else:
        print("Se procedera a calcular el promedio general del curso en ", assign)

    # Bloque para dar a conocer el promedio general y cantidad de estudiantes en cada promedio
general_average = round(sum_average / n)
print("El promedio general del curso es de: ", general_average, ' en ', assign)
print("El numero de estudiantes con notas SOBRESALIENTE: ", sobresaliente,
      '\n El numero de estudiantes con notas MUY BUENO: ', muy_bueno,
      '\n El numero de estudiantes con notas BUENO: ', bueno,
      '\n El numero de estudiantes con notas REGULAR: ', regular,
      '\n El numero de estudiantes con notas INSUFICIENTES: ', insuficiente)
