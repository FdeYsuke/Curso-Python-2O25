class Numero:
    def __init__(self, numero_recibido):
        self.valor = numero_recibido

    def evaluarNumero(self):
        numero_actual = self.valor

        if numero_actual == 10:
            print("El número ingresado es 10")
        elif numero_actual == 7:
            print("Se ha ingresado un comodín")
            return

        if (numero_actual % 2) == 0:
            print("El número ingresado es par")
            resultado_suma_par = numero_actual + 2
            print(f"La suma realizada es: {resultado_suma_par}")
        else:
            print("El número ingresado es impar")

    def sumar(self, numero_a_sumar):
        return self.valor + numero_a_sumar

def main():
    print("=== Evaluador de Números (Con Clase y Objeto) ===")

    try:
        numero_ingresado = int(input("Ingrese un número para la evaluación: "))
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")
        return 

    mi_numero_evaluar = Numero(numero_ingresado)

    print("\n--- Resultado de la Evaluación ---")
    mi_numero_evaluar.evaluarNumero()

if __name__ == "__main__":
    main()