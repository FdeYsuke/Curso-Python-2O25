class Numero:
    # El método __init__ se usa para inicializar un objeto de la clase
    # Recibe el número que se va a evaluar y lo guarda en 'self.numero'
    def __init__(self, numero):
        self.numero = numero

    def evaluarNumero(self):
        """
        Evalúa el número almacenado en el objeto para determinar si es par o impar,
        con mensajes especiales para 7 y 10.
        """
        # La lógica de las condiciones especiales (10 y 7) debe ir primero,
        # para que tengan prioridad sobre la verificación de par/impar.
        if self.numero == 10:
            print("El número ingresado es 10")
        elif self.numero == 7:
            print("Se ha ingresado un comodín")
        # Si no es 10 ni 7, verificamos si es par o impar.
        # Usamos el operador módulo (%) que da el residuo de una división.
        # Si el residuo de dividir por 2 es 0, es par.
        elif (self.numero % 2) == 0:
            print("El número ingresado es par")
        else: # Si el residuo no es 0 (es 1 para enteros), es impar.
            print("El número ingresado es impar")

    # Este método fue parte del código que proporcionaste previamente.
    # Realiza la suma del número del objeto con otro número dado.
    def sumar(self, numero_a_sumar):
        return self.numero + numero_a_sumar

# --- Función Principal (main) ---
# Esta función es el punto de entrada de tu programa y organiza el flujo.
def main():
    print("=== Evaluador de Números ===")

    # Se solicita la entrada del usuario.
    # 'input()' siempre devuelve texto, por eso usamos 'int()' para convertirlo a número entero.
    try:
        entrada_usuario = int(input("Ingrese el número a evaluar: "))
    except ValueError:
        # Si el usuario no ingresa un número válido, se muestra un mensaje de error
        # y la función termina.
        print("Entrada inválida. Por favor, ingrese un número entero.")
        return 

    # Se crea un objeto (una instancia) de nuestra clase 'Numero'.
    # Le pasamos el número que el usuario ingresó.
    mi_numero = Numero(entrada_usuario)

    # Se llama al método 'evaluarNumero()' del objeto 'mi_numero'
    # para que realice la evaluación y muestre el mensaje.
    mi_numero.evaluarNumero()

# Esta es una línea estándar en Python.
# Asegura que la función 'main()' se ejecute solo cuando el script es ejecutado directamente.
if __name__ == "__main__":
    main()