#Renato Silva
import random

def fortuna ():
    lista_fortuna = ['No persigas la felicidad, creala',
                     'Todas las cosas son dificiles antes de ser faciles',
                     'El pajaro madrugador consigue el gusano, pero el segundo raton se lleva el queso',
                     'Alguien en tu vida necesita una carta de tu parte',
                     'No solo pienses. ¡Actua!',
                     'Tu corazon se acelerara',
                     'La fortuna que buscas esta en otra galleta',
                     '¡Ayuda! ¡Estoy prisionero en una panaderia china!'
    ]

    fortuna = random.choice(lista_fortuna)
    print(fortuna)
    return fortuna  
fortuna()
fortuna()
fortuna()