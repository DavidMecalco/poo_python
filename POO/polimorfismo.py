
class Persona:

#definimos el metodo constructor

    def __init__(self, nombre):
        self.nombre = nombre
    
    def avanza(self):
        print('Ando caminando')

#Subclase
class Ciclista(Persona):

    def __init__(self, nombre):
#Referencía a la superclase
        super().__init__(nombre)

    def avanza(self):
        print('Ando en bicicleta')

def main():
    persona = Persona('David')
    persona.avanza()

    ciclista = Ciclista('Daniel')
    ciclista.avanza()

if __name__ == "__main__":
    main()
