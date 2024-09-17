from abc import ABC, abstractmethod

from src.gestorAplicacion.manejoLocal.Fecha import Fecha
from src.gestorAplicacion.mixins import Identificable


class Producto(ABC, Identificable):
    # Constructores
    # Constructor con todos los atributos menos Id
    def __init__(self, nombre:str, precio:float, cantidad:int, cantidadInicial:int, prestable:bool, condicion:int, fecha_lanzamiento:Fecha, descuento:float, puntosRequeridos:int):
        super().__init__()
        self._nombre = nombre
        self._precio = precio
        self._cantidad = cantidad
        self._cantidad_inicial = cantidadInicial
        self._prestable = prestable
        self._condicion = condicion
        self._fecha_lanzamiento = fecha_lanzamiento
        self._descuento = descuento
        self._puntos_requeridos = puntosRequeridos


    # ~~~~~ Metodos ~~~~~

    # Metodo para calcular las ventas en base a la cantidad inicial y la actual
    # (recordemos que la cantidad inicial se reinicia cada mes)
    def calcular_ventas(self):
        return self._cantidad_inicial - self._cantidad
    #Diccionario de prioridad para el orden


    # TODO metodos para ordenar productos por defecto
    @classmethod
    def ordenar(cls, parametro:str, lista):
        if parametro.lower() == "nombre":
            lista.sort(key=lambda x:x.get_nombre())
        elif parametro.lower() == "precio":
            lista.sort(key=lambda x:x.get_precio(), reverse=True)
        elif parametro.lower() == "ventas":
            lista.sort(key=lambda x:x.calcular_ventas(),reverse=True)
        elif parametro.lower() == "prioridad":
            prio = {"prioridad muy alta": 1, "prioridad alta": 2, "prioridad media": 3, "prioridad baja": 4}
            lista.sort(key=lambda x:prio[x.getPrioridad()])


    # TODO metodo para clonar producto

    # Metodo toString...?
    @abstractmethod
    def __str__(self):
        return f"ID: {self._id}, Nombre: {self._nombre}"


    # ~~~~~ Getters y Setters ~~~~~
    def get_id(self):
        return self._id
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
    def get_cantidad_inicial(self):
        return self._cantidad_inicial
    def set_cantidad_inicial(self, cantidadInicial):
        self._cantidad_inicial = cantidadInicial
    def is_prestable(self):
        return self._prestable
    def set_prestable(self, prestable):
        self._prestable = prestable
    def get_condicion(self):
        return self._condicion
    def set_condicion(self, condicion):
        self._condicion = condicion
    def get_fecha_lanzamiento(self):
        return self._fecha_lanzamiento
    def get_descuento(self):
        return self._descuento
    def set_descuento(self, descuento):
        self._descuento = descuento
    def get_puntos_requeridos(self):
        return self._puntos_requeridos
    def set_puntos_requeridos(self, puntosRequeridos):
        self._puntos_requeridos = puntosRequeridos


