#Renato Silva
#07/04
adivinanza = 0
intentos = 0
limite_intentos = 5 

while adivinanza != 6 and intentos < limite_intentos:
    adivinanza = int(input('Adivina el número:'))
    intentos += 1 

if adivinanza == 6:
    print(f'¡Felicidades! Adivinaste el número en {intentos} intentos.')
else:
    print('¡Se acabaron tus intentos! El número correcto era 6.')