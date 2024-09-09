from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, cedula, nombre, correo, telefono):
        self._cedula = cedula
        self._nombre = nombre
        self._correo = correo
        self._telefono = telefono

    #Getters y setters
    def get_cedula(self):
        return self._cedula
    def get_nombre(self):
        return self._nombre
    def get_correo(self):
        return self._correo
    def get_telefono(self):
        return self._telefono

    def set_cedula(self, cedula):
        self._cedula = cedula
    def set_nombre(self, nombre):
        self._nombre = nombre
    def set_correo(self, correo):
        self._correo = correo
    def set_telefono(self, telefono):
        self._telefono = telefono

    @abstractmethod
    def metodo_abstracto(self):
        pass