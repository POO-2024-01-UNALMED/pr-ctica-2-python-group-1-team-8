from src.gestorAplicacion.productos.Producto import Producto
from src.gestorAplicacion.productos.Accesorio import Accesorio
from src.gestorAplicacion.productos.Juego import Juego
from src.gestorAplicacion.productos.Consola import Consola
from src.gestorAplicacion.manejoLocal.Reabastecimiento import Reabastecimiento
from src.gestorAplicacion.manejoLocal.Fecha import Fecha
from src.gestorAplicacion.manejoLocal.Tienda import Tienda
from src.gestorAplicacion.informacionVenta.Transaccion import Transaccion

from re import match

#Metodo para revisar el inventario
def revisarInventario():
    while True:
        # TODO:Separador
        opcion = opcionMultiple("Revisar los productos del local\nModificar la informacion de algun producto\nCalcular la prioridad de los productos\nCrear productos\nSalir")
        match opcion:
            case 1:
                revisarProductos(),
            case 2:
                modificarProducto(),
            case 3:
                calcularPrioridad(),
            case 4:
                crearProducto(),
            case 5:
                return





#Metodo para elegir una de multiples opciones
def opcionMultiple(texto:str,):
    frases = texto.split("\n")
    while True:
        print("Seleccione una opcion:")
        for i in range(len(frases)):
            print(f"{i+1}. {frases[i]}\n")
        opcion1 = input("Ingrese su opcion: ")
        if opcion1.isdigit():
            opcion1 = int(opcion1)
            if 0 < opcion1 <= len(frases):
                break
        else:
            print("Ingrese un numero valido\n")
            input("Presione enter para continuar")
            continue
    return int(opcion1)

#Metodo para revisar los productos del local
def revisarProductos():
    opcion = opcionMultiple("\nRevisar por tipo de producto\nRevisar todos los productos en la tienda\nRegresar")
    match opcion:
        case 1:
            revisarTipoProducto(),
        case 2:
            revisarTodosProductos(),
        case 3:
            return

#Metodo para revisar los productos por tipo
def revisarTipoProducto():
    opcion = opcionMultiple("Accesorio\nConsola\nJuego\nRegresar")
    lista = []
    #TODO: Borrar local cuando se pase al main
    local = Tienda("puebla",50000)
    match opcion:
        case 1:#Revisar por tipo Accesorio
            for i in local.get_inventario():
                if isinstance(i,Accesorio):
                    lista.append(i)
        case 2:#Revisar por tipo Consola
            for i in local.get_inventario():
                if isinstance(i,Consola):
                    lista.append(i)
        case 3:#Revisar por tipo Juego
            for i in local.get_inventario():
                if isinstance(i,Juego):
                    lista.append(i)
        case 4:
            return
    for i in lista:
        print(i)
#Metodo para revisar todos los productos en la tienda
def revisarTodosProductos():
    lista = []

#Metodo para modificar la informacion de un producto
def modificarProducto():
    pass

#Metodo para calcular la prioridad de los productos
def calcularPrioridad():
    pass

#Metodo para crear un producto
def crearProducto():
    pass


