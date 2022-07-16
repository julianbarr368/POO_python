class Lavadora():

    def __init__(self):
        pass

    def lavar (self, temperatura = 'caliente', carga = 50):
        self._sensado_cantidad_carga(carga)
        self._llenar_con_agua(temperatura, carga)
        self._cargar_jabon()
        self._lavar()
        self._centrifugar()

    def _sensado_cantidad_carga(self, carga):
        if carga == 50:
            print("Capacidad al 50%")
        elif carga == 100:
            print("Capacidad al 100%")
        else:
            print('No se detecto la carga')
        return carga

    def _llenar_con_agua(sel, temperatura, carga):
        print(f'llenado el agua hasta el {carga} % de capacidad con agua {temperatura}')
    
    def _cargar_jabon(self):
        print('Añadiendo jabon')

    def _lavar(self):
         print('Se esta lavando')
    
    def _centrifugar(self):
         print('Se esta centrifugando')


if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar()
