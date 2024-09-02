from abc import ABC, abstractmethod

class Producto(ABC):
    ultimoId = 1

    # Constructores
    # Constructor con todos los atributos menos Id
    def __init__(self, nombre, precio, cantidad, cantidadInicial, prestable, condicion, fechaLanzamiento, descuento, puntosRequeridos):
        self.id = Producto.ultimoId
        Producto.ultimoId += 1
        self.__nombre = nombre
        self.__precio = precio
        self.__cantidad = cantidad
        self.__cantidadInicial = cantidadInicial
        self.__prestable = prestable
        self.__condicion = condicion
        self.__fechaLanzamiento = fechaLanzamiento
        self.__descuento = descuento
        self.__puntosRequeridos = puntosRequeridos


    # ~~~~~ Metodos ~~~~~

    # Metodo para calcular las ventas en base a la cantidad inicial y la actual
    # (recordemos que la cantidad inicial se reinicia cada mes)
    def calcular_ventas(self):
        return self.cantidadInicial - self.cantidad

    # TODO metodos para ordenar productos

    # TODO metodo para clonar producto

    # Metodo toString...?
    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.__nombre}, Precio: {self.__precio}, Cantidad: {self.__cantidad}, Condicion: {self.__condicion}, Fecha de Lanzamiento: {self.__fechaLanzamiento}"

    @abstractmethod
    def metodo_abstracto(self):
        pass


    # ~~~~~ Getters y Setters ~~~~~
    def get_id(self):
        return self.id
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def get_precio(self):
        return self.__precio
    def set_precio(self, precio):
        self.__precio = precio
    def get_cantidad(self):
        return self.__cantidad
    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad
    def get_cantidadInicial(self):
        return self.__cantidadInicial
    def set_cantidadInicial(self, cantidadInicial):
        self.__cantidadInicial = cantidadInicial
    def get_prestable(self):
        return self.__prestable
    def set_prestable(self, prestable):
        self.__prestable = prestable
    def get_condicion(self):
        return self.__condicion
    def set_condicion(self, condicion):
        self.__condicion = condicion
    def get_fechaLanzamiento(self):
        return self.__fechaLanzamiento

    def get_descuento(self):
        return self.__descuento
    def set_descuento(self, descuento):
        self.__descuento = descuento
    def get_puntosRequeridos(self):
        return self.__puntosRequeridos
    def set_puntosRequeridos(self, puntosRequeridos):
        self.__puntosRequeridos = puntosRequeridos
