class Persona():


    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print(f'Ando caminando y me llamo {self.nombre}')

class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
       print(f'No ando caminado, ando en  mi bicicleta y me llamo {self.nombre}')


def run():
    persona = Persona('Juan')
    persona.avanza()

    ciclista = Ciclista('Pedro')
    ciclista.avanza()
    


if __name__ == '__main__':
    run()

   

