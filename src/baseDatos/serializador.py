import pickle

class Serializador:
    @staticmethod
    def serializar_todo(lista_locales, lista_clientes, ultima_fecha):
        # Locales
        try:
            import os
            path_locales = os.path.realpath('src\\baseDatos\\temp\\locales.txt')
            with open(path_locales, 'wb') as file:
                pickle.dump(lista_locales, file)

            path_clientes = os.path.realpath('src\\baseDatos\\temp\\clientes.txt')
            with open(path_clientes, 'wb') as file:
                pickle.dump(lista_clientes, file)

            path_fecha = os.path.realpath('src\\baseDatos\\temp\\fecha.txt')
            with open(path_fecha, 'wb') as file:
                pickle.dump(ultima_fecha, file)

        except Exception: # Esta excepcion manejara la serializacion si no se ejecuta desde el .exe
            serializar = open('../baseDatos/temp/locales.txt', 'wb')
            pickle.dump(lista_locales, serializar)
            serializar.close()

            # Clientes
            serializar1 = open('../baseDatos/temp/clientes.txt', 'wb')
            pickle.dump(lista_clientes, serializar1)
            serializar1.close()

            # Fecha
            serializar2 = open('../baseDatos/temp/fecha.txt', 'wb')
            pickle.dump(ultima_fecha, serializar2)
            serializar2.close()
            print("Serializado con exito")