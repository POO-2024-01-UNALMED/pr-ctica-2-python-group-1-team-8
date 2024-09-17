from multimethod import multimethod

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
        Tienda.agregar_tienda(self)



    # Metodos
    # Agregar producto al inventario correspondiente
    def agregar_producto(self, producto):
        if producto.is_prestable():
            producto.set_precio(producto.get_precio() * 0.01)
            self._inventarioPrestamo.append(producto)
        elif producto.get_condicion() < 5:
            self._inventarioUsado.append(producto)
        else:
            self._inventario.append(producto)
    @classmethod
    def agregar_tienda(cls, tienda):
        if isinstance(tienda, Tienda):
            cls._locales.append(tienda)

    # Reduce en uno la cantidad de un producto en un inventario dado segun codigo
    @staticmethod
    def retirar_uno_de_inventario(producto, inventario):
        for p in inventario:
            if p.getCodigo() == producto.getCodigo():
                p.set_cantidad(p.get_cantidad() - 1)

    # Establece la prioridad de los productos en el inventario
    def actualizar_prioridad(self):
        for i in self._inventario:
            if i.getPrioridad() is None:
                if i.get_cantidad_inicial() - i.get_cantidad() > i.get_cantidad_inicial() * 0.8:
                    i.setPrioridad("Prioridad muy alta")
                elif i.get_cantidad_inicial() - i.get_cantidad() >= i.get_cantidad_inicial() * 0.51:
                    i.setPrioridad("Prioridad alta")
                elif i.get_cantidad_inicial() - i.get_cantidad() >= i.get_cantidad_inicial() * 0.21:
                    i.setPrioridad("Prioridad media")
                else:
                    i.setPrioridad("Prioridad baja")

    def agregar_empleado(self, empleado):
        self._empleados.append(empleado)

    def agregar_transaccion(self, transaccion):
        self._caja.append(transaccion)
        self.agregar_fondos(transaccion.getValorFinal())

    def agregar_fondos(self, fondos):
        self._fondos += fondos

    def agregar_subasta(self, subasta):
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

    # Metodo para obtener los productos de una categoria en el inventario de la tienda
    @multimethod
    def get_productos_categoria_inventario(self, categoria:str):
        invent = self._inventario

        if categoria == "Consola":
            from src.gestorAplicacion.productos.Consola import Consola
            return [p for p in invent if isinstance(p, Consola)]
        elif categoria == "Juego":
            return [p for p in invent if isinstance(p, Juego)]
        elif categoria == "Accesorio":
            from src.gestorAplicacion.productos.Accesorio import Accesorio
            return [p for p in invent if isinstance(p, Accesorio)]

    # Metodo para obtener los productos de una categoria en un inventario especifico
    @multimethod
    def get_productos_categoria_inventario(self, categoria:str, tipo_inventario:str):
        invent = []
        match tipo_inventario:
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

    # Metodo para buscar un producto por su id en un inventario especifico
    @multimethod
    def buscar_producto_id(self, id:int, tipo_inventario:str):
        if tipo_inventario == "prestamo":
            for p in self._inventarioPrestamo:
                if p._id == id:
                    return p
        elif tipo_inventario == "usado":
            for p in self._inventarioUsado:
                if p._id == id:
                    return p
        return None

    # Metodo para buscar un producto por su id en el inventario de la tienda
    @multimethod
    def buscar_producto_id(self, id:int):
        for p in self._inventario:
            if p._id == id:
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