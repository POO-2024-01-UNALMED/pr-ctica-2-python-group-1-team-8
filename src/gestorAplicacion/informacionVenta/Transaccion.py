class Transaccion:
    ultimo_id = 1

    def __init__(self, fecha, cliente, empleado, local, productos, valor_sin_descuento, valor_final):
        self._id = Transaccion.ultimo_id
        Transaccion.ultimo_id += 1
        self._fecha = fecha
        self._cliente = cliente
        self._empleado = empleado
        self._local = local
        self._productos = productos
        self._valor_sin_descuento = valor_sin_descuento
        self._valor_final = valor_final

    #Metodos
    def agregar_a_local(self):
        self._local.agregar_transaccion(self)

    def hallar_valor_sin_descuento(self, productos):
        valor = 0
        for producto in productos:
            valor += producto.get_precio()
        return valor

    #Getters y setters
    def get_id(self):
        return self._id
    def get_fecha(self):
        return self._fecha
    def get_cliente(self):
        return self._cliente
    def get_empleado(self):
        return self._empleado
    def get_local(self):
        return self._local
    def get_productos(self):
        return self._productos
    def get_valor_sin_descuento(self):
        return self._valor_sin_descuento
    def get_valor_final(self):
        return self._valor_final

    def set_id(self, id):
        self._id = id
    def set_fecha(self, fecha):
        self._fecha = fecha
    def set_cliente(self, cliente):
        self._cliente = cliente
    def set_empleado(self, empleado):
        self._empleado = empleado
    def set_local(self, local):
        self._local = local
    def set_productos(self, productos):
        self._productos = productos
    def set_valor_sin_descuento(self, valor_sin_descuento):
        self._valor_sin_descuento = valor_sin_descuento
    def set_valor_final(self, valor_final):
        self._valor_final = valor_final