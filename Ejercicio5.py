# Los alumnos de Hogwarts se han dividido en dos casas, Gryffindor y Slytherin,
# de acuerdo al sexo y el nombre. Gryffindor está formado por las mujeres con un nombre
# anterior a la M y los hombres con un nombre posterior a la N y Slytheryn por el resto.
# Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
name = input ('Introduzca su nombre: ')
gender = input ('Indique si usted es mujer u hombre: ')

uName = name.upper()
uGender = gender.upper()

if uName[:1] in {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H' 'I', 'J', 'K', 'L', 'M'}:
    if uGender == 'MUJER':
        print('Griffindor')
    else :
        print('Slythering')
elif uName[:1] in {'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}  :
    if uGender == 'HOMBRE' :
        print ('Grifindor')
    else :
        print ('Slythering')
else :
    print('Algún dato de los introducidos no es válido, vuelva a introducirlos. ')