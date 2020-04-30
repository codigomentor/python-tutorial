class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrarMensaje(self):
        print("Yo soy una funcion")

class Estudiante(Persona):
    def __init__(self, nombre, edad):
        Persona.__init__(self, nombre, edad)

estudiante = Estudiante("Boris", 30)
estudiante.mostrarMensaje() # Yo soy una funcion