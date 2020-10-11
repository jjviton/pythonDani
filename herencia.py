class Humano:
    def __init__(self,edad):
        self.edad = edad

    def hablar (self,mensaje):
        print (mensaje)

class IngSistemas(Humano):
    def __init__(self):
        print ("Hola")
    def programar(self,lenguaje):
        print ("Voy a programar en", lenguaje)


class LicDerecho(Humano):
    def estudiarCaso(self,de):
        print ("Debo estudiar el caso de", de)


pedro = IngSistemas()
raul = LicDerecho(21)

pedro.programar("Python")

raul.estudiarCaso("Juan")


pedro.hablar("Adios")

raul.hablar("Adios, Pedro")
