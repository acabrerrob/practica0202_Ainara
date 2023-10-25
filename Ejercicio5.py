# Los alumnos de Hogwarts se han dividido en dos casas, Gryffindor y Slytherin,
# de acuerdo al sexo y el nombre. Gryffindor está formado por las mujeres con un nombre
# anterior a la M y los hombres con un nombre posterior a la N y Slytheryn por el resto.
# Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
name = input ('Introduzca su nombre: ')
gender = input ('Introduzca su sexo: ')

uName = name.upper()


if uName[:1] == 'A' or  uName[:1] == 'B' or uName[:1] == 'C':
    print (uName[:1])
