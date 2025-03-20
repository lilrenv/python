#Renato Silva, soy ambicioso y hoy es 17/03/2025

mi_lista = [10, 20, 30, 40, 50] #creacion de la lista
print(mi_lista[3]) #acceso al tercer elemento de la lista

mi_lista[-1] = 60 #cambiar el valor del ultimo elemento por otro valor
print(mi_lista) #lista ya modificada con el ultimo valor

mi_lista.append(80) #agregar un nuevo elemento a la lista
print(mi_lista) #lista ya modificada con nuevo elemento


mi_lista[2] = 5 #insertar un elemento en el segundo valor de la lista
print(mi_lista) #lista con elemento ya modificado


eliminado = mi_lista.pop(2) #elimina un elemento de la lista usando el valor
print(mi_lista) #lista ya modificada con elemento eliminado de la lista


indice = mi_lista.index(60) #encontrar la posicion del elemento ocupando .index
print(indice) #en la salida deberia de ser 3 

mi_lista.reverse() #invertir el orden de la lista
print(mi_lista) #orden de la lista ya invertido
