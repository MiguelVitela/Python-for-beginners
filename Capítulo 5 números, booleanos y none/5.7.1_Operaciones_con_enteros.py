"""Se pueden sumar dos enteros usando +, por ejemplo, 10 + 5. A su vez, dos
los números enteros se pueden restar (10 - 5) y multiplicar (10 * 4). Operaciones como +,
- y * entre enteros siempre producen resultados enteros.
Esto se ilustra a continuación"""

n1 = 5
n2 = 6
print(n1+n2)
print(type(n1 + n2))

n3 = 5 
n4 = 9
print(n3*n4)
print(type(n3 * n4)) 

goles_a_favor = 4
goles_en_contra = 2
diferencia_de_goles = goles_a_favor - goles_en_contra
print(diferencia_de_goles)
print(type(diferencia_de_goles))


"""Sin embargo, puede notar que nos hemos perdido la división con respecto a
enteros, ¿por qué es esto? Es porque depende del operador de división que utilice como
a lo que realmente es el tipo devuelto.
Por ejemplo, si dividimos el número entero 100 entre 20, el resultado puede ser
razonablemente esperar producir podría ser 5; pero no lo es, en realidad es 5.0:"""

print('------'*20)

print(100/20)
print(type(100/20))

"""Y como puede ver en esto, el tipo de resultado es flotante (es decir, flotante
número de punto). Entonces porqué es este el caso?
La respuesta es que la división no sabe si los dos enteros involucrados pueden
dividirse entre sí exactamente o no (es decir, hay un resto). Por lo tanto, por defecto
produce un número de coma flotante (o real) que puede tener una parte fraccionaria. Esta
Por supuesto, es necesario en algunas situaciones, por ejemplo, si dividimos 3 entre 2"""

print('------'*20)

print(3/2)
print(type(3/2))

"""También se puede realizar una división entera, como por ejemplo:"""

print('------'*20)

entera = 3//2
print(entera)
print(type(entera))

"""Aunque también podemos obtener el módulo de una división, es decir su residuo"""

print('------'*20)

print('El módulo de la operación 4 / 2 es:', 4%2) # El residuo es 0
print('El módulo de la operación 3 / 2 es:', 3%2) # El residuo es 1

"""Y por último encontramos la exponenciación"""

print('------'*20)

a = 5
b = 3

expo = a ** b

print(expo)