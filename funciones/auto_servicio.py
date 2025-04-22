print( '1: Hamburguesa con queso ',
        '2: Papas fritas',
        '3: Refresco',
        '4: Helados',
        '5: Galletas')

def pedir_comida(numero_articulo):
    menu = {
        1: "Hamburguesa con queso",
        2: "Papas fritas ",
        3: "Refresco",
        4: "Helados",
        5: "Galletas"
    }
    
    return menu.get(numero_articulo, "Opción no válida. Por favor, elige un número del 1 al 5.")

# Ejemplo de uso
numero = int(input("Ingresa el número del artículo que deseas pedir: "))
print(pedir_comida(numero))