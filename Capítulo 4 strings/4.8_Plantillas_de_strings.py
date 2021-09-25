"""Una alternativa al uso de formato de cadena es utilizar plantillas de cadena. Éstas eran
introducido en Python 2.4 como una solución más simple y menos propensa a errores para la mayoría de cadenas
requisitos de formato.
Una plantilla de cadena es una clase (tipo de cosa) que se crea a través de la cadena.
Función Template (). La plantilla contiene una o más variables nombradas precedidas por un símbolo $. La plantilla se 
puede utilizar con un conjunto de valores que reemplace las variables de la plantilla con valores reales."""

import string
# Initialise the template with ¢variables that
# will be substitute with actual values
#plantilla = string.Template('$futbolista juega para $equipo en $año')

template = string.Template('$artist sang $song in $year')

"""Tenga en cuenta que es necesario incluir una declaración de importación al inicio del programa.
ya que las plantillas no se proporcionan de forma predeterminada en Python; deben cargarse desde un
biblioteca de características de cadena adicionales. Esta biblioteca es parte de Python pero necesitas
dígale a Python que desea acceder a estas instalaciones de cadenas adicionales.
Regresaremos a la declaración de importación más adelante en el libro; por ahora solo excepto
que es necesario para acceder a la funcionalidad Plantilla.
La plantilla en sí se crea mediante la función string.Template (). los
cadena pasada a la función string.Template () puede contener cualquier carácter
más las variables de la plantilla (que se indican con el carácter $ seguido del
nombre de la variable como $ artista arriba).
Por lo tanto, lo anterior es una plantilla para el patrón 'algún artista cantó alguna canción en algún año'.
Los valores reales se pueden sustituir en la plantilla utilizando el sustituto ()
función. La función sustituta toma un conjunto de pares clave = valor, en el que la clave es la
nombre de la variable de plantilla (menos el carácter $ inicial) y el valor es el
valor para usar en la cadena"""

print(template.substitute(artist='Freddie Mercury', song='The Great Pretender', year=1987))

jugador = string.Template('$jugador juega en el $equipo como $posicion')
print(jugador.substitute(jugador='Leo Messi', equipo='PSG', posicion='delantero'))

# Initialise the template with $variables that
# will be substitute with actual values

# Replace / substitute template variables with actual values
# Can use a key = value pairs where the key is the name of 
# the template Variable and the value is the value to use 
# in the string


hola = string.Template('$persona quiere $fruta en su $lugar')
print(hola.substitute(persona='Maria', fruta='melones', lugar='casa'))

print('*' *20)
"""Por supuesto, podemos reutilizar la plantilla sustituyendo la plantilla por otros valores.
variables, cada vez que llamamos al método substitute () generará una nueva
cadena con las variables de plantilla reemplazadas con los valores apropiados:"""

print(template.substitute(artist='Ed Sheeran', song='Galway Girl', year=2017))
print(template.substitute(artist='Camila Cabello', song='Havana', year=2018))

print(jugador.substitute(jugador = 'Cristiano Ronaldo', equipo = 'Manchester United', posicion = 'Delantero'))
print(hola.substitute(persona = 'Luis', fruta = 'Sandía', lugar = 'tarabajo'))

print('*' *20)

"""Alternativamente, puede crear lo que se conoce como diccionario. Un diccionario es un
estructura compuesta por pares clave: valor en los que la clave es única. Esto permite que
la estructura de datos que se creará contenga los valores a utilizar y luego se aplique a la
función sustituta:"""

d = dict(artist = 'Billy Idol', song='Eyes Without a Face', year = 1984)
print(template.substitute(d))

diccionario = dict(jugador = 'Tomas Muller', equipo = 'Bayern Munich', posicion = 'Medio')
print(jugador.substitute(diccionario))

diccionario2 = dict(persona = 'Alma', fruta = 'manzanas', lugar = 'escuela')
print(hola.substitute(diccionario2))
print('*' *20)

"""Las cadenas de plantilla pueden contener variables de plantilla con el formato
$ nombre-de-variable; sin embargo, hay algunas variaciones que vale la pena señalar:
• $$ le permite incluir un carácter '$' en la cadena sin que Python interprete
como el comienzo de una variable de plantilla, el doble '$$' se reemplaza con un
solo $. Esto se conoce como escapar de un personaje de control.
• $ {template_variable} es equivalente a $ template_variable. Está
requerido cuando los caracteres de identificación válidos siguen al marcador de posición pero no son parte
del marcador de posición, como '' $ {sust.} ificación ''.
Otro punto a tener en cuenta sobre la función template.substitute () es que si
si no proporciona un valor a todas las variables de la plantilla, se producirá un error
generado. Por ejemplo"""

#print(template.substitute(artist='David Bowie', song='Rebel Rebel'))

"""Dará lugar a que el programa no se ejecute y se genere un mensaje de error.}

Esto se debe a que no se ha proporcionado un valor a la variable de plantilla $ año.
Si no quiere tener que preocuparse por proporcionar todas las variables en un
plantilla con un valor, entonces debe usar la función safe_substitute ():"""

print(template.safe_substitute(artist='David Bowie', song='Rebel Rebel'))

print(hola.safe_substitute(persona = 'Juan', fruta = 'pera'))
print(jugador.safe_substitute(jugador = 'Jack Grealish', equipo = 'Manchester City' ))
"""Esto completará las variables de plantilla proporcionadas y dejará cualquier otra plantilla
variables que se incorporarán a la cadena tal como están, por ejemplo:"""

#David Bowie sang Rebel Rebel in $year