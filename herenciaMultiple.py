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
    def __init__(sefl,escuela):
        print ("Lic. en derecho egresado de:", escuela)
    def estudiarCaso(self,de):
        print ("Debo estudiar el caso de", de)

class estudioso(LicDerecho,IngSistemas):
    pass

pepe = estudioso("Gredos")

pepe.hablar("Hola soy de herencia multiple")
pepe.programar("C++")
pepe.estudiarCaso("Juan")


