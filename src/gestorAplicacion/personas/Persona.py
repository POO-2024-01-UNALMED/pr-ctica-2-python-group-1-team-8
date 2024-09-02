from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, cedula, nombre, correo, telefono):
        self._cedula = cedula
        self._nombre = nombre
        self._correo = correo
        self._telefono = telefono

    #Getters y setters
    def get_cedula(self):
        return self.cedula
    def get_nombre(self):
        return self.nombre
    def get_correo(self):
        return self.correo
    def get_telefono(self):
        return self.telefono

    def set_cedula(self, cedula):
        self.cedula = cedula
    def set_nombre(self, nombre):
        self.nombre = nombre
    def set_correo(self, correo):
        self.correo = correo
    def set_telefono(self, telefono):
        self.telefono = telefono

    @abstractmethod
    def metodo_abstracto(self):
        pass