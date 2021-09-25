"""Cualquier operación que involucre tanto enteros como números de coma flotante siempre
producir un número de coma flotante. Es decir, si uno de los lados de una operación como
sumar, restar, dividir o multiplicar es un número de punto flotante, entonces el resultado será un
número de coma flotante. Por ejemplo, dado el número entero 3 y el punto flotante
número 0.1, si los multiplicamos, obtenemos un número de punto flotante:"""

i = 3 * 0.1
print(i)

"""¿Cuál puede haber sido o no lo que esperaba (podría haber esperado
0,3); sin embargo, esto resalta el comentario al comienzo de este capítulo relacionado con
Los números de punto flotante (o reales) se representan como una aproximación dentro de un
sistema informático. Si esto fuera parte de un cálculo mayor (como el cálculo de
la cantidad de interés que se pagará por un préstamo muy grande durante un período de 10 años),
el resultado final bien podría quedar fuera por una cantidad significativa.
Es posible solucionar este problema utilizando uno de los módulos (o bibliotecas) de Pythons.
Por ejemplo, el módulo decimal proporciona la clase Decimal que manejará adecuadamente la multiplicación de 3 por 0,1."""