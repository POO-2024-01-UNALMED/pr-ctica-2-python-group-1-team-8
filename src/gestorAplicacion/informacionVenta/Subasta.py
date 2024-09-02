class Subasta:
    ultimo_id = 1

    def __init__(self, fecha_inicio, fecha_fin, productos, oferta_mayor, local, tipo):
        self._id = Subasta.ultimo_id
        Subasta.ultimo_id += 1
        self._fecha_inicio = fecha_inicio
        self._fecha_fin = fecha_fin
        self._productos = productos
        self._ofertas = []
        self._ofertantes = []
        self._oferta_mayor = oferta_mayor
        self._estado = "Activa"
        self._local = local
        self._tipo = tipo

    #TODO: Implementar metodos

    #Getters y setters
    def get_id(self):
        return self._id
    def get_fecha_inicio(self):
        return self._fecha_inicio
    def get_fecha_fin(self):
        return self._fecha_fin
    def get_productos(self):
        return self._productos
    def get_ofertas(self):
        return self._ofertas
    def get_ofertantes(self):
        return self._ofertantes
    def get_oferta_mayor(self):
        return self._oferta_mayor
    def get_estado(self):
        return self._estado
    def get_local(self):
        return self._local
    def get_tipo(self):
        return self._tipo

    def set_id(self, id):
        self._id = id
    def set_fecha_inicio(self, fecha_inicio):
        self._fecha_inicio = fecha_inicio
    def set_fecha_fin(self, fecha_fin):
        self._fecha_fin = fecha_fin
    def set_productos(self, productos):
        self._productos = productos
    def set_ofertas(self, ofertas):
        self._ofertas = ofertas
    def set_ofertantes(self, ofertantes):
        self._ofertantes = ofertantes
    def set_oferta_mayor(self, oferta_mayor):
        self._oferta_mayor = oferta_mayor
    def set_estado(self, estado):
        self._estado = estado
    def set_local(self, local):
        self._local = local
    def set_tipo(self, tipo):
        self._tipo = tipo