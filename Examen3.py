print("Fco. San. Car. Cor 0421 ")
print(" ")
class triangulo:
    # el metodo init inicializa los tres lados del triangulo
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    # el metodo tipo determina el tipo de triangulo
    def tipo(self):
        if self.lado1 == self.lado2 == self.lado3:
            print("es un triangulo equilatero")
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            print("es un triangulo isosceles")
        else:
            print("es un triangulo escaleno")

    # el metodo imprimir muestra el lado mayor
    def imprimir(self):
        mayor = max(self.lado1, self.lado2, self.lado3)
        print(f"el lado mayor es: {mayor}")

# creamos un triangulo de ejemplo
triangulo6 = triangulo(6, 8, 8)
triangulo6.imprimir()
triangulo6.tipo()
print(" ")
