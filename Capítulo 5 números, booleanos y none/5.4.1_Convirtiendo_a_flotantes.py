"""Al igual que con los enteros, es posible convertir otros tipos como un int o una cadena en un
flotante. Esto se hace usando la función float ()"""

entero = 562
cadena = '1.5563'
flotante = float(entero)
print('Valor entero como flotante:', flotante)
print(type(flotante))
flotante = float(cadena)
print('Valor de cadena como flotante:', flotante)
print(type(flotante))