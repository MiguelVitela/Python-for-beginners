# 4.6.1 Las cadenas de Python distinguen entre mayúsculas y minúsculas

"""
En Python, la cadena 'l' no es la misma que la cadena 'L'; uno contiene la minúscula
la letra 'l' y la otra la letra mayúscula 'L'. Si las mayúsculas y minúsculas no le importan
entonces deberías convertir cualquier cadena que quieras comparar en un caso común
antes de realizar cualquier prueba; por ejemplo usando lower () como en
"""

lic = 'Olivella'
print(lic.lower().startswith('o')) # Lower convierte a minusculas todas las letras de una cadena
print('----' *20)

# 4.6.2 Nombres de funciones / métodos

"""
Tenga mucho cuidado con el uso de mayúsculas en los nombres de funciones / métodos; en Python
isupper () es una operación completamente diferente a isUpper (). Si usa el
caso incorrecto Python no podrá encontrar la función o método requerido y va a
generar un mensaje de error. No se preocupe por la terminología sobre funciones
y métodos en este punto, por ahora pueden tratarse como lo mismo y solo
difieren en la forma en que recordaron o invocaron.
"""

# 4.6.3 Invocaciones de funciones / métodos

"""
También tenga cuidado de incluir siempre los corchetes cuando llame a una función o
método; incluso si no toma parámetros / argumentos. Hay una diferencia significante
entre isupper e isupper (). El primero es el nombre de una operación en un
string mientras que el segundo es una llamada a esa operación para que la operación se ejecute.
Ambos formatos son legales en Python pero el resultado es muy diferente, por ejemplo:
"""

rusia = 'Unión Soviética'

print(rusia.isupper)
print(rusia.isupper())

"""
Tenga en cuenta que la primera impresión le indica que se refiere a la
método llamado isupper definido en el tipo String; mientras que el segundo realmente corre
isupper () para usted y devuelve True o False
"""
