# mixin para clases que necesiten identificar cada instancia de forma unica
class Identificable:
    def __init__(self):
        if not hasattr(self.__class__, 'ultimo_id'): # si no tiene el ultimo_id definido
            self.__class__.ultimo_id = 1
        self.id = self.__class__.ultimo_id
        self.__class__.ultimo_id += 1

# mixin para clases que puedan registrar una fecha en la que fueron creadas
class MarcaTiempo:
    def __init__(self):
        from src.gestorAplicacion.manejoLocal.Fecha import Fecha
        self.creado_en = Fecha.ultima_fecha_acceso # se registra la fecha cuando se crea la instancia
