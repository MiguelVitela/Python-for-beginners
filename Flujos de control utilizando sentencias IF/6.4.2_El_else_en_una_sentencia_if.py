"""También podemos definir una parte "else" de una declaración if; este es un elemento opcional que
se puede ejecutar si la parte condicional de la instrucción if devuelve False. Por ejemplo:"""

number = int(input('Escribe un número: '))

if number < 0:
    print(number, 'es un número negativo')
else:
    print(number, 'es un número positivo')
    
"""Ahora, cuando se ejecuta este código, si el número ingresado es menor que cero,
se ejecutará la primera declaración print () de lo contrario se ejecutará la segunda declaración
print (). Sin embargo, tenemos la garantía de que al menos uno (y como máximo uno) de 
los print () se ejecutará."""