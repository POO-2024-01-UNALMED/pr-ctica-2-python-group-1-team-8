class Subasta:
    ultimo_id = 1

    def __init__(self, fecha_inicio, fecha_fin, productos, oferta_mayor, local, tipo):
        self.___id = Subasta.ultimo_id
        Subasta.ultimo_id += 1
        self.___fecha_inicio = fecha_inicio
        self.___fecha_fin = fecha_fin
        self.___productos = productos
        self.___ofertas = []
        self.___ofertantes = []
        self.___oferta_mayor = oferta_mayor
        self.___estado = "Activa"
        self.___local = local
        self.___tipo = tipo

    #TODO: Implementar metodos

    #Getters y setters
    def get_id(self):
        return self.___id
    def get_fecha_inicio(self):
        return self.___fecha_inicio
    def get_fecha_fin(self):
        return self.___fecha_fin
    def get_productos(self):
        return self.___productos
    def get_ofertas(self):
        return self.___ofertas
    def get_ofertantes(self):
        return self.___ofertantes
    def get_oferta_mayor(self):
        return self.___oferta_mayor
    def get_estado(self):
        return self.___estado
    def get_local(self):
        return self.___local
    def get_tipo(self):
        return self.___tipo

    def set_id(self, id):
        self.___id = id
    def set_fecha_inicio(self, fecha_inicio):
        self.___fecha_inicio = fecha_inicio
    def set_fecha_fin(self, fecha_fin):
        self.___fecha_fin = fecha_fin
    def set_productos(self, productos):
        self.___productos = productos
    def set_ofertas(self, ofertas):
        self.___ofertas = ofertas
    def set_ofertantes(self, ofertantes):
        self.___ofertantes = ofertantes
    def set_oferta_mayor(self, oferta_mayor):
        self.___oferta_mayor = oferta_mayor
    def set_estado(self, estado):
        self.___estado = estado
    def set_local(self, local):
        self.___local = local
    def set_tipo(self, tipo):
        self.___tipo = tipo