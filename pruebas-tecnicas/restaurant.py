#Renato Silva
#09/04

rating = float(input("¿De 1 a 5 estrellas, cual fue tu nivel de satisfaccion en el restaurant?"))


if rating > 4.5 :
    print ('¡Extraordinario!')
    
elif rating >= 4 :
    print ('¡Excelente!')

elif rating >= 3 :
    print ('Bueno')

elif rating >= 2 : 
    print ('Regular')        

else:
    print ('Pesimo')        