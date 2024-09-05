from src.gestorAplicacion.productos import Juego

class Tienda:
    # Constructor
    def __init__(self, nombre, fondos=0):
        self.__nombre = nombre
        self.__fondos = fondos
        self.__caja = []
        self.__subastas = []
        self.__inventario = []
        self.__inventarioPrestamo = []
        self.__inventarioUsado = []
        self.__reabastecimientos = []
        self.__empleados = []
        Tienda.locales.append(self)

    locales = []

    # Metodos
    # Agregar producto al inventario correspondiente
    def agregarProducto(self, producto):
        if producto.isPrestable():
            self.__inventarioPrestamo.append(producto)
        elif producto.getCondicion() < 5:
            self.__inventarioUsado.append(producto)
        else:
            self.__inventario.append(producto)

    # Reduce en uno la cantidad de un producto en un inventario dado segun codigo
    @staticmethod
    def retirarUnoDeInventario(producto, inventario):
        for p in inventario:
            if p.getCodigo() == producto.getCodigo():
                p.setCantidad(p.getCantidad() - 1)

    # Establece la prioridad de los productos en el inventario
    def actualizarPrioridad(self):
        for i in self.__inventario:
            if i.getPrioridad() is None:
                if i.getCantidadInicial() - i.getCantidad() > i.getCantidadInicial() * 0.8:
                    i.setPrioridad("Prioridad muy alta")
                elif i.getCantidadInicial() - i.getCantidad() >= i.getCantidadInicial() * 0.51:
                    i.setPrioridad("Prioridad alta")
                elif i.getCantidadInicial() - i.getCantidad() >= i.getCantidadInicial() * 0.21:
                    i.setPrioridad("Prioridad media")
                else:
                    i.setPrioridad("Prioridad baja")

    def agregarEmpleado(self, empleado):
        self.__empleados.append(empleado)

    def agregarTransaccion(self, transaccion):
        self.__caja.append(transaccion)
        self.agregarFondos(transaccion.getValorFinal())

    def agregarFondos(self, fondos):
        self.__fondos += fondos

    def agregarSubasta(self, subasta):
        self.__subastas.append(subasta)

    def reabastecer_producto(self, producto_recibido):
        for producto_local in self.__inventario:
            if producto_local._nombre.lower() == producto_recibido._nombre.lower():
                # Para juegos, comparar también por consola
                if isinstance(producto_local, Juego) and isinstance(producto_recibido, Juego):
                    juego_local = producto_local
                    juego_recibido = producto_recibido

                    # Si ambos tienen la misma plataforma, aumentar la cantidad del producto local
                    if juego_local.plataforma.lower() == juego_recibido.plataforma.lower():
                        producto_local.cantidad += producto_recibido.cantidad
                    else:  # si no, agregar el producto recibido al inventario
                        self.__inventario.append(producto_recibido)

                    return
                else:  # Para otro tipo de productos solo valerse de la comparación por nombre
                    producto_local.cantidad += producto_recibido.cantidad  # Aumentar la cantidad del producto local
                    return

        # En caso de que el producto no se encuentre, agregarlo al inventario
        self.__inventario.append(producto_recibido)

    def retirar_producto(self, producto, cantidad):
        for p in self.__inventario:
            if p == producto:
                p.cantidad -= cantidad
                p.cantidad_inicial -= cantidad

    def agregar_orden(self, orden):
        if orden is not None:
            self.__reabastecimientos.append(orden)

# Getters y setters
    def get_nombre(self):
            return self.__nombre

    def set_nombre(self, nombre):
            self.__nombre = nombre

    def get_fondos(self):
            return self.__fondos

    def set_fondos(self, fondos):
            self.__fondos = fondos

    def get_caja(self):
            return self.__caja

    def set_caja(self, caja):
            self.__caja = caja

    def get_inventario(self):
            return self.__inventario

    def set_inventario(self, inventario):
            self.__inventario = inventario

    def get_inventario_prestamo(self):
            return self.__inventarioPrestamo

    def set_inventario_prestamo(self, inventarioPrestamo):
            self.__inventarioPrestamo = inventarioPrestamo

    def get_inventario_usado(self):
            return self.__inventarioUsado

    def set_inventario_usado(self, inventarioUsado):
            self.__inventarioUsado = inventarioUsado

    def get_reabastecimientos(self):
            return self.__reabastecimientos

    def set_reabastecimientos(self, reabastecimientos):
            self.__reabastecimientos = reabastecimientos

    def get_locales():
            return Tienda.locales

    def set_locales(locales):
            Tienda.locales = locales

    def get_empleados(self):
            return self.__empleados

    def set_empleados(self, empleados):
            self.__empleados = empleados

    def get_subastas(self):
            return self.__subastas

    def set_subastas(self, subastas):
            self.__subastas = subastas