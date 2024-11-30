print("Fco. San. Car. Cor 0421 ")
print(" ")

class agenda:
    # el metodo init inicializa una lista vacía para los contactos
    def __init__(self):
        self.contactos = []

    # el metodo añadir_contacto agrega un nuevo contacto
    def añadir_contacto(self, nombre, telefono, email):
        self.contactos.append({"nombre": nombre, "telefono": telefono, "email": email})
        print(f"contacto {nombre} añadido")

    # el metodo listadecontactos muestra todos los contactos
    def listadecontactos(self):
        for contacto in self.contactos:
            print(f"nombre: {contacto['nombre']}, telefono: {contacto['telefono']}, email: {contacto['email']}")

    # el metodo buscarelcontacto busca un contacto por nombre
    def buscarelcontacto(self, nombre):
        for contacto in self.contactos:
            if contacto['nombre'] == nombre:
                print(f"encontrado: {contacto}")
                return
        print(f"contacto {nombre} no encontrado")

    # el metodo editarelcontacto permite cambiar la informacion de un contacto
    def editarelcontacto(self, nombre, nuevotelefono, nuevoemail):
        for contacto in self.contactos:
            if contacto['nombre'] == nombre:
                contacto['telefono'] = nuevotelefono
                contacto['email'] = nuevoemail
                print(f"contacto {nombre} actualizado")
                return
        print(f"contacto {nombre} no encontrado")

# creamos una agenda de ejemplo
laagenda6 = agenda()
laagenda6.añadir_contacto("santiago", "6148285282", "santiagocarrasco320@email.com")
laagenda6.listadecontactos()
laagenda6.buscarelcontacto("santiago")
laagenda6.editarelcontacto("santiago", "123456789", "santiagocarrasco320@nuevoemail.com")
laagenda6.listadecontactos()
print(" ")
