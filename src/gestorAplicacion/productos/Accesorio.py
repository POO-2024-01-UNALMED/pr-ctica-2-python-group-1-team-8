from src.gestorAplicacion.productos.Producto import Producto

class Accesorio(Producto):
    def __init__(self, nombre, precio, cantidad, cantidadInicial, prestable, condicion, fechaLanzamiento, descuento, puntosRequeridos, marca, consola):
        super().__init__(nombre, precio, cantidad, cantidadInicial, prestable, condicion, fechaLanzamiento, descuento, puntosRequeridos)
        self._marca = marca
        self._consola = consola

    def __str__(self):
        return f"Nombre: {self._nombre} | Precio: {self._precio} | Marca: {self._marca} | Consola: {self._consola}"

    # ~~~~~ Getters y Setters ~~~~~
    def getMarca(self):
        return self._marca
    def setMarca(self, marca):
        self._marca = marca
    def getConsola(self):
        return self._consola
    def setConsola(self, consola):
        self._consola = consola

    def __repr__(self):
        return f"COD: {self.getId()} |Nombre: {self.getNombre()} | Precio: {self.getPrecio()} | Consola: {self.getConsola()}"
