pistas = ("Puerta Roja", 221, "Londres", 3.14, "Watson", 7, "Moriarty")

print("🔎 ¡Bienvenido, detective Holmes!")
print("🧩 Se ha encontrado una serie de pistas misteriosas...")
print("🗝️ Pistas encontradas:", pistas)

#📌 analisis de pistas 

print("\In 🕵️ analizando las pistas...")

#¿Cual es la primera pista?
print(pistas.index("Puerta Roja"))

#¿Como encontrar la ultima pista?
print(pistas[6])

#¿Cuantas pistas hay en total?
print(len(pistas))

#¿Esta la palabra "Londres" en las pistas?
print("Londres" in pistas)

#¿Desempaqueta las primeras 3 pistas?
pista1, pista2, pista3 =  ("Puerta Roja", 221, "Londres")

print(pista1)  # "Puerta Roja"
print(pista2)  # 221
print(pista3)  # "Londres"

#Crea una nueva tupla con pistas adicionales 
nuevaspistas = ("Estación Central", 42, "Baker Street", 9.81, "Holmes", 5)
print(nuevaspistas)

#Encuentra la posicion de Watson
print(pistas.index("Watson"))

#¿Cuantas veces aparece el numero 7 en las pistas?
print(pistas.count(7))



print("\n felicitaciones, detective. ¡Has resuelto el analisis de las pistas!")
print("🔒 Ahora, sigue con las deducciones para resolver el misterio")
