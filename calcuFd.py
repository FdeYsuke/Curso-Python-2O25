def evaluar_numero(numero):
    """
    Evalúa un número para determinar si es par o impar,
    con mensajes especiales para 7 y 10.
    """
    if numero == 10:
        print("El número ingresado es 10")
    elif numero == 7:
        print("Se ha ingresado un comodín")
    elif (numero % 2) == 0:
        print("El número ingresado es par")
    else:
        print("El número ingresado es impar")

def main():
    """
    Función principal para solicitar la entrada del usuario
    y llamar a la función de evaluación.
    """
    # Se solicita la entrada del usuario y se convierte a entero
    entrada = int(input("Ingrese el número a evaluar: "))

    # Se invoca la función de evaluación con el número ingresado
    evaluar_numero(entrada)

# Esto asegura que la función main se ejecute cuando el script es corrido directamente
if __name__ == "__main__":
    main()