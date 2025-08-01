def sumar(a, b):
    """
    Esta función suma dos números y devuelve el resultado.
    """
    return a + b

def restar(a, b):
    """
    Esta función resta dos números y devuelve el resultado.
    """
    return a - b

if __name__ == '__main__':
    # Aquí puedes probar las funciones directamente.
    
    num1 = 10
    num2 = 5
    
    # Realizamos la suma
    resultado_suma = sumar(num1, num2)
    print(f"La suma de {num1} y {num2} es: {resultado_suma}")
    
    # Realizamos la resta
    resultado_resta = restar(num1, num2)
    print(f"La resta de {num1} y {num2} es: {resultado_resta}")