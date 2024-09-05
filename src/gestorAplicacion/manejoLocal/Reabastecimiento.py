class Reabastecimiento:
    # Constructor
    def __init__(self, local_origen, local_destino, fecha_entrega, productos_recibidos):
        self._local_origen = local_origen
        self._local_destino = local_destino
        self._fecha_entrega = fecha_entrega
        self._productos_recibidos = productos_recibidos

    # Metodos

    # Metodo que aplica reabastecimiento a todos los productos del inventario
    # de este (el reabastecimiento) al inventario de la tienda destino
    def aplicar_reabastecimiento(self):
        for producto in self._productos_recibidos:
            self._local_destino.reabastecer_producto(producto)

    # Getters y setters
    def get_local_origen(self):
        return self._local_origen

    def set_local_origen(self, local_origen):
        self._local_origen = local_origen

    def get_local_destino(self):
        return self._local_destino

    def set_local_destino(self, local_destino):
        self._local_destino = local_destino

    def get_fecha_entrega(self):
        return self._fecha_entrega

    def set_fecha_entrega(self, fecha_entrega):
        self._fecha_entrega = fecha_entrega

    def get_productos_recibidos(self):
        return self._productos_recibidos

    def set_productos_recibidos(self, productos_recibidos):
        self._productos_recibidos = productos_recibidos