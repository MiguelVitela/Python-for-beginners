"""
Python proporciona un sistema de formato sofisticado para cadenas que puede ser útil para
imprimir información o registrar información de un programa.
El sistema de formato de cadena utiliza una cadena especial conocida como cadena de formato que
actúa como un patrón que define cómo se distribuirá la cadena final. Esta cadena de formato puede
contiener marcadores de posición que serán reemplazados con valores reales cuando la cadena final sea
creada. Se puede aplicar un conjunto de valores a la cadena de formato para llenar los marcadores de posición
utilizando el método format ().
El ejemplo más simple de una cadena de formato es uno que proporciona un único marcador de posición
indicado por dos llaves (por ejemplo, {}). Por ejemplo, el siguiente es un formato
cadena con el patrón 'Hola' seguido de un marcador de posición:
"""

ejemplo = 'Hola {}!'


"""Esto se puede usar con el método de cadena format () para proporcionar un valor (o
rellenar) el marcador de posición, por ejemplo:"""

print(ejemplo.format('Guapeton'))



"""Una cadena de formato puede tener cualquier número de marcadores de posición que se deben completar, por
ejemplo, el siguiente ejemplo tiene dos marcadores de posición que se rellenan al proporcionar dos
valores al método format ()"""

print('----'*10)
nombre = "Miguel"
edad = 20
print("{} is {} years old".format(nombre, edad))

"""También ilustra que las variables se pueden utilizar para proporcionar los valores para el formato
método así como valores literales. Un valor literal es un valor fijo como 42 o el
cadena 'John'.
De forma predeterminada, los valores están vinculados a los marcadores de posición según el orden en que
se proporcionan al método format (); sin embargo, esto se puede anular proporcionando un índice al marcador de posición para indicarle qué valor debe vincularse, para
ejemplo"""

print('----'*10)
presentación = "Hola {1} {0}, tu sacaste {2} en el {3}"
print(presentación.format('Vitela', 'Miguel', '100', 'exámen'))

"""Por supuesto, al ordenar los valores, es bastante fácil equivocarse en algo.
porque un desarrollador podría pensar que las cadenas están indexadas desde 1 o simplemente porque
hacer el pedido incorrecto.
Un enfoque alternativo es utilizar valores con nombre para los marcadores de posición. En esto
acercarse a las llaves que rodean el nombre del valor a ser sustituido, por
ejemplo {artista}. Luego, en el método format () se proporciona un par clave = valor
donde la clave es el nombre en la cadena de formato; esto se muestra a continuación"""

print('----'*10)

album = "{artist} sang {song} in {year}"
print(album.format(artist='Santa Fe Klan', song='No lleguaré', year=2021)) 

nuevo = '{saludo} abuela espero que {familiar} se encuentre {salud}'
print(nuevo.format(saludo = 'Hola', familiar = 'mi tio', salud = 'bien'))


"""También es posible indicar alineación y ancho dentro de la cadena de formato. Para
Por ejemplo, si desea indicar un ancho que se dejará para un marcador de posición cualquiera que sea el
valor real proporcionado, puede hacer esto usando dos puntos (':') seguidos del ancho para
usar. Por ejemplo, para especificar un espacio de 25 caracteres que se puede llenar con un
valor sustituto que puede utilizar {: 25} como se muestra a continuación:"""
print('----'*10)

print('|{:25}|'.format('25 characters width')) # Imprime |25 characters width      |
print('|{:20}|'.format('25 characters width')) # Imprime |25 characters width |

"""Dentro de este espacio también puede indicar una alineación donde:
• <Indica alineación a la izquierda (predeterminado),
•> Indica alineación a la derecha,
• ^ Indica centrado.
Estos siguen los dos puntos (':') y vienen antes del tamaño del espacio para usar, por
ejemplo:"""
print('----'*10)

print('|{:<25}|'.format('left aligned')) # The default
print('|{:>45}|'.format('right aligned'))
print('|{:^25}|'.format('centered'))

"""Otra opción de formato es indicar que un número debe formatearse con
separadores (como una coma) para indicar miles"""
print('----'*10)

print('{:,}'.format(1234567890))
print('{:,}'.format(1234567890.0))

"""De hecho, existen numerosas opciones disponibles para controlar el diseño de un valor
dentro de la cadena de formato y se debe hacer referencia a la documentación de Python para
más información."""