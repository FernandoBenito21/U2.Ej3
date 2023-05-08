import os
import datetime

class Registro:
    __temperatura = 0
    __humedad = 0
    __presion = 0
    def __init__(self,temp,humedad,presion):
        self.__temperatura = temp
        self.__humedad = humedad
        self.__presion = presion
    def getTemperatura(self):
        return self.__temperatura
    def getHumedad(self):
        return self.__humedad
    def getPresion(self):
        return self.__presion