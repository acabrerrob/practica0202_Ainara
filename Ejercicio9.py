number = int (input('Introduzca un número entero: '))

for i in range(1, number + 1, +1):
    for j in range(2 * i - 1, 0, -2):
        print(j, end = ' ')
    print()  
