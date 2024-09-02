from src.gestorAplicacion.personas.Persona import Persona

class Cliente(Persona):
    clientes = []

    #Constructor
    def __init__(self, cedula, nombre, correo, telefono, puntos_fidelidad):
        super().__init__(cedula, nombre, correo, telefono)
        self._puntos_fidelidad = puntos_fidelidad
        self._prestamos = []
        self._compras = []
        Cliente.clientes.append(self)



    # Getters y setters
    def get_puntos_fidelidad(self):
        return self.puntos_fidelidad
    def get_prestamos(self):
        return self.prestamos
    def get_compras(self):
        return self.compras

    def set_puntos_fidelidad(self, puntos_fidelidad):
        self.puntos_fidelidad = puntos_fidelidad
    def set_prestamos(self, prestamos):
        self.prestamos = prestamos
    def set_compras(self, compras):
        self.compras = compras

    #Metodos
    def agregar_prestamo(self, prestamo):
        self.prestamos.append(prestamo)
    def agregar_compra(self, compra):
        self.compras.append(compra)

    def metodo_abstracto(self):
        pass
