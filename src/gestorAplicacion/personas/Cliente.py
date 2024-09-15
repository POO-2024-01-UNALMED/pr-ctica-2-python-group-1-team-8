from multimethod import multimethod

from src.gestorAplicacion.personas.Persona import Persona

class Cliente(Persona):
    clientes = []

    # Constructor
    @multimethod
    def __init__(self, cedula, nombre, correo, telefono, puntos_fidelidad):
        super().__init__(cedula, nombre, correo, telefono)
        self._puntos_fidelidad = puntos_fidelidad
        self._prestamos = []
        self._compras = []
        Cliente.clientes.append(self)

    # Constructor sin puntos de fidelidad
    @multimethod
    def __init__(self, cedula, nombre, correo, telefono):
        super().__init__(cedula, nombre, correo, telefono)
        self._puntos_fidelidad = 0
        self._prestamos = []
        self._compras = []
        Cliente.clientes.append(self)

    @staticmethod
    def buscar_cliente(cedula):
        for c in Cliente.clientes:
            if c.get_cedula() == cedula:
                return c
        return None

    # Getters y setters
    def get_puntos_fidelidad(self):
        return self._puntos_fidelidad
    def get_prestamos(self):
        return self._prestamos
    def get_compras(self):
        return self._compras

    def set_puntos_fidelidad(self, puntos_fidelidad):
        self._puntos_fidelidad = puntos_fidelidad
    def set_prestamos(self, prestamos):
        self._prestamos = prestamos
    def set_compras(self, compras):
        self._compras = compras

    #Metodos
    def agregar_prestamo(self, prestamo):
        self._prestamos.append(prestamo)
    def agregar_compra(self, compra):
        self._compras.append(compra)

    def metodo_abstracto(self):
        pass
