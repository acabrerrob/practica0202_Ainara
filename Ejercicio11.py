# Escribir un programa que pida al usuario una palabra y luego muestre 
# por pantalla una a una las letras de la palabra introducida empezando por la última.
word = input ('Introduzca una palabra: ')

splitWord = word.split()

print(splitWord[::-1] )