# Escribir un programa que pregunte el correo electrónico
# del usuario en la consola y muestre por pantalla otro correo
# electrónico con el mismo nombre (la parte delante de la arroba
# @) pero con dominio ceu.es.

email = input("Introduzca su correo electronico: ")

new_email = email[:email.find("@")+1]
print(new_email+"ceu.es")







