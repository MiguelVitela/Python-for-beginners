# DIVIDIENDO STRINGS

# Muy comunmente se tiene que dividir un string en multiples strings más pequeños separados por espacios o comas.

titulo = 'El bueno, el malo, y el feo'
print('Cadena normal', titulo)
print('Separar usando un espacio')
print(titulo.split(' '))  # 'El', 'bueno,', 'el', 'malo,', 'y', 'el', 'feo'
print('Separar usando una coma')
print(titulo.split(',')) # 'El bueno', ' el malo', ' y el feo'

"""
Como se pudo ver cada string puede ser separado utilizando los espacios que exista entre estos o bien utilizando el uso de 
comas en su escritura.
No pasamos la cadena a split () sino que usamos el
formato de la variable que contiene la cadena seguida de '.' y luego dividir ().
Esto se debe a que split () es en realidad lo que se conoce como método.
los métodos se aplican a cosas como cadenas usando la notación  de
punto.
"""

# 4.5.7 CONTANDO STRINGS
# También es posible realizar "Conteo de strings"
"""
Es posible averiguar cuántas veces se repite una cadena en otra cadena. Esta
se hace usando la operación count () por ejemplo
"""
 
mi_string = 'Cuenta  el número    de   espacios'
print(mi_string.count(' ')) # Indica que hay 10 espacios en blanco en el string
print(mi_string.count('a')) # Indica cuantas letras "a" hay en el string

# 4.5.8 REEMPLAZANDO STRINGS

"""
Una cadena puede reemplazar una subcadena en otra cadena. Esto se hace usando el
método replace () en una cadena. Por ejemplo
"""

mensaje_de_bienvenida = 'Hola mundo'
print(mensaje_de_bienvenida.replace('Hola', 'Hasta luego'))

# 4.5.9 ENCONTRANDO SUBCADENAS

"""
Puede averiguar si una cadena es una subcadena de otra cadena usando la función find ()
método. Este método toma una segunda cadena como parámetro y comprueba si eso
cadena está en la cadena que recibe el método find (), por ejemplo:
"""

# El método devuelve -1 si la cadena no está presente. De lo contrario, devuelve un índice.
# que indica el inicio de la subcadena. Por ejemplo
print('Miguel Angel Vitela Martinez'.find('Lopez')) # Devuelve -1 pues "Lopez" no se encuentra en la cadena


print('Miguel Angel Vitela Martinez'.find('Vitela')) # Devuelve un 13, pues es la posición de la primer letra de "Vitela"



