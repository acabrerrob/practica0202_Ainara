age = int (input ('Introduzca su edad: '))
monthIncome = float ( input('Introduzca su ingreso mensual: '))

if age >= 16:
    if monthIncome >= 1000:
        print ('Usted ha de tributar')
    else:
        print ('Usted no ha de tributar')
else:
    print ('Usted no ha de tributar')