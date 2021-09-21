# 4.5.9 ENCONTRANDO SUBCADENAS

"""
Puede averiguar si una cadena es una subcadena de otra cadena usando la función find ()
método. Este método toma una segunda cadena como parámetro y comprueba si eso
cadena está en la cadena que recibe el método find (), por ejemplo:
"""

# El método devuelve -1 si la cadena no está presente. De lo contrario, devuelve un índice.
# que indica el inicio de la subcadena. Por ejemplo
print('Miguel Angel Vitela Martinez'.find('Lopez')) # Devuelve -1 pues "Lopez" no se encuentra en la cadena


print('Miguel Angel Vitela Martinez'.find('Vitela')) # Devuelve un 13, pues es la posición de la primer letra de "Vitela"
