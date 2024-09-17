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



        except Exception:
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
        except Exception:
            deserializarClientes = open("../baseDatos/temp/clientes.txt", "rb")
            Cliente.clientes = pickle.load(deserializarClientes)
