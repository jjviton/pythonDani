class Prueba(object):
    def __init__(self):
        self.__privado = "Soy Privado"
        self.privado = "Soy Publico"

    def __metodoPrivado(self):
        return "Soy Privado"

    def metodoPublico(self):
        print ("Soy Publico")

    def getPrivado(self):
        return self.__privado

    def setPrivado(self,valor):
        self.__privado = self.__metodoPrivado()


obj = Prueba()

obj.setPrivado("tengo nuevo valor")
print (obj.getPrivado())
