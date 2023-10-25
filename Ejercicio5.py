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