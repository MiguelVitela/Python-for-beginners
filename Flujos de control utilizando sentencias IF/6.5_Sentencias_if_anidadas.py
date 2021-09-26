"""Es posible anidar una instrucción if dentro de otra. Este término anidamiento indica
que una instrucción if se encuentra dentro de otra instrucción if y puede ser
utilizado para refinar el comportamiento condicional del programa.
A continuación se ofrece un ejemplo. Tenga en cuenta que permite realizar algún comportamiento
antes y después de la ejecución / ejecución de la instrucción if anidada. También tenga en cuenta 
que la sangría es clave aquí, ya que es cómo funciona Python si las declaraciones if están 
anidadas o no"""


snowing = True
temp = -1
if temp < 0:
    print('It is freezing')
    
    if snowing:
        print('Put on boots')
    print('Time for Hot Chocolate')

print('Bye')


print('-----'*20)

snowing = True
temp = -1
if temp < 0:
    print('It is freezing')
    
    if snowing:
        print('Put on boots')
        print('Time for Hot Chocolate')
        
print('Bye')

print('-----'*20)


sudar = True
temperatura = 35
if temperatura > 30:
    print('Hace un calor que te cagas')
    
    if sudar:
        print('Saquen las caguamas jotos')
    print('Es tiempo de una coquita bien helodia')
    
print('A che qlo no te quieres pagar nada, mejor me voy')


print('-----'*20)


temper = int(input('Escriba la temperatura que hace en su localidad: '))

if temper >= 5 and temper < 15 :
    humedad = input('Hay humedad o es clima seco?, responda seco o humedo: ')
    if humedad == 'seco' or humedad == 'Seco' or humedad == 'SECO':
        print('Hace frio seco')
    elif humedad == 'humedo' or humedad == 'Humedo' or humedad == 'HUMEDO':
        print('Se me entumen las patas')
    else:
        print('Respuesta no vàlida, intèntelo de nuevo')
        
elif temper >= 15 and temper < 25:
    humedad = input('Hay humedad o es clima seco?, responda seco o humedo: ')
    if humedad == 'seco' or humedad == 'Seco' or humedad == 'SECO':
        print('Excelente clima, es perfecto para mì')
    elif humedad == 'humedo' or humedad == 'Humedo' or humedad == 'HUMEDO':
        print('Ojo, si sale el sol puede hacer mucho calor')
    else:
        print('Respuesta no vàlida, intèntelo de nuevo')
        
elif temper >= 25 and temper < 45:
   humedad = input('Hay humedad o es clima seco?, responda seco o humedo: ')
   if humedad == 'seco' or humedad == 'Seco' or humedad == 'SECO':
       print('Hace mucho calor seco, clima ideal para sacar las guamas')
   elif humedad == 'humedo' or humedad == 'Humedo' or humedad == 'HUMEDO':
       print('No manches asì si se siente bien culero')
   else:
       print('Respuesta no vàlida, intèntelo de nuevo')
       
else:
    print('Los valores de temperatura dados son muy extremos, introduzca el dato nuevamente')
    
     