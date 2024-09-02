import Producto
class Juego(Producto):
    def __init__(self, nombre, precio, cantidad, cantidadInicial, prestable, condicion, fechaLanzamiento, descuento, puntosRequeridos, genero,plataforma):
        super().__init__(nombre, precio, cantidad, cantidadInicial, prestable, condicion, fechaLanzamiento, descuento, puntosRequeridos)
        self.__plataforma = plataforma
        self.__genero = genero

    def __str__(self):
        return f"Nombre: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}, Plataforma: {self.plataforma}"

    # ~~~~~ Getters y Setters ~~~~~
    def get_plataforma(self):
        return self.__plataforma
    def set_plataforma(self, plataforma):
        self.__plataforma = plataforma
    def get_genero(self):
        return self.__genero
    def set_genero(self, genero):
        self.__genero = genero