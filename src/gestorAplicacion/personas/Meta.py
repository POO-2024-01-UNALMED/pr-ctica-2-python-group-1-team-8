from src.gestorAplicacion.manejoLocal.Fecha import Fecha


class Meta:
    ultimo_id = 1

    def __init__(self, empleado, dia_limite, mes_limite, year_limite, valor_alcanzar, valor_bonificacion):
        self.__codigo = Meta.ultimo_id
        Meta.ultimo_id += 1
        self.__empleado = empleado
        self.__fecha = Fecha(dia_limite, mes_limite, year_limite)
        self.__valor_alcanzar = valor_alcanzar
        self.__valor_bonificacion = valor_bonificacion
        empleado.ingresar_meta(self)
        self.__estado = "En proceso"
        self.__acumulado = 0

    #Metodos
    def incrementar_acumulado(self, valor):
        if self.__estado == "En proceso":
            self.__empleado.acumulado += valor

    # Getters y setters
    def get_codigo(self):
        return self.__codigo
    def get_empleado(self):
        return self.__empleado
    def get_fecha(self):
        return self.__fecha
    def get_valor_alcanzar(self):
        return self.__valor_alcanzar
    def get_valor_bonificacion(self):
        return self.__valor_bonificacion
    def get_estado(self):
        return self.__estado
    def get_acumulado(self):
        return self.__acumulado

    def set_codigo(self, codigo):
        self.__codigo = codigo
    def set_empleado(self, empleado):
        self.__empleado = empleado
    def set_fecha(self, fecha):
        self.__fecha = fecha
    def set_valor_alcanzar(self, valor_alcanzar):
        self.__valor_alcanzar = valor_alcanzar
    def set_valor_bonificacion(self, valor_bonificacion):
        self.__valor_bonificacion = valor_bonificacion
    def set_estado(self, estado):
        self.__estado = estado
    def set_acumulado(self, acumulado):
        self.__acumulado = acumulado

    #Metodo toString
    def __str__(self):
        return f"* Codigo de meta: {self.get_codigo()} | Valor a alcanzar: {self.get_valor_alcanzar()} | Valor de bonificación: {self.get_valor_bonificacion()} | Fecha limite: {self.get_fecha().__str__()}, Estado: {self.estado}"