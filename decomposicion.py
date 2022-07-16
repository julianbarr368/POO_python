from asyncio import run_coroutine_threadsafe
from xml.etree.ElementTree import SubElement


class Automovil():

    def __init__(self,modelo ,marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en_reposo' # Atributo privado que no se va a mostar.
        self._motor = Motor(cilindros = 4)

    def acelerar(self, tipo = "despacio"):
        if tipo == "rapido":
            self.inyecta_gasolina(10)
        else:
            self.inyecta_gasolina(3)
        self._estado = "en_movimiento"

class Motor():

    def __init__(self, cilindros, tipo = "Gasolina"):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

    def inyecta_gasolina(self, cantidad):
        pass

class Acesorios():

    def __init__(self, ruedas, pantalla, tapizado):
        self.ruedas = ruedas
        self.pantalla = pantalla
        self.tapizado = tapizado

    def tipo_modelo(selt, baja_gama, media_gama, alta_gama):
        pass
