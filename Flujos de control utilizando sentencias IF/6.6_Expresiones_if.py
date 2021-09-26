"""Una expresión if es una forma abreviada de una declaración if que devuelve un valor. En
de hecho, la diferencia entre una expresión y una declaración en un lenguaje de programación es 
solo eso; las expresiones devuelven un valor; declaraciones no"""

"""Es bastante común querer asignar un valor específico a una variable dependiente de
alguna condición. Por ejemplo, si queremos decidir si alguien es adolescente o no
entonces podríamos verificar si tienen más de 12 años y menos de 20. Podríamos escribir 
esto como:"""

edad = 16
etapa = None

if (edad > 12) and edad < 20:
    etapa = 'adolescente'
    
else:
    etapa = 'no adolescente'
    
print(etapa)

"""Si ejecutamos esto, imprimimos la cadena 'adolescente'.
Sin embargo, esto es bastante largo y puede que no sea obvio que la verdadera intención de este
El código consistía en asignar un valor apropiado al estado.
Una alternativa es una expresión if. El formato de una expresión if es:

<result1> if <condition-is-met> else <result2>
"""

estado = ('adolescente' if edad > 12 and edad < 20 else 'no adolescente')
print(estado)

"""Una vez más, el resultado impreso es 'adolescente', sin embargo, ahora el código es mucho más
conciso, y está claro que el propósito de la prueba es determinar el resultado a asignar
al estado"""

#ejercicio de práctica

print('----'*20)

kilos = 89
categoria = None

if (kilos == 77):
    categoria = 'Welter'
    
else:
    categoria = 'No es welter'

print(categoria) 

# Ahora con expresión if

categoria = ('Welter' if kilos == 77 else 'no welter')
print(categoria)