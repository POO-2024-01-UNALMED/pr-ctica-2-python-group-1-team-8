from src.gestorAplicacion.productos.Producto import Producto
from src.gestorAplicacion.manejoLocal.Fecha import Fecha
from src.gestorAplicacion.productos.Juego import Juego


class Consola(Producto):
    def __init__(self, nombre:str, precio:float, cantidad:int, cantidadInicial:int, prestable:bool, condicion:int, fecha_lanzamiento:Fecha, descuento:float, puntosRequeridos:int, marca:str):
        super().__init__(nombre, precio, cantidad, cantidadInicial, prestable, condicion, fecha_lanzamiento, descuento, puntosRequeridos)
        self._marca = marca

    def __str__(self):
        return f"{self._id} | {self._nombre} | Marca: {self._marca}"

    def get_marca(self):
        return self._marca
    def set_marca(self, marca):
        self._marca = marca

    def __repr__(self):
        return f"COD: {self.get_id()} |Nombre: {self.get_nombre()} | Precio: {self.get_precio()} | Marca: {self.get_marca()}"