print("Fco. San. Car. Cor 0421 ")
print(" ")
class alumno:
    # el metodo init inicializa los atributos del alumno
    def __init__(self, nombre, calificacion):
        self.nombre = nombre
        self.calificacion = calificacion

    # el metodo imprimir muestra el nombre y la calificacion
    def imprimir(self):
        print(f"el alumno {self.nombre} tiene una calificacion de {self.calificacion}")

    # el metodo resultado nos dice si aprobo o no
    def resultado(self):
        if self.calificacion >= 5:
            print(f"{self.nombre} ha aprobado con {self.calificacion}")
        else:
            print(f"{self.nombre} ha suspendido con {self.calificacion}")

# creamos un alumno de ejemplo
alumno6 = alumno("Santiagüito", 8)
alumno6.imprimir()
alumno6.resultado()
print(" ")