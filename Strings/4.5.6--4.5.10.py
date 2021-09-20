# Muy comunmente se tiene que dividir un string en multiples strings más pequeños separados por espacios o comas.

titulo = 'El bueno, el malo, y el feo'
print('Cadena normal', titulo)
print('Separar usando un espacio')
print(titulo.split(' '))
print('Separar usando una coma')
print(titulo.split(','))

"""
Como se pudo ver cada palabra del string es separada usando comas o un espacio.
No pasamos la cadena a split () sino que usamos el
formato de la variable que contiene la cadena seguida de '.' y luego dividir ().
Esto se debe a que split () es en realidad lo que se conoce como método.
los métodos se aplican a cosas como cadenas usando el punto
notación.
"""
