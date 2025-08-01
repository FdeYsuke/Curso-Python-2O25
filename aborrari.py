sers golds Downloads > TAREASUMAR.py >
class Numero:
def Init (self, numero):
numero Fixed: was using instead of self.numero
def evaluarlkumero(self):
If self.numero % 2 != 0: #Fixed: was using self. Nimero
print("El Müsero es Impar")
If self.numого - 7:
print("El Número ingresado es Comodin")
else:
print("El Musero es Par")
If self.numero 10:
print("El Nomero Ingresado es un Comodin")
def sumar(self, numero a sumar):
return self.numero numero a sumar
@staticmethod Added decorator
def main():
Try:
valor ingresado int(input("Ingrese un Nimero: ")) Fixed capitalization
numero obj Numero(valor_ingresado) Fixed: was using instead of
numero_obj.evaluarNumero() #Fixed: was colling evaluar)
suma numero_obj.sumar(2)
print(f La Suma es: (suma)") Fixed Indentation
except ValueError:
print("Por favor Ingrese un número välido")