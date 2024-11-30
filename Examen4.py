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

# creamos una calculadora de ejemplo
calc = calculadora(12, 6)
print("suma:", calc.suma())
print("resta:", calc.resta())
print("multiplicacion:", calc.multiplicacion())
print("division:", calc.division())
print(" ")
