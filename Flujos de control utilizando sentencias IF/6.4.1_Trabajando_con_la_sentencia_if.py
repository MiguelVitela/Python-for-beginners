"""En su forma más básica, la declaración if es
if <condición-evaluación-a-booleano>:
declaración
Tenga en cuenta que la condición debe evaluarse como Verdadero o Falso (o un equivalente
valor. Si la condición es Verdadera, ejecutaremos el
declaración con sangría.
Tenga en cuenta que la sangría, esto es muy importante en Python; de hecho, diseño del código
es muy, muy importante en Python. La sangría se utiliza para determinar cómo una pieza de
El código debe estar asociado con otra parte del código.
Veamos un ejemplo sencillo"""
import math

número = int(input('Escriba un número: '))

if número < 0:
    print(número, 'es negativo')
    
"""Si deseamos ejecutar múltiples declaraciones cuando nuestra condición es Verdadera, podemos
sangrar varias líneas; de hecho, todas las líneas con sangría al mismo nivel después del if
serán automáticamente parte de la declaración if. Por ejemplo"""

print('------' *20)

n = int(input('Escriba otro número: '))

if n > 0:
    print(n,'es un número positivo')
    print('El cuadrado de ese número es: ', n**2)
    print('La raíz cuadrada de ese número es: ', math.sqrt(n))
print('Hasta luego')


"""Si metemos un número negativo antes del último if solo se imprimirá en consola "Hasta luego".
Tenga en cuenta que no se ejecutó ninguna de las líneas sangradas.
Esto se debe a que las 3 líneas con sangría están asociadas con la instrucción if y
solo se ejecutará si la condición booleana evalúa (devuelve) True. Sin embargo,
la instrucción print ('Hasta luego') no es parte de la instrucción if; es simplemente la siguiente
instrucción a ejecutar después de que la sentencia if """