import pickle

class Serializador:
    @staticmethod
    def serializar_todo(lista_locales, lista_clientes, ultima_fecha):
        # Locales
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
        print("Serializado fecha")