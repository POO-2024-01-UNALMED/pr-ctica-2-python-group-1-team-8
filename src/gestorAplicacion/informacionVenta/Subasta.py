from src.gestorAplicacion.mixins import Identificable, MarcaTiempo


class Subasta(Identificable, MarcaTiempo):
    def __init__(self, fecha_fin, productos, oferta_mayor, local, tipo):
        super().__init__()
        self._fecha_fin = fecha_fin
        self._productos = productos
        self._ofertas = []
        self._ofertantes = []
        self._oferta_mayor = oferta_mayor
        self._estado = "Activa"
        self._TIPO = tipo
        self._LOCAL = local

        local.agregar_subasta(self)

    # Sumarle 7 dias a la fecha de fin de la subasta y decrementar su oferta inicial
    def extender_subasta(self, fecha_actual):
        from src.gestorAplicacion.manejoLocal.Fecha import Fecha
        self._fecha_fin = Fecha(int(fecha_actual.get_total_dias()) + 7)

        if (self._TIPO == 'Ascendente' or self._TIPO == 'Descendente') and self._oferta_mayor > 0:
            oferta_mayor_anterior = self._oferta_mayor
            oferta_mayor_nueva = int(self._oferta_mayor * 0.8)
            self._oferta_mayor = oferta_mayor_nueva

            return 'Se ha extendido la subasta # ' + str(self.get_id()) + ' por 7 dias y se ha decrementado la oferta mayor de ' + str(oferta_mayor_anterior) + ' a ' + str(oferta_mayor_nueva)
        else:
            return 'Se ha extendido la subasta # ' + str(self.get_id()) + ' por 7 dias'

    # ~~ Agregar subastas ~~
    # Metodo para agregar una oferta a una subasta ascendente
    def agregar_oferta(self, oferta, cliente):
        self._ofertas.append(oferta)
        self._ofertantes.append(cliente)
        self._oferta_mayor = oferta

    # Metodo para agregar oferta a una subasta anonima
    def agregar_oferta_anonima(self, oferta, cliente):
        self._ofertas.append(oferta)
        self._ofertantes.append(cliente)

        # Actualizar oferta mayor
        if (oferta > self._oferta_mayor):
            self._oferta_mayor = oferta

    # Registra oferta ganadora de una subasta descendente
    def registrar_oferta_ganadora(self, cliente):
        self._ofertas.append(self._oferta_mayor)
        self._ofertantes.append(cliente)
        self._estado = "Finalizada"

        # Actualizar puntos del ganador
        cliente.set_puntos(cliente.get_puntos_fidelidad() - self._oferta_mayor)

    # ~~ Finalizar subastas ~~
    # Finalizar subasta ascendente o descendente. Retorna al ganador
    def finalizar_subasta(self):
        self._estado = 'Finalizada'

        # Buscar ofertante ganador
        ganador = self._ofertantes[self._ofertas.index(self._oferta_mayor)]

        # Actualizar puntos de ganador
        ganador.set_puntos_fidelidad(ganador.get_puntos_fidelidad() + self._oferta_mayor)

        return ganador

    # Finalizar subasta anonima. Retorna al ganador, y en caso de empate,
    # el ganador sera el primero en haber ofertado
    def finalizar_subasta_anonima(self):
        self._estado = 'Finalizada'

        # Buscar mayor oferta
        for i in range(len(self._ofertas)):
            if self._ofertas[i] == self._oferta_mayor:
                return self._ofertantes[i]

    # ~~ Calcular valoracion de objetos de subasta ~~
    # Calcular valoracion de subasta ascendente del conjunto de productos que recibe
    @staticmethod
    def calcular_valoracion_ascendente(productos, fecha_actual):
        valor_total = 0

        for pro in productos:
            rareza = 0

            # Valorar por diferencia de tiempo entre el año de lanzamiento y la fecha actual
            years_diferencia = abs(fecha_actual.get_year() - pro.get_fecha_lanzamiento().get_year())
            rareza += years_diferencia // 5

            # Valorar por condicion
            rareza += pro.get_condicion() - 1

            # Añadir el valor de la rareza al valor total
            valor_inicial = int(pro.get_precio() * (pow(1.2, rareza) - 1))

            valor_total += valor_inicial

        return valor_total

    # Calcular valoracion de subasta descendente del conjunto de productos que recibe
    @staticmethod
    def calcular_valoracion_descendente(productos, fecha_actual):
        valor_total = 0

        for pro in productos:
            rareza = 0

            # Valorar por diferencia de tiempo entre el año de lanzamiento y la fecha actual
            years_diferencia = abs(fecha_actual.get_year() - pro.get_fecha_lanzamiento().get_year())
            rareza += years_diferencia // 5

            # Valorar por condicion
            rareza += pro.get_condicion() - 1

            # Añadir el valor de la rareza al valor total
            valor_inicial = int(pro.get_precio() * (pow(1.4, rareza) + 1))

            valor_total += valor_inicial

        return valor_total

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
    def get_LOCAL(self):
        return self._LOCAL
    def get_TIPO(self):
        return self._TIPO

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
    def set_LOCAL(self, local):
        self._LOCAL = local
    def set_TIPO(self, tipo):
        self._TIPO = tipo