# Una panadería vende barras de pan a 3.49€ cada una.
# El pan que no es el día tiene un descuento del 60%.
# Escribir un programa que comience leyendo el número
# de barras vendidas que no son del día. Después el programa
# debe mostrar el precio habitual de una barra de pan,
# el descuento que se le hace por no ser fresca y el coste final total.

price = 3.49
discount = 0.6

panes_nofrescos = int(input("Ingrese el numero de barras de panes que no son del dia: "))

normal_price = round(price * panes_nofrescos, 2)
discount_price = round(normal_price * discount, 2)
total_price = round(normal_price - discount_price, 2)

print("El precio normal de las barres de panes es de: ", normal_price,
      "\n debido a que no son frescas se les hace un descuento de: ", discount_price,
      ",\n por tanto, el precio total es de: ", total_price)
