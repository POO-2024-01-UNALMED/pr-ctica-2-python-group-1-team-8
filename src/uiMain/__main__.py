from gui import VentanaPrincipal
import pickle

if __name__ == "__main__":
    # Objetos para pruebas



    #serializar = open("../temp/serializado.txt","wb")
    #pickle.dump(clientes,serializar)
    #serializar.close()

    deserializar = open("../temp/serializado.txt", "rb")
    archivo = pickle.load(deserializar)

    a = VentanaPrincipal()
    deserializar.close()
