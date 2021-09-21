#ACCEDER A UN SUBCONJUNTO DE CARACTERES
"""
También podemos imprimir un rango de caracteres que conformen un string, para ello también se usa []
se escribe primero el número del caracter por el cual se empezará a imprimir en pantalla y después de los : el 
numero de la posición del string en donde terminará la impresión.
si falta alguno de los dos numeros se tomará como referencia el inicio o el final. por ejemplo:    
"""

string2 = 'Me voy a bañar'

print(string2[1:6]) #Del 1 al 6
print(string2[:5]) # Del 0 al 5
print(string2[3:]) # Del 3 al último