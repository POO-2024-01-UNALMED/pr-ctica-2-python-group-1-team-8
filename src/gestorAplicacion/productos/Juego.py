import Producto
class Juego(Producto):
    def __init__(self, nombre, precio, cantidad, cantidadInicial, prestable, condicion, fechaLanzamiento, descuento, puntosRequeridos, genero,plataforma):
        super().__init__(nombre, precio, cantidad, cantidadInicial, prestable, condicion, fechaLanzamiento, descuento, puntosRequeridos)
        self._plataforma = plataforma
        self._genero = genero

    def __str__(self):
        return f"Nombre: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}, Plataforma: {self.plataforma}"

    # ~~~~~ Getters y Setters ~~~~~
    def get_plataforma(self):
        return self._plataforma
    def set_plataforma(self, plataforma):
        self._plataforma = plataforma
    def get_genero(self):
        return self._genero
    def set_genero(self, genero):
        self._genero = genero