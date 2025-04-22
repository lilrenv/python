#Renato Silva
#03/04/2025

altura = int(input('¿Cual es tu altura (cm)?'))
#crearon una variable para solicitar informacion del usuario
creditos = int(input('¿Cuantos creditos tienes?'))

if altura >= 137 and creditos >= 10:
    print('Disfruta tu viaje')
elif altura < 137 and creditos >= 10:
    print('No tienes la altura suficiente para subir')    
elif creditos < 10 and altura >= 137:
    print('No tienes suficientes creditos')
else:
    print('No tienes la altura ni los creditos necesarios para subir')        