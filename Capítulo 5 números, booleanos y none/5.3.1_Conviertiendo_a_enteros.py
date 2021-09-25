"""Es posible convertir otro tipo en un entero usando la función int (). Para
ejemplo, si queremos convertir una cadena en un int (asumiendo que la cadena contiene un
número entero), entonces podemos hacer esto usando la función int (). Por ejemplo:"""

total = int('400')
print(type(total))
print(total)

"""Esto puede resultar útil cuando se utiliza con la función input ().
La función input () siempre devuelve una cadena. Si queremos pedirle al usuario que ingrese
un número entero, entonces necesitaremos convertir la cadena devuelta desde el
input () en un int. Podemos hacer esto envolviendo la llamada a la entrada ()
en una llamada a la función int (), por ejemplo"""

edad = int(input('Escriba su edad: '))
print(type(edad))
print(edad)

"""La función int () también se puede utilizar para convertir un número de punto flotante en un
int, por ejemplo"""

entero = int(4.565)
print(entero)