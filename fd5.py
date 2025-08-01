class Numero:
    # El método __init__ es el constructor de la clase.
    # Se ejecuta automáticamente cuando creas un nuevo objeto (ej: mi_numero = Numero(5)).
    # 'self' se refiere al objeto actual, y 'numero_recibido' es el valor que pasamos.
    def __init__(self, numero_recibido):
        # Aquí definimos un atributo del objeto: 'self.valor' guardará el número.
        self.valor = numero_recibido

    def evaluarNumero(self):
        """
        Evalúa el número almacenado en el atributo 'self.valor' del objeto.
        Determina si es par o impar, maneja mensajes especiales para 7 y 10.
        Si el número es par (incluido el 10), realiza una suma de numero + 2 y la imprime.
        """
        # Accedemos al número usando 'self.valor'
        numero_actual = self.valor

        # --- Paso 1: Manejar condiciones especiales (10 y 7) ---
        # Es crucial que estas condiciones se evalúen primero para que sus mensajes
        # específicos tengan prioridad sobre el mensaje general de par/impar.
        if numero_actual == 10:
            print("El número ingresado es 10")
            # Para el número 10, después de su mensaje específico,
            # también queremos que se imprima "El número ingresado es par" y se haga la suma.
            # Por lo tanto, NO usamos 'return' aquí, permitiendo que el código continúe.
        elif numero_actual == 7:
            print("Se ha ingresado un comodín")
            return # Si el número es 7, es un caso especial y el método termina aquí.

        # --- Paso 2: Determinar si es par o impar y realizar la suma si es par ---
        # Accedemos al número de nuevo con 'self.valor'
        if (numero_actual % 2) == 0:
            # Si el número es par (esto incluye el caso del 10 que pasó la primera condición),
            # imprimimos el mensaje de "par".
            print("El número ingresado es par")

            # Ahora, realizamos la suma de "número + 2" como se solicitó para todos los pares.
            resultado_suma_par = numero_actual + 2
            print(f"La suma realizada es: {resultado_suma_par}")
        else:
            # Si el número no es par (y no fue 7), entonces es impar.
            print("El número ingresado es impar")

    def sumar(self, numero_a_sumar):
        """
        Este método suma el número almacenado en el objeto ('self.valor')
        con otro número ('numero_a_sumar') y devuelve el resultado.
        """
        return self.valor + numero_a_sumar

# --- Función Principal (main) ---
# Esta función es el punto de entrada de tu programa y organiza el flujo.
def main():
    print("=== Evaluador de Números (Con Clase y Objeto) ===")

    # --- Solicitud y evaluación del número ingresado por el usuario ---
    try:
        # Pedimos al usuario que ingrese un número.
        # input() siempre devuelve texto, así que usamos int() para convertirlo a un número entero.
        numero_ingresado = int(input("Ingrese un número para la evaluación: "))
    except ValueError:
        # Manejamos el error si el usuario no ingresa un número válido.
        print("Entrada inválida. Por favor, ingrese un número entero.")
        return # Salimos de la función main si hay un error.

    # --- Creación de un objeto de la clase Numero ---
    # Aquí estamos creando un 'objeto' llamado 'mi_numero_evaluar'
    # de la 'clase' Numero. Le pasamos 'numero_ingresado' para que sea su atributo 'valor'.
    mi_numero_evaluar = Numero(numero_ingresado)

    print("\n--- Resultado de la Evaluación ---")
    # --- Invocación de un método del objeto ---
    # Llamamos al método 'evaluarNumero()' del objeto 'mi_numero_evaluar'.
    # Este método utiliza el atributo 'self.valor' del objeto para hacer las comprobaciones.
    mi_numero_evaluar.evaluarNumero()

    # --- Ejemplo adicional: Uso del método 'sumar' ---
    # Si quieres mostrar cómo se usa el método 'sumar' con el objeto:
    print("\n--- Demostración del método 'sumar' ---")
    # Vamos a sumar 5 al número que se ingresó inicialmente.
    numero_a_sumar_ejemplo = 5
    # Llamamos al método 'sumar' del objeto 'mi_numero_evaluar'.
    # Este método devolverá la suma de 'numero_ingresado' + 5.
    resultado_ejemplo_suma = mi_numero_evaluar.sumar(numero_a_sumar_ejemplo)
    print(f"Si sumamos {mi_numero_evaluar.valor} + {numero_a_sumar_ejemplo}, el resultado es: {resultado_ejemplo_suma}")


# Esta es una línea estándar en Python.
# Asegura que la función 'main()' se ejecute solo cuando el script es ejecutado directamente.
if __name__ == "__main__":
    main()