#Renato Silva
#09/04

gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

print('P1) ¿Te gusta mas el amanecer o el atardecer?')
print('1. Amanecer')
print('2. Atardecer')

respuestauno = input('Ingresa 1 o 2: ')

if respuestauno == 1:
    gryffindor += 1
    ravenclaw += 1

elif respuestauno == 2:
    hufflepuff += 1
    slytherin += 1

else: 
    print('Respuesta no valida.')


print('P2) Cuando muera, quiero que la gente me recuerde como: ')
print('1. El bueno')
print('2. El grandioso')
print('1. El sabio')
print('1. El valiente')

respuestados = int(input('Ingresa 1, 2, 3 o 4: '))

if respuestados ==1:
    hufflepuff += 2
elif respuestados ==2:
    slytherin += 2
elif respuestados ==3:
    ravenclaw += 2
elif respuestados ==4:
    gryffindor += 2

else:
    print('Respuesta no valida')        

print('P3) ¿Que tipo de instrumento complace mas a tu oido?')
print('1. El violin')
print('2. La trompeta')
print('3. El piano')
print('4. El tambor')

respuestatres = int(input('Ingresa 1, 2, 3 o 4: '))

if respuestatres ==1:
    hufflepuff += 4
elif respuestatres ==2:
    slytherin += 4
elif respuestatres ==3:
    ravenclaw += 4
elif respuestatres ==4:
    gryffindor += 4

else:
    print('Respuesta no valida')        



print('Puntajes finales: ')
print(f'Gryffindor: {gryffindor}')
print(f'Ravenclaw: {ravenclaw}')
print(f'Hufflepuf: {hufflepuff}')
print(f'Slytherin: {slytherin}')

casas = {
    "Gryffindor": gryffindor,
    "Ravenclaw": ravenclaw,
    "Hufflepuf": hufflepuff,
    "Slytherin": slytherin
}

casaganadora = max(casas, key=casas.get)
print(f'El sombrero seleccionador te ha asignado a: {casaganadora}!')