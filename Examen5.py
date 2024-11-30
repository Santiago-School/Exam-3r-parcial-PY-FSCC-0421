print("fco. san. car. cor 0421 ")
print(" ")
class agenda:
    # el metodo init inicializa una lista vacia para los contactos
    def __init__(self):
        self.contactos = []

    # el metodo añadiruncontacto agrega un nuevo contacto
    def añadiruncontacto(self, nombre, telefono, email):
        self.contactos.append({"nombre": nombre, "telefono": telefono, "email": email})
        print(f"contacto {nombre} anadido")

    # el metodo listadecontactos muestra todos los contactos
    def listadecontactos(self):
        if len(self.contactos) == 0:
            print("no hay contactos en la agenda")
        else:
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

def mostrarelmenu():
    print("\nmenu de opciones:")
    print("1. anadir contacto")
    print("2. lista de contactos")
    print("3. buscar contacto")
    print("4. editar contacto")
    print("5. cerrar agenda")

# creamos una instancia de la agenda
miagenda = agenda()

# bucle principal
while True:
    mostrarelmenu()
    opcion = input("elige una opcion (1-5): ")

    if opcion == "1":
        nombre = input("introduce el nombre del contacto: ")
        telefono = input("introduce el telefono del contacto: ")
        email = input("introduce el email del contacto: ")
        miagenda.añadiruncontacto(nombre, telefono, email)

    elif opcion == "2":
        miagenda.listadecontactos()

    elif opcion == "3":
        buscarnombre = input("introduce el nombre del contacto a buscar: ")
        miagenda.buscarelcontacto(buscarnombre)

    elif opcion == "4":
        nombre_editar = input("introduce el nombre del contacto a editar: ")
        nuevotelefono = input("introduce el nuevo telefono: ")
        nuevoemail = input("introduce el nuevo email: ")
        miagenda.editarelcontacto(nombre_editar, nuevotelefono, nuevoemail)

    elif opcion == "5":
        print("cerrando agenda...")
        break

    else:
        print("opcion no valida, por favor elige entre 1 y 5")
