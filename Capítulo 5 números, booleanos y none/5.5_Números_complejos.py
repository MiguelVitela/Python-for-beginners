"""Los números complejos son el tercer tipo de Python de tipo numérico incorporado.
El número complejo está definido por una parte real y una parte imaginaria y tiene la forma
a + bi (donde i es la parte imaginaria y ayb son números reales):"""

"""La parte real del número (a) es el número real que se suma al puro
número imaginario.
La parte imaginaria del número, (b), es el coeficiente del número real del puro
número imaginario.
La letra 'j' se usa en Python para representar la parte imaginaria del número, por ejemplo:"""

c1 = 1j
c2 = 2j
print('c1:', c1, ', c2:', c2)
print(type(c1))
print(c1.real)
print(c1.imag)

print('-----'*20)

print(c2.real)
print(c2.imag)
"""Como puede ver, el tipo de número es 'complejo' y cuando el número es
impreso directamente se hace imprimiendo las partes real e imaginaria juntas.
No se preocupe si esto es confuso; es poco probable que necesite utilizar complejos
números a menos que esté haciendo una codificación muy específica, por ejemplo, dentro de un
campo científico."""