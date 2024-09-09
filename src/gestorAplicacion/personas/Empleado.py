from src.gestorAplicacion.personas.Persona import Persona

class Empleado(Persona):
    def __init__(self, cedula, nombre, correo, telefono, salario, salario_porcentual, acumulado_mensual, dias_laborales, tienda):
        super().__init__(cedula, nombre, correo, telefono)
        self._salario = salario
        self._salario_porcentual = salario_porcentual
        self._acumulado_mensual = acumulado_mensual
        self._dias_laborales = dias_laborales
        self._tienda = tienda
        self._metas = []
        self._metas_alcanzadas = []
        self._metas_caducadas = []
        self._transacciones = []
        tienda.agregarEmpleado(self)

    # Metodos
    def ingresar_meta(self, meta):
        self.metas.append(meta)
    def ingresar_meta_alcanzada(self, meta):
        self.metas_alcanzadas.append(meta)
    def ingresar_meta_caducada(self, meta):
        self.metas_caducadas.append(meta)
    def ingresar_transaccion(self, transaccion):
        self.transacciones.append(transaccion)
    def __str__(self):
        return f"* Nombre: {self._nombre} - Cedula: {self._cedula}"

    # Getters y setters
    def get_salario(self):
        return self._salario
    def get_salario_porcentual(self):
        return self._salario_porcentual
    def get_acumulado_mensual(self):
        return self._acumulado_mensual
    def get_dias_laborales(self):
        return self._dias_laborales
    def get_tienda(self):
        return self._tienda
    def get_metas(self):
        return self._metas
    def get_metas_alcanzadas(self):
        return self._metas_alcanzadas
    def get_metas_caducadas(self):
        return self._metas_caducadas
    def get_transacciones(self):
        return self._transacciones

    def set_salario(self, salario):
        self._salario = salario
    def set_salario_porcentual(self, salario_porcentual):
        self._salario_porcentual = salario_porcentual
    def set_acumulado_mensual(self, acumulado_mensual):
        self._acumulado_mensual = acumulado_mensual
    def set_dias_laborales(self, dias_laborales):
        self._dias_laborales = dias_laborales
    def set_tienda(self, tienda):
        self._tienda = tienda
    def set_metas(self, metas):
        self._metas = metas
    def set_metas_alcanzadas(self, metas_alcanzadas):
        self._metas_alcanzadas = metas_alcanzadas
    def set_metas_caducadas(self, metas_caducadas):
        self._metas_caducadas = metas_caducadas
    def set_transacciones(self, transacciones):
        self._transacciones = transacciones

    def metodo_abstracto(self):
        pass