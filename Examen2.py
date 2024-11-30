print("Fco. San. Car. Cor 0421 ")
print(" ")

class persona:
    # el metodo init inicializa el nombre y la edad de la persona
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # el metodo mostrar muestra los datos de la persona
    def mostrar(self):
        print(f"hola, soy {self.nombre} y tengo {self.edad} años")

    # el metodo siesmayor verifica si la persona es mayor de edad
    def siesmayor(self):
        if self.edad >= 18:
            print(f"{self.nombre} es mayor de edad")
        else:
            print(f"{self.nombre} es menor de edad")

# creamos una persona de ejemplo
persona6 = persona("Santiago", 16)
persona6.mostrar()
persona6.siesmayor()
print(" ")

