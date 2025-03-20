#crear lista
mi_lista = []

mi_lista.append("🏦 Sacar dinero del banco")
mi_lista.append("🍵 Hacer una colada")
mi_lista.append("🌱 Dar un paseo")
mi_lista.append("💈 Cortarse el cabello")
mi_lista.append("🍵 Preparar un te")
mi_lista.append("💻 Terminar el capitulo de listas")
mi_lista.append("♥️ Llamar a mama")
mi_lista.append("📺 Ver Mi Heroe Academia")

print(mi_lista)

#Acceder a la primera tarea de la lista
indice = mi_lista.index("🏦 Sacar dinero del banco")
print(indice) 

#Encontrar la segunda tarea de la lista
print(mi_lista[1])

#obtener un subconjunto de tareas usando slicing(rebanado)
print(mi_lista[0:4])

# Intentar acceder a un índice inexistente y manejar el error
try:
    # Aquí vamos a intentar acceder a un índice fuera de rango
    print(mi_lista[10])  # Índice 10 no existe porque la lista tiene solo 8 elementos
except IndexError:
    print("Error: El índice no existe en la lista.")

    
# Añadir una tarea secreta sin usar .append() al final del código
mi_lista[0:0] = ["🤫 Tarea secreta"]  # Insertar al principio de la lista

# O también podríamos usar el operador += para concatenar una lista
# mi_lista += ["🤫 Tarea secreta"]

print("\nLista después de añadir la tarea secreta:")
print(mi_lista)
