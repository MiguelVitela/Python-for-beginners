"""En el Cap. 3 introdujimos brevemente el operador de asignación ('=') que se utilizó para
asignar un valor a una variable. De hecho, existen varios operadores de asignación diferentes
que podría usarse con valores numéricos.
Estos operadores de asignación en realidad se denominan operadores compuestos como
combinan una operación numérica (como sumar) con la asignación
operador. Por ejemplo, el operador compuesto + = es una combinación de la suma
operador y el operador = tal que:"""

x = 0
x = 0+1
print(x) # Imprimià el valor màs reciente, en este caso el 1

"""A algunos desarrolladores les gusta usar estos operadores compuestos porque son más concisos
escribir y puede ser interpretado de manera más eficiente por el intérprete de Python.
La siguiente tabla proporciona una lista de los operadores compuestos disponibles"""

z = 5
z **= 2
print(z)

m = 4
m //= 3
print(m)
"""      
Operator │                                  Description                                       │  Example  │ Equivalent
                 
+=       │     Add the value to the left-hand variable                                        │   x += 2  │ x = x + 2
 
−=       │  subtract the value from the left-hand variable                                    │   x −= 2  │ x = x – 2

*=       │   Multiple the left-hand variable by the value                                     │  x *= 2   │ x = x * 2

/=       │ Divide the variable value by the right-hand value                                  │  x /= 2   │ x = x / 2

//=      │ Use integer division to divide the variable’s value bythe right-hand value         │  x //= 2  │ x = x // 2

%=       │ Use the modulus (remainder) operator to apply the right-hand value to the variable │  x %= 2   │ x = x % 2

**=      │ Apply the power of operator to raise the variable’s value by the value supplied    │ x **= 3   │ x = x ** 3

"""