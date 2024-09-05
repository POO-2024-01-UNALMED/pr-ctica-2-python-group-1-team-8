class Transaccion:
    ultimo_id = 1

    def __init__(self, fecha, cliente, empleado, local, productos, valor_sin_descuento, valor_final):
        self.___id = Transaccion.ultimo_id
        Transaccion.ultimo_id += 1
        self.___fecha = fecha
        self.___cliente = cliente
        self.___empleado = empleado
        self.___local = local
        self.___productos = productos
        self.___valor_sin_descuento = valor_sin_descuento
        self.___valor_final = valor_final

    #Metodos
    def agregar_a_local(self):
        self.___local.agregar_transaccion(self)

    def hallar_valor_sin_descuento(self, productos):
        valor = 0
        for producto in productos:
            valor += producto.get_precio()
        return valor

    #Getters y setters
    def get_id(self):
        return self.___id
    def get_fecha(self):
        return self.___fecha
    def get_cliente(self):
        return self.___cliente
    def get_empleado(self):
        return self.___empleado
    def get_local(self):
        return self.___local
    def get_productos(self):
        return self.___productos
    def get_valor_sin_descuento(self):
        return self.___valor_sin_descuento
    def get_valor_final(self):
        return self.___valor_final

    def set_id(self, id):
        self.___id = id
    def set_fecha(self, fecha):
        self.___fecha = fecha
    def set_cliente(self, cliente):
        self.___cliente = cliente
    def set_empleado(self, empleado):
        self.___empleado = empleado
    def set_local(self, local):
        self.___local = local
    def set_productos(self, productos):
        self.___productos = productos
    def set_valor_sin_descuento(self, valor_sin_descuento):
        self.___valor_sin_descuento = valor_sin_descuento
    def set_valor_final(self, valor_final):
        self.___valor_final = valor_final