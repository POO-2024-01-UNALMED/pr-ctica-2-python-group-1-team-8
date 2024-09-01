from abc import ABC, abstractmethod

class Producto(ABC):
    ultimoId = 1

    # Constructores
    # Constructor con todos los atributos menos Id
    def __init__(self, nombre, precio, cantidad, cantidadInicial, prestable, condicion, fechaLanzamiento, descuento, puntosRequeridos):
        self.id = Producto.ultimoId
        Producto.ultimoId += 1
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.cantidadInicial = cantidadInicial
        self.prestable = prestable
        self.condicion = condicion
        self.fechaLanzamiento = fechaLanzamiento
        self.descuento = descuento
        self.puntosRequeridos = puntosRequeridos


    # ~~~~~ Metodos ~~~~~

    # Metodo para calcular las ventas en base a la cantidad inicial y la actual
    # (recordemos que la cantidad inicial se reinicia cada mes)
    def calcular_ventas(self):
        return self.cantidadInicial - self.cantidad

    # TODO metodos para ordenar productos

    # TODO metodo para clonar producto

    # Metodo toString...?

    @abstractmethod
    def metodo_abstracto(self):
        pass