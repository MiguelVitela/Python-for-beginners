"""En algunos casos, puede haber varias condiciones que desee probar, con cada condición
siendo probada si la anterior falló. Este escenario es compatible con Python
por el elemento elif de una declaración if"""

"""El elemento elif de una instrucción if sigue a la parte if y viene antes de cualquier
else. Tiene el siguiente formato: 

elif <condition-evaluating-to-boolean>:
statement:
"""

ahorros = int(input('Escriba por favor la cantidad de dinero ahorrada: '))

if ahorros <= 0:
    print('Usted no tiene nada ahorrado')
    
elif ahorros > 500:
    print('Usted tiene poco dinero ahorrado')
    
elif ahorros >= 1000:
    print('Usted tiene algo de dinero ahorrado')
    
elif ahorros > 2000:
    print('Usted tiene mucho dinero ahorrado')
    
else:
    print('Adiós')

