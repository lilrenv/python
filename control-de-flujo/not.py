#Renato Silva
#Quiero irme a mi casita

respuesta = input('¿Estas cansado SI / NO?:').strip().lower()

cansado = respuesta == 'SI'

if not cansado: 
    print('Es hora de programar')
else: 
    print('Tomate un descanso')    