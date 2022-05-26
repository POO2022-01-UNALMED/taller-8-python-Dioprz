from persona import Persona
from deportista import Deportista

class Futbolista(Persona, Deportista):

    listaFutbolistas = []

    def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil, deporte = "Futbol"):
        Persona.__init__(self,  nombre, edad, altura, sexo)
        Deportista.__init__(self,añosPracticando, deporte)
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        
    def __str__(self):
        return "Mi nombre es " + self.getNombre() + " soy profesional en el deporte " + self.getDeporte() + " Tengo " + str(self.getEdad) + " años de edad y llevo " + str(self.getAñosPracticando) + " años en el deporte"


    def getGolesMarcados(self):
        return self._golesMarcados

    def getTarjetasRojas(self):
        return self._tarjetasRojas

    def getPiernaHabil(self):
        return self._piernaHabil

    def setGolesMarcados(self, goles):
        self._golesMarcados = goles

    def setTarjetasRojas(self, tarjetas):
        self._tarjetasRojas = tarjetas

    def setPiernaHabil(self, pierna):
        self._piernaHabil = pierna

