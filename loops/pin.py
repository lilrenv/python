#Renato Silva
#07/04
#Aca atras tomando desayuno

print('Banco del 4°B')

pin = int(input('Ingresa tu PIN:'))

while pin !=1234: 
    pin = int (input('PIN incorrecto. Ingresa tu PIN nuevamente:'))

if pin ==1234:
    print('PIN aceptado')
    print('Bienvenido a tu cuenta')