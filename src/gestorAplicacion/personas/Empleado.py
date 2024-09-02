from src.gestorAplicacion.personas.Persona import Persona


class Empleado(Persona):
    def __init__(self, cedula, nombre, correo, telefono, salario, salario_porcentual, dias_laborales, tienda):
        super().__init__(cedula, nombre, correo, telefono)
        self._salario = salario
        self._salario_porcentual = salario_porcentual
        self._dias_laborales = dias_laborales
        self._tienda = tienda

    # Getters y setters
    def get_salario(self):
        return self.salario
    def get_salario_porcentual(self):
        return self.salario_porcentual
    def get_dias_laborales(self):
        return self.dias_laborales
    def get_tienda(self):
        return self.tienda

    def set_salario(self, salario):
        self.salario = salario
    def set_salario_porcentual(self, salario_porcentual):
        self.salario_porcentual = salario_porcentual
    def set_dias_laborales(self, dias_laborales):
        self.dias_laborales = dias_laborales
    def set_tienda(self, tienda):
        self.tienda = tienda

    def metodo_abstracto(self):
        pass