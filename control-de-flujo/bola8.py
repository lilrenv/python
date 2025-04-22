#Renato Silva 15/04

import random

pregunta = str(input('¿Cual es tu pregunta?'))

def fortuna ():
    lista_fortuna = ['Si, definitivamente',
                     'Con Toda certeza, que si',
                     'Sin lugar a dudas',
                     'Respuesta confusa, intentalo de nuevo',
                     'Preguntalo nuevamente mas tarde',
                     'Mejor no decirte ahora',
                     'Mis fuentes dicen que no',
                     'El panorama no es muy favorable',
                     'Muy dudoso'
    ]

    fortuna = random.choice(lista_fortuna)
    print(fortuna)
    return fortuna  
fortuna()
