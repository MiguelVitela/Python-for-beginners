"""También vale la pena explorar lo que sucede en la división de enteros y verdaderos cuando
están involucrados números negativos. Por ejemplo"""

print('La división de 3 / 2 es', 3/2)
print('La división de -3 / 2 es', -3/2)
print('La división entera de 3 / 2 es', 3//2)
print('La división entera de -3 / 2 es', -3//2)



"""Los primeros tres de estos podrían ser exactamente lo que espera dado nuestro anterior
discusión; sin embargo, el resultado del último ejemplo puede parecer un poco sorprendente, ¿por qué
¿3 // 2 genera 1 pero −3 // 2 genera −2?
La respuesta es que Python siempre redondea el resultado de la división entera hacia
menos infinito (que es el menor número negativo posible). Esto significa que tira
el resultado de la división entera al número más pequeño posible, 1 es menor que
1,5 pero −2 es menor que −1,5"""