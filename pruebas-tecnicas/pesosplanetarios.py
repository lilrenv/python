#Renato Silva
#09/04

peso = float(input('¿Cual es su peso terrestre?'))
planeta = int(input('Escoge un numero de planeta (1-7)'))

peso_mercurio = 0.38  
peso_venus = 0.91     
peso_marte = 0.38   
peso_jupiter = 2.53
peso_saturno = 1.07
peso_urano = 0.89
peso_neptuno = 1.14

destinopesomercurio = (peso * peso_mercurio)
destinopesovenus = (peso * peso_venus)
destinopesomarte = (peso * peso_marte)
destinopesojupiter = (peso * peso_jupiter)
destinopesosaturno = (peso * peso_saturno)
destinopesourano = (peso * peso_urano)
destinopesoneptuno = (peso * peso_neptuno)

if planeta == 1:
    print(f"¡Cha-Chang! tu peso en mercurio es: {destinopesomercurio}kg")

elif planeta == 2:
    print(f"¡Cha-Chang! tu peso en venus es: {destinopesovenus}kg") 

elif planeta == 3:
    print(f"¡Cha-Chang! tu peso en marte es: {destinopesomarte}kg")    

elif planeta == 4:
    print(f"¡Cha-Chang! tu peso en jupiter es: {destinopesojupiter}kg")    

elif planeta == 5:
    print(f"¡Cha-Chang! tu peso en saturno es: {destinopesosaturno}kg")    

elif planeta == 6:
    print(f"¡Cha-Chang! tu peso en urano es: {destinopesourano}kg")    

elif planeta == 7:
    print(f"¡Cha-Chang! tu peso en neptuno es: {destinopesoneptuno}kg")         

else: 
    print('¡Planeta invalido!')      


