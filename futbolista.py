from persona import Persona
from deportista import Deportista

class Futbolista(Persona, Deportista):

    listaFutbolistas = []

    def __init__(self, golesMarcados, tarjetasRojas, piernaHabil, nombre, edad, altura, sexo, deporte, añosPracticando):
        Persona.__init__(self,  nombre, edad, altura, sexo)
        Deportista.__init__(self, deporte, añosPracticando)
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        
    def __str__(self):
        return "Mi nombre es " + self._nombre + " soy profesional en el deporte " + self._deporte + " Tengo " + self._edad + " años de edad y llevo " + self._añosPracticando + " años en el deporte"


    def getGolesMarcados():
        return self._golesMarcados

    def getTarjetasRojas():
        return self._tarjetasRojas

    def getPiernaHabil():
        return self._piernaHabil

    def setGolesMarcados(goles):
        self._golesMarcados = goles

    def setTarjetasRojas(tarjetas):
        self._tarjetasRojas = tarjetas

    def setPiernaHabil(pierna):
        self._piernaHabil = pierna

