# Escribir un programa que pregunte por consola el
# precio de un producto en euros con dos decimales
# y muestre por pantalla el número de euros y el número
# de céntimos del precio introducido.

price = input("Introduzca el precio de un producto en euros con dos decimales: ")
eur = price[:price.find(".")]
cents = price[price.find('.')+1:]

print("Numero de euros ", eur, ' con ', cents, 'centimos')


