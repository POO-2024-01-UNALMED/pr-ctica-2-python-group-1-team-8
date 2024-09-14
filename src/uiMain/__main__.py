from gui import VentanaPrincipal
import pickle

if __name__ == "__main__":
    # Objetos para pruebas

    #serializar = open("../temp/locales.txt","wb")
    #pickle.dump(tiendas,serializar)
    #serializar.close()
    #serializar1 = open("../temp/clientes.txt", "wb")
    #pickle.dump(clientes, serializar1)
    #serializar1.close()


    deserializarLocales = open("../temp/locales.txt", "rb")
    locales = pickle.load(deserializarLocales)
    deserializarClientes = open("../temp/clientes.txt", "rb")
    cliente = pickle.load(deserializarClientes)

    a = VentanaPrincipal()

    deserializarLocales.close()
    deserializarClientes.close()