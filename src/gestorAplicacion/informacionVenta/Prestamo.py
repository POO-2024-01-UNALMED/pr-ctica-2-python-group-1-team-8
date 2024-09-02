class Prestamo:
    ultimo_id = 0
    def __init__(self, fecha_inicio, fecha_fin, cliente, productos, valor_total, estado):
        self._id = Prestamo.ultimo_id
        Prestamo.ultimo_id += 1
        self._fecha_inicio = fecha_inicio
        self._fecha_fin = fecha_fin
        self._cliente = cliente
        self._produtos = productos
        self._valor_total = valor_total
        self._estado = estado

        cliente.agregar_prestamo(self)

    #Metodos
    def __str__(self):
        return f"* ID: {self.get_id()} | Fecha de inicio: {self.get_fecha_inicio()} | Fecha de fin: {self.get_fecha_fin()} | Cliente: {self._cliente.get_nombre()} | Valor total: {self.get_valor_total()} | Estado: {self.get_estado()} | Productos: {self.imprimir_productos()}"

    def imprimir_productos(self):
        productos = ""
        for producto in self._produtos:
            productos += f"* ID: {producto.get_id()} | Nombre: {producto.get_nombre()}\n"
        return productos

    # Getters y setters
    def get_id(self):
        return self._id
    def get_fecha_inicio(self):
        return self._fecha_inicio
    def get_fecha_fin(self):
        return self._fecha_fin
    def get_cliente(self):
        return self._cliente
    def get_productos(self):
        return self._produtos
    def get_valor_total(self):
        return self._valor_total
    def get_estado(self):
        return self._estado

    def set_id(self, id):
        self._id = id
    def set_fecha_inicio(self, fecha_inicio):
        self._fecha_inicio = fecha_inicio
    def set_fecha_fin(self, fecha_fin):
        self._fecha_fin = fecha_fin
    def set_cliente(self, cliente):
        self._cliente = cliente
    def set_productos(self, productos):
        self._produtos = productos
    def set_valor_total(self, valor_total):
        self._valor_total = valor_total
    def set_estado(self, estado):
        self._estado = estado