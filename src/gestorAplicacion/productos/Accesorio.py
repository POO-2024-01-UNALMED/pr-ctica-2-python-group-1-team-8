import Producto

class Accesorio(Producto):
    def __init__(self, nombre, precio, cantidad, cantidadInicial, prestable, condicion, fechaLanzamiento, descuento, puntosRequeridos, marca)                      :
        super().__init__(nombre, precio, cantidad, cantidadInicial, prestable, condicion, fechaLanzamiento, descuento, puntosRequeridos)
        self.__marca = marca
        self.__consola = consola

    def __str__(self):
        return f"Nombre: {self.nombre} Precio: {self.precio} Descripcion: {self.descripcion} Marca: {self.marca} Color: {self.color} Talla: {self.talla} Material: {self.material}"

    # ~~~~~ Getters y Setters ~~~~~
    def get_marca(self):
        return self.__marca
    def set_marca(self, marca):
        self.__marca = marca
    def get_consola(self):
        return self.__consola
    def set_consola(self, consola):
        self.__consola = consola
