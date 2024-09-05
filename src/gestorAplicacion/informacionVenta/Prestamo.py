class Prestamo:
    ultimo_id = 0
    def __init__(self, fecha_inicio, fecha_fin, cliente, productos, valor_total, estado):
        self.___id = Prestamo.ultimo_id
        Prestamo.ultimo_id += 1
        self.___fecha_inicio = fecha_inicio
        self.___fecha_fin = fecha_fin
        self.___cliente = cliente
        self.___produtos = productos
        self.___valor_total = valor_total
        self.___estado = estado

        cliente.agregar_prestamo(self)

    #Metodos
    def __str__(self):
        return f"* ID: {self.get_id()} | Fecha de inicio: {self.get_fecha_inicio()} | Fecha de fin: {self.get_fecha_fin()} | Cliente: {self.___cliente.get_nombre()} | Valor total: {self.get_valor_total()} | Estado: {self.get_estado()} | Productos: {self.imprimir_productos()}"

    def imprimir_productos(self):
        productos = ""
        for producto in self.___produtos:
            productos += f"* ID: {producto.get_id()} | Nombre: {producto.get_nombre()}\n"
        return productos

    # Getters y setters
    def get_id(self):
        return self.___id
    def get_fecha_inicio(self):
        return self.___fecha_inicio
    def get_fecha_fin(self):
        return self.___fecha_fin
    def get_cliente(self):
        return self.___cliente
    def get_productos(self):
        return self.___produtos
    def get_valor_total(self):
        return self.___valor_total
    def get_estado(self):
        return self.___estado

    def set_id(self, id):
        self.___id = id
    def set_fecha_inicio(self, fecha_inicio):
        self.___fecha_inicio = fecha_inicio
    def set_fecha_fin(self, fecha_fin):
        self.___fecha_fin = fecha_fin
    def set_cliente(self, cliente):
        self.___cliente = cliente
    def set_productos(self, productos):
        self.___produtos = productos
    def set_valor_total(self, valor_total):
        self.___valor_total = valor_total
    def set_estado(self, estado):
        self.___estado = estado