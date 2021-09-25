"""Python tiene un tipo especial, NoneType, con un solo valor, None.
Esto se usa para representar valores nulos o nada.
No es lo mismo que Falso, o una cadena vacía o 0; es un sin valor. Puede ser
se utiliza cuando necesita crear una variable pero no tiene un valor inicial para ella. Para
ejemplo:"""

ganador = None

"""A continuación, puede probar la presencia de None usando 'is' y 'is not', por
ejemplo:"""

print(ganador is None) # Devolverá True
print(ganador is not None) #Devolverá False

print('ganador:', ganador)
print('ganador is None:', ganador is None)
print('ganador is not None:', ganador is not None)
print(type(ganador))
print('colocar la variable ganador como "True"')
ganador = True
print('ganador:', ganador)
print('ganador is None:', ganador is None)
print('ganadorr is not None:', ganador is not None)
print(type(ganador))