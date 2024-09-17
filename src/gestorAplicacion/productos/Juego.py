from src.gestorAplicacion.productos.Producto import Producto

class Juego(Producto):
    def __init__(self, nombre, precio, cantidad, cantidadInicial, prestable, condicion, fechaLanzamiento, descuento, puntosRequeridos, genero,plataforma):
        super().__init__(nombre, precio, cantidad, cantidadInicial, prestable, condicion, fechaLanzamiento, descuento, puntosRequeridos)
        self._plataforma = plataforma
        self._genero = genero

    def __str__(self):
        return f"Nombre: {self._nombre}, Precio: {self._precio}, Cantidad: {self._cantidad}, Plataforma: {self._plataforma}"

    # ~~~~~ Getters y Setters ~~~~~
    def get_plataforma(self):
        return self._plataforma
    def set_plataforma(self, plataforma):
        self._plataforma = plataforma
    def get_genero(self):
        return self._genero
    def set_genero(self, genero):
        self._genero = genero

    def __repr__(self):
        return f"COD: {self.get_id()} |Nombre: {self.get_nombre()} | Precio: {self.get_precio()} | Plataforma: {self.get_plataforma()}"