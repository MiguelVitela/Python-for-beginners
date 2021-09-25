"""Python admite otro tipo llamado booleano; un tipo booleano solo puede ser uno de
Verdadero o falso (y nada más). Tenga en cuenta que estos valores son verdaderos (con mayúscula
T) y Falso (con F mayúscula); verdadero y falso en Python no son lo mismo y
no tienen sentido por sí mismos."""

"""El equivalente de la clase int o float para los booleanos es bool.
El siguiente ejemplo ilustra el almacenamiento de los dos valores booleanos en una variable."""

bool1 = True
print(bool1)

bool2 = False
print(bool2)

print(type(bool2))


"""El tipo booleano es en realidad un subtipo de entero (pero solo con los valores
Verdadero y Falso) por lo que es fácil traducir entre los dos, usando las funciones
int () y bool () para convertir de booleanos a enteros y viceversa. Para
ejemplo"""

print('------'*20)

print(int(True))
print(int(False))
print(bool(1))
print(bool(0))

"""También puede convertir cadenas en booleanos siempre que las cadenas contengan
"true" o "false" (y nada más). Por ejemplo"""

print('------'*20)

status = bool(input('OK to proceed: '))
print(status)
print(type(status))