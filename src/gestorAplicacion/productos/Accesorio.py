from src.gestorAplicacion.productos.Producto import Producto

class Accesorio(Producto):
    def __init__(self, nombre, precio, cantidad, cantidadInicial, prestable, condicion, fecha_lanzamiento, descuento, puntosRequeridos, marca, consola):
        super().__init__(nombre, precio, cantidad, cantidadInicial, prestable, condicion, fecha_lanzamiento, descuento, puntosRequeridos)
        self._marca = marca
        self._consola = consola

    def __str__(self):
        return f"{self._id} | {self._nombre} | Marca: {self._marca}"

    # ~~~~~ Getters y Setters ~~~~~
    def get_marca(self):
        return self._marca
    def set_marca(self, marca):
        self._marca = marca
    def get_consola(self):
        return self._consola
    def set_consola(self, consola):
        self._consola = consola

    def __repr__(self):
        return f"COD: {self.get_id()} |Nombre: {self.get_nombre()} | Precio: {self.get_precio()} | Consola: {self.get_consola()}"
