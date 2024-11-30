print("Fco. San. Car. Cor 0421 ")
print(" ")
class calculadora:
    # el metodo init inicializa los dos numeros
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    # el metodo suma suma los dos numeros
    def suma(self):
        return self.num1 + self.num2

    # el metodo resta resta los dos numeros
    def resta(self):
        return self.num1 - self.num2

    # el metodo multiplicacion multiplica los dos numeros
    def multiplicacion(self):
        return self.num1 * self.num2

    # el metodo division divide los dos numeros
    def division(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "padre, no se puede dividir entre 0"
# Pedir los datos al usuario
try:
    num1 = float(input("introduce el primer numero: "))
    num2 = float(input("introduce el segundo numero: "))
    
    # Crear una calculadora con los nemeros introducidos
    calc = calculadora(num1, num2)
    
    # Mostrar los resultados de las operaciones
    print("suma:", calc.suma())
    print("resta:", calc.resta())
    print("multiplicacion:", calc.multiplicacion())
    print("division:", calc.division())
    print(" ")
except ValueError:
    print("Por favor, ingresa valores numericos validos")
print(" ")
