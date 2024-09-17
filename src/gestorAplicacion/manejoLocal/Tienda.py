from src.gestorAplicacion.informacionVenta.Transaccion import Transaccion
from src.gestorAplicacion.productos.Juego import Juego
from src.gestorAplicacion.personas.Empleado import Empleado

class Tienda:
    # Constructor
    _locales = []

    def __init__(self, nombre, fondos=0):
        self._nombre = nombre
        self._fondos = fondos
        self._caja:list[Transaccion] = []
        self._subastas = []
        self._inventario = []
        self._inventarioPrestamo = []
        self._inventarioUsado = []
        self._reabastecimientos = []
        self._empleados = []
        Tienda.agregarTienda(self)



    # Metodos
    # Agregar producto al inventario correspondiente
    def agregarProducto(self, producto):
        if producto.isPrestable():
            producto.setPrecio(producto.getPrecio() * 0.01)
            self._inventarioPrestamo.append(producto)
        elif producto.getCondicion() < 5:
            self._inventarioUsado.append(producto)
        else:
            self._inventario.append(producto)
    @classmethod
    def agregarTienda(cls, tienda):
        if isinstance(tienda, Tienda):
            cls._locales.append(tienda)

    # Reduce en uno la cantidad de un producto en un inventario dado segun codigo
    @staticmethod
    def retirarUnoDeInventario(producto, inventario):
        for p in inventario:
            if p.getCodigo() == producto.getCodigo():
                p.setCantidad(p.getCantidad() - 1)

    # Establece la prioridad de los productos en el inventario
    def actualizarPrioridad(self):
        for i in self._inventario:
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
        self._empleados.append(empleado)

    def agregarTransaccion(self, transaccion):
        self._caja.append(transaccion)
        self.agregarFondos(transaccion.getValorFinal())

    def agregarFondos(self, fondos):
        self._fondos += fondos

    def agregarSubasta(self, subasta):
        self._subastas.append(subasta)

    def reabastecer_producto(self, producto_recibido):
        for producto_local in self._inventario:
            if producto_local._nombre.lower() == producto_recibido._nombre.lower():
                # Para juegos, comparar también por consola
                if isinstance(producto_local, Juego) and isinstance(producto_recibido, Juego):
                    juego_local = producto_local
                    juego_recibido = producto_recibido

                    # Si ambos tienen la misma plataforma, aumentar la cantidad del producto local
                    if juego_local._plataforma.lower() == juego_recibido._plataforma.lower():
                        producto_local._cantidad += producto_recibido._cantidad
                    else:  # si no, agregar el producto recibido al inventario
                        self._inventario.append(producto_recibido)

                    return
                else:  # Para otro tipo de productos solo valerse de la comparación por nombre
                    producto_local.cantidad += producto_recibido.cantidad  # Aumentar la cantidad del producto local
                    return

        # En caso de que el producto no se encuentre, agregarlo al inventario
        self._inventario.append(producto_recibido)

    def retirar_producto(self, producto, cantidad):
        for p in self._inventario:
            if p == producto:
                p.cantidad -= cantidad
                p.cantidad_inicial -= cantidad

    def agregar_orden(self, orden):
        if orden is not None:
            self._reabastecimientos.append(orden)

    def get_productos_categoria_inventario(self, categoria, tipo_inventario=None):
        invent = []
        match tipo_inventario:
            case None:
                invent = self._inventario
            case "prestamo":
                invent = self._inventarioPrestamo
            case "usado":
                invent = self._inventarioUsado

        if categoria == "Consola":
            from src.gestorAplicacion.productos.Consola import Consola
            return [p for p in invent if isinstance(p, Consola)]
        elif categoria == "Juego":
            return [p for p in invent if isinstance(p, Juego)]
        elif categoria == "Accesorio":
            from src.gestorAplicacion.productos.Accesorio import Accesorio
            return [p for p in invent if isinstance(p, Accesorio)]

    def buscar_producto_id(self, id, tipo_inventario=None):
        if tipo_inventario is None:
            for p in self._inventario:
                if p.id == id:
                    return p
        elif tipo_inventario == "prestamo":
            for p in self._inventarioPrestamo:
                if p.id == id:
                    return p
        elif tipo_inventario == "usado":
            for p in self._inventarioUsado:
                if p.id == id:
                    return p
        return None

# Getters y setters
    def get_nombre(self):
            return self._nombre

    def set_nombre(self, nombre):
            self._nombre = nombre

    def get_fondos(self):
            return self._fondos

    def set_fondos(self, fondos):
            self._fondos = fondos

    def get_caja(self):
            return self._caja

    def set_caja(self, caja):
            self._caja = caja

    def get_inventario(self):
            return self._inventario

    def set_inventario(self, inventario):
            self._inventario = inventario

    def get_inventario_prestamo(self):
            return self._inventarioPrestamo

    def set_inventario_prestamo(self, inventarioPrestamo):
            self._inventarioPrestamo = inventarioPrestamo

    def get_inventario_usado(self):
            return self._inventarioUsado

    def set_inventario_usado(self, inventarioUsado):
            self._inventarioUsado = inventarioUsado

    def get_reabastecimientos(self):
            return self._reabastecimientos

    def set_reabastecimientos(self, reabastecimientos):
            self._reabastecimientos = reabastecimientos

    @classmethod
    def get_locales(cls):
            return Tienda._locales

    def set_locales(locales):
            Tienda._locales = locales

    def get_empleados(self):
            return self._empleados

    def set_empleados(self, empleados):
            self._empleados = empleados

    def get_subastas(self):
            return self._subastas

    def set_subastas(self, subastas):
            self._subastas = subastas