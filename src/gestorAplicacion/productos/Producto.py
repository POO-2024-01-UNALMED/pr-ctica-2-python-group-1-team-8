from abc import ABC, abstractmethod
from audioop import reverse

from src.gestorAplicacion.manejoLocal.Fecha import Fecha
class Producto(ABC):
    ultimoId = 1

    # Constructores
    # Constructor con todos los atributos menos Id
    def __init__(self, nombre:str, precio:float, cantidad:int, cantidadInicial:int, prestable:bool, condicion:int, fechaLanzamiento:Fecha, descuento:float, puntosRequeridos:int):
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
        return self._cantidadInicial - self._cantidad
    #Diccionario de prioridad para el orden


    # TODO metodos para ordenar productos por defecto
    @classmethod
    def ordenar(cls, parametro:str, lista):
        if parametro.lower() == "nombre":
            lista.sort(key=lambda x:x.getNombre())
        elif parametro.lower() == "precio":
            lista.sort(key=lambda x:x.getPrecio(),reverse=True)
        elif parametro.lower() == "ventas":
            lista.sort(key=lambda x:x.calcular_ventas(),reverse=True)
        elif parametro.lower() == "prioridad":
            prio = {"prioridad muy alta": 1, "prioridad alta": 2, "prioridad media": 3, "prioridad baja": 4}
            lista.sort(key=lambda x:prio[x.getPrioridad()])


    # TODO metodo para clonar producto

    # Metodo toString...?
    def __str__(self):
        return f"ID: {self.id}, Nombre: {self._nombre}, Precio: {self._precio}, Cantidad: {self._cantidad}, Condicion: {self._condicion}, Fecha de Lanzamiento: {self._fechaLanzamiento}"

    @abstractmethod
    def metodo_abstracto(self):
        pass


    # ~~~~~ Getters y Setters ~~~~~
    def getId(self):
        return self.id
    def getNombre(self):
        return self._nombre
    def setNombre(self, nombre):
        self._nombre = nombre
    def getPrecio(self):
        return self._precio
    def setPrecio(self, precio):
        self._precio = precio
    def getCantidad(self):
        return self._cantidad
    def setCantidad(self, cantidad):
        self._cantidad = cantidad
    def getCantidadInicial(self):
        return self._cantidadInicial
    def setCantidadInicial(self, cantidadInicial):
        self._cantidadInicial = cantidadInicial
    def isPrestable(self):
        return self._prestable
    def setPrestable(self, prestable):
        self._prestable = prestable
    def getCondicion(self):
        return self._condicion
    def setCondicion(self, condicion):
        self._condicion = condicion
    def getFechaLanzamiento(self):
        return self._fechaLanzamiento

    def getDescuento(self):
        return self._descuento
    def setDescuento(self, descuento):
        self._descuento = descuento
    def getPuntosRequeridos(self):
        return self._puntosRequeridos
    def setPuntosRequeridos(self, puntosRequeridos):
        self._puntosRequeridos = puntosRequeridos


