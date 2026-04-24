class Persona:

    # Metodo constructor de la clase
    def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    # Metodo para mostrar los datos de la persona
    def mostrarpersona(self):
        print("nombre: ", self.nombre)
        print("apellidos: ", self.apellidos)
        print("edad: ", self.edad)

def main():
    print("vamos a aprender POO...")
    persona_1 = Persona("Lorenzo", "Perez", 18)
    persona_1.mostrarpersona()

if __name__ == "__main__":
    main()