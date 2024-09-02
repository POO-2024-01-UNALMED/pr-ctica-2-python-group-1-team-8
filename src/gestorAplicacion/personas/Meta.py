from src.gestorAplicacion.manejoLocal.Fecha import Fecha


class Meta:
    ultimo_id = 1

    def __init__(self, empleado, dia_limite, mes_limite, year_limite, valor_alcanzar, valor_bonificacion):
        self._codigo = Meta.ultimo_id
        Meta.ultimo_id += 1
        self._empleado = empleado
        self._fecha = Fecha(dia_limite, mes_limite, year_limite)
        self._valor_alcanzar = valor_alcanzar
        self._valor_bonificacion = valor_bonificacion
        empleado.ingresar_meta(self)
        self._estado = "En proceso"
        self._acumulado = 0

    #Metodos
    def incrementar_acumulado(self, valor):
        if self._estado == "En proceso":
            self._empleado.acumulado += valor

    # Getters y setters
    def get_codigo(self):
        return self._codigo
    def get_empleado(self):
        return self._empleado
    def get_fecha(self):
        return self._fecha
    def get_valor_alcanzar(self):
        return self._valor_alcanzar
    def get_valor_bonificacion(self):
        return self._valor_bonificacion
    def get_estado(self):
        return self._estado
    def get_acumulado(self):
        return self._acumulado

    def set_codigo(self, codigo):
        self._codigo = codigo
    def set_empleado(self, empleado):
        self._empleado = empleado
    def set_fecha(self, fecha):
        self._fecha = fecha
    def set_valor_alcanzar(self, valor_alcanzar):
        self._valor_alcanzar = valor_alcanzar
    def set_valor_bonificacion(self, valor_bonificacion):
        self._valor_bonificacion = valor_bonificacion
    def set_estado(self, estado):
        self._estado = estado
    def set_acumulado(self, acumulado):
        self._acumulado = acumulado

    #Metodo toString
    def __str__(self):
        return f"* Codigo de meta: {self.get_codigo()} | Valor a alcanzar: {self.get_valor_alcanzar()} | Valor de bonificación: {self.get_valor_bonificacion()} | Fecha limite: {self.get_fecha().__str__()}, Estado: {self.estado}"