from src.gestorAplicacion.personas.Persona import Persona

class Empleado(Persona):
    def __init__(self, cedula, nombre, correo, telefono, salario, salario_porcentual, acumulado_mensual, dias_laborales, tienda):
        super().__init__(cedula, nombre, correo, telefono)
        self.__salario = salario
        self.__salario_porcentual = salario_porcentual
        self.__acumulado_mensual = acumulado_mensual
        self.__dias_laborales = dias_laborales
        self.__tienda = tienda
        self.__metas = []
        self.__metas_alcanzadas = []
        self.__metas_caducadas = []
        self.__transacciones = []

    # Metodos
    def ingresar_meta(self, meta):
        self.metas.append(meta)
    def ingresar_meta_alcanzada(self, meta):
        self.metas_alcanzadas.append(meta)
    def ingresar_meta_caducada(self, meta):
        self.metas_caducadas.append(meta)
    def ingresar_transaccion(self, transaccion):
        self.transacciones.append(transaccion)

    # Getters y setters
    def get_salario(self):
        return self.salario
    def get_salario_porcentual(self):
        return self.salario_porcentual
    def get_acumulado_mensual(self):
        return self.acumulado_mensual
    def get_dias_laborales(self):
        return self.dias_laborales
    def get_tienda(self):
        return self.tienda
    def get_metas(self):
        return self.metas
    def get_metas_alcanzadas(self):
        return self.metas_alcanzadas
    def get_metas_caducadas(self):
        return self.metas_caducadas
    def get_transacciones(self):
        return self.transacciones

    def set_salario(self, salario):
        self.salario = salario
    def set_salario_porcentual(self, salario_porcentual):
        self.salario_porcentual = salario_porcentual
    def set_acumulado_mensual(self, acumulado_mensual):
        self.acumulado_mensual = acumulado_mensual
    def set_dias_laborales(self, dias_laborales):
        self.dias_laborales = dias_laborales
    def set_tienda(self, tienda):
        self.tienda = tienda
    def set_metas(self, metas):
        self.metas = metas
    def set_metas_alcanzadas(self, metas_alcanzadas):
        self.metas_alcanzadas = metas_alcanzadas
    def set_metas_caducadas(self, metas_caducadas):
        self.metas_caducadas = metas_caducadas
    def set_transacciones(self, transacciones):
        self.transacciones = transacciones

    def metodo_abstracto(self):
        pass