import Producto

class Consola(Producto):
    def __init__(self, nombre, precio, cantidad,cantidadInicial, prestable, condicion, fechaLanzamiento, descuento, puntosRequeridos, marca):
        super().__init__(nombre, precio, cantidad,cantidadInicial, prestable, condicion, fechaLanzamiento, descuento, puntosRequeridos)
        self._marca = marca

    def __str__(self):
        return f"Nombre: {self.nombre}\nPrecio: {self.precio}\nCantidad: {self.cantidad}\nMarca: {self.marca}"

    def get_marca(self):
        return self.marca
    def set_marca(self, marca):
        self._marca = marca