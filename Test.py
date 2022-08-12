while True:
    t = input("Ingrese el nombre del trabajor: ")
    worked_hours = float(input("Cuantas horas trabajo?: "))
    value_hours = float(input("Cuanto cuesta cada hora?: "))
    sueldo = worked_hours * value_hours

    if sueldo < 200:
        discount = 0.03
    elif 200 < sueldo < 400:
        discount = 0.05
    elif 401 < sueldo < 600:
        discount = 0.07
    elif 601 < sueldo < 800:
        discount = 0.1
    elif sueldo > 800:
        discount = 0.12

    neto = (sueldo - (sueldo * discount))

    print(t, sueldo, sueldo * discount, neto)

    validation = input("Tiene otro trabajador? (Y/N): ")

    if validation == "Y":
        continue
    elif validation == "N":
        print("Eso es todo, vuelva pronto")
        break
