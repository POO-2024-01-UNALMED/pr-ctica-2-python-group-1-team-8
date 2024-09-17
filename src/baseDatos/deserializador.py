import pickle

class Deserializador:
    @staticmethod
    def deserializar_locales():
        from src.gestorAplicacion.manejoLocal.Tienda import Tienda
        try:
            import os
            path_locales = os.path.realpath('src\\baseDatos\\temp\\locales.txt')
            with open(path_locales, 'rb') as file:
                Tienda.set_locales(pickle.load(file))

        except Exception: # Esta excepcion manejara la deserializacion si no se ejecuta desde el .exe
            deserializarLocales = open("../baseDatos/temp/locales.txt", "rb")
            Tienda.set_locales(pickle.load(deserializarLocales))

    @staticmethod
    def deserializar_clientes():
        from src.gestorAplicacion.personas.Cliente import Cliente
        try:
            import os
            path_clientes = os.path.realpath('src\\baseDatos\\temp\\clientes.txt')
            with open(path_clientes, 'rb') as file:
                Cliente.clientes = pickle.load(file)
        except Exception: # Esta excepcion manejara la deserializacion si no se ejecuta desde el .exe
            deserializarClientes = open("../baseDatos/temp/clientes.txt", "rb")
            Cliente.clientes = pickle.load(deserializarClientes)

    @staticmethod
    def deserializar_fecha():
        from src.gestorAplicacion.manejoLocal.Fecha import Fecha
        try:
            import os
            path_fecha = os.path.realpath('src\\baseDatos\\temp\\fecha.txt')
            with open(path_fecha, 'rb') as file:
                Fecha.ultima_fecha_acceso = pickle.load(file)
        except Exception: # Esta excepcion manejara la deserializacion si no se ejecuta desde el .exe
            deserializarFecha = open("../baseDatos/temp/fecha.txt", "rb")
            Fecha.ultima_fecha_acceso = pickle.load(deserializarFecha)
