from abc import ABC, abstractmethod

class Producto(ABC):
    ultimoId = 1

    # Constructores
    # Constructor con todos los atributos menos Id
    def __init__(self, nombre, precio, cantidad, cantidadInicial, prestable, condicion, fechaLanzamiento, descuento, puntosRequeridos):
        self.id = Producto.ultimoId
        Producto.ultimoId += 1
        self._nombre = nombre
        self._precio = precio
        self._cantidad = cantidad
        self._cantidadInicial = cantidadInicial
        self._prestable = prestable
        self._condicion = condicion
        self._fechaLanzamiento = fechaLanzamiento
        self._descuento = descuento
        self._puntosRequeridos = puntosRequeridos


    # ~~~~~ Metodos ~~~~~

    # Metodo para calcular las ventas en base a la cantidad inicial y la actual
    # (recordemos que la cantidad inicial se reinicia cada mes)
    def calcular_ventas(self):
        return self.cantidadInicial - self.cantidad

    # TODO metodos para ordenar productos por defecto
    @classmethod
    def ordenar(cls,parametro:str,lista):
        if parametro.lower() == "nombre":
            sorted(lista,key=lambda x:x.__nombre)
        elif parametro.lower() == "precio":
            sorted(lista,key=lambda x:x.__precio)
        elif parametro.lower() == "ventas":
            sorted(lista,key=lambda x:x.calcular_ventas())

    # TODO metodo para clonar producto

    # Metodo toString...?
    def __str__(self):
        return f"ID: {self.id}, Nombre: {self._nombre}, Precio: {self._precio}, Cantidad: {self._cantidad}, Condicion: {self._condicion}, Fecha de Lanzamiento: {self._fechaLanzamiento}"

    @abstractmethod
    def metodo_abstracto(self):
        pass


    # ~~~~~ Getters y Setters ~~~~~
    def get_id(self):
        return self.id
    def get_nombre(self):
        return self._nombre
    def set_nombre(self, nombre):
        self._nombre = nombre
    def get_precio(self):
        return self._precio
    def set_precio(self, precio):
        self._precio = precio
    def get_cantidad(self):
        return self._cantidad
    def set_cantidad(self, cantidad):
        self._cantidad = cantidad
    def get_cantidadInicial(self):
        return self._cantidadInicial
    def set_cantidadInicial(self, cantidadInicial):
        self._cantidadInicial = cantidadInicial
    def get_prestable(self):
        return self._prestable
    def set_prestable(self, prestable):
        self._prestable = prestable
    def get_condicion(self):
        return self._condicion
    def set_condicion(self, condicion):
        self._condicion = condicion
    def get_fechaLanzamiento(self):
        return self._fechaLanzamiento

    def get_descuento(self):
        return self._descuento
    def set_descuento(self, descuento):
        self._descuento = descuento
    def get_puntosRequeridos(self):
        return self._puntosRequeridos
    def set_puntosRequeridos(self, puntosRequeridos):
        self._puntosRequeridos = puntosRequeridos
