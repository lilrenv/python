def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero"
    return a / b

def exponenciacion(a, b):
    return a ** b

# Ejemplo de uso
if __name__ == "__main__":
    print("Suma: ", sumar(5, 3))
    print("Resta: ", restar(5, 3))
    print("Multiplicación: ", multiplicar(5, 3))
    print("División: ", dividir(5, 3))
    print("Exponenciación: ", exponenciacion(2, 4))
