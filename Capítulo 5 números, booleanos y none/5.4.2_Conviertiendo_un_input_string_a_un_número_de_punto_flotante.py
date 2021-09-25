"""Como hemos visto, la función input () devuelve una cadena; que pasa si queremos
que el usuario ingrese un número de punto flotante (o real)? Como hemos visto antes, una cuerda
se puede convertir en un número de punto flotante usando la función float () y
por lo tanto, podemos usar este enfoque para convertir una entrada del usuario en un flotante"""

calificación = float(input('Por favor escriba la calificación exacta con decimales: '))
print(calificación)
print(type(calificación))