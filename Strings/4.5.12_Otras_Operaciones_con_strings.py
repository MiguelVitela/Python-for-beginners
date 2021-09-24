"""
De hecho, hay muchas operaciones diferentes disponibles para cadenas, incluidas
comprobar que una cadena comienza o termina con otra cadena, es decir, en mayúsculas o minúsculas
etc. También es posible reemplazar parte de una cadena con otra cadena, convertir cadenas
a mayúsculas, minúsculas o título, etc.

A continuación se ofrecen ejemplos de estos (tenga en cuenta que todas estas operaciones utilizan el punto
notación)

"""

chente = 'Pedro que gusto de verte'
print('Probando un string')
print('-' * 20)
print('Supe que eras licenciado', chente) # Se imprime el string escrito y el string de la variable chente
print("chente.startswith('H')", # Nos imprime "False" pues el string de la variable chente no empieza con "H"
print(chente.startswith('H')))
print(chente)
print("chente.startswith('P')", chente.startswith('P'))
print("chente.endswith('e')", chente.endswith('e')) # Pregunta si el string de la variable chente termina con "e"
print('chente.istitle()', chente.istitle()) # istitle Python () para detectar todas las palabras estén escritas cadena es una primera letra mayúscula y otras letras en minúsculas
print('chente.isupper()', chente.isupper()) # Este método indica si una cadena se comprende solo por letras mayúsculas
print('chente.islower()', chente.islower()) # Este método indica si una cadena se comprende solo por letras minúsculas
print('chente.isalpha()', chente.isalpha()) # método son Python isalpha () para detectar la cadena se compone de sólo letras.
print('Conversiones de strings')
print('-' * 20)
print('chente.upper()', chente.upper()) # Convierte el string a letras mayúsculas
print('chente.lower()', chente.lower()) # Convierte el string a letras minúsculas
print('chente.title()', chente.title()) # Convierte en mayúscula la primer letra después de un espacio
print('chente.swapcase()', chente.swapcase()) # Intercambia mayusculas por minúsculas y viseversa del string original
print('String leading, trailing spaces', " xyz ".strip()) # El método strip e utiliza para eliminar todos los espacios en blanco iniciales y finales de una cadena.