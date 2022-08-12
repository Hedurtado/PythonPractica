# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas.
# Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así
# que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda.
# Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos
# y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

payaso_w = 112
toy_w = 75

payaso_sold = int(input("Enter the number of payasos sold "))
toy_sold = int(input("Enten the number of munecas sold "))

total_weight_p = payaso_w * payaso_sold
total_weight_t = toy_w * toy_sold

total_weight = total_weight_t + total_weight_p

print("El peso total del paquete es de: ", total_weight, "g")














