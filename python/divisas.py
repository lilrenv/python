#Renato Silva
#Ahora se pone interesante los ejercicios
#25/03/2025

pesos = int(input("¿Cuanto te queda en pesos colombianos?")) 
soles = int(input("¿Cuanto te queda en soles peruanos?"))
reales = int(input("¿Cuanto te queda en reales brasileños?"))


# Tasas de cambio aproximadas
tasa_pesos = 0.00025  # COP a USD
tasa_soles = 0.28     # PEN a USD
tasa_reales = 0.21    # BRL a USD


# Convertir las divisas a dólares
dolares = (pesos * tasa_pesos) + (soles * tasa_soles) + (reales * tasa_reales)

# Mostrar el resultado
print(f"¡Cha-Chang! Ahora tienes el total en dolares 💰 (USD): {dolares:.2f}")