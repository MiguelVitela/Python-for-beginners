#CONVERTIR OTRAS CLASES EN STRINGS

"""Si intenta utilizar el operador de concatenación '+' con una cadena y algún otro tipo
de clase como un número, obtendrá un error.
Recibirá un mensaje de error que indica que solo puede concatenar cadenas
con cadenas no enteros con cadenas. Para concatenar un número como 21 con un
cadena debe convertirla en una cadena. Esto se puede hacer usando la función str ().
Por ejemplo:
"""

mensaje = 'Hola yo acabo de cumplir' + str(20)
print(mensaje)