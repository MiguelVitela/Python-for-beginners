"""
Podemos hacer muchas operaciones con strings en python, entre las que destacan las
que destacan la concatenación, es decir la unión de strings. Por ejempo:
"""
    
string1 = 'Hola yo '
string2 = 'Me llamo '
string3 = 'Miguel'
    
string_final = string1 + string2 + string3
print(string_final)

# También podemos conocer el largo de un string:
print(len(string2))

"""
También podemos imprimir un solo caracter de un string poniendo entre [] el número de la posición que ocupa el string
que queremos imprimir, ejemplo:
"""

print(string3[4])

# Es importaante mencionar que las posiciones del strinng comienzan en 0 de isquierda a derecha.

"""
También podemos imprimir un rango de caracteres que conformen un string, para ello también se usa []
se escribe primero el número del caracter por el cual se empezará a imprimir en pantalla y después de los : el 
numero de la posición del string en donde terminará la impresión.
si falta alguno de los dos numeros se tomará como referencia el inicio o el final. por ejemplo:    
"""

print(string2[1:6]) #Del 1 al 6
print(string2[:5]) # Del 0 al 5
print(string2[3:]) # Del 3 al último

# Repetición o multiplicación de strings
# Con el operador * podemos duplicar strings como si de una multiplicación se tratase.

print(string3 * 5)
print('hola' * 10)