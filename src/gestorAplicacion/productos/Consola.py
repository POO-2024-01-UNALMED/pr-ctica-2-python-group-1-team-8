from Producto import Producto

class Consola(Producto):
    def __init__(self, nombre, precio, cantidad,cantidadInicial, prestable, condicion, fechaLanzamiento, descuento, puntosRequeridos, marca):
        super().__init__(nombre, precio, cantidad,cantidadInicial, prestable, condicion, fechaLanzamiento, descuento, puntosRequeridos)
        self._marca = marca

    def __str__(self):
        return f"Nombre: {self._nombre}\nPrecio: {self._precio}\nCantidad: {self._cantidad}\nMarca: {self._marca}"

    def getMarca(self):
        return self._marca
    def setMarca(self, marca):
        self._marca = marca

    def metodo_abstracto(self):
        pass