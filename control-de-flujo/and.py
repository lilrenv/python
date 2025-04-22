#Renato Silva
#02/04/2025
#Hace frio juan

usuario = input('Ingresar tu nombre:')
hambre = int(input('¿Cuanta hambre tienes? (1-10)'))
enojo = int(input('¿Cuanto enojo tienes? (1-10)'))

if hambre > 4 and enojo > 5:
    print('Enfadado por hambre')
elif hambre> 4 and enojo < 4:
    print('Chill pero con hambre')      