from src.gestorAplicacion.productos.Producto import Producto
from src.gestorAplicacion.productos.Accesorio import Accesorio
from src.gestorAplicacion.productos.Juego import Juego
from src.gestorAplicacion.productos.Consola import Consola
#from src.gestorAplicacion.manejoLocal.Reabastecimiento import Reabastecimiento
from src.gestorAplicacion.manejoLocal.Fecha import Fecha
from src.gestorAplicacion.manejoLocal.Tienda import Tienda
#from src.gestorAplicacion.informacionVenta.Transaccion import Transaccion

#Metodo para revisar el inventario
def revisarInventario(local:Tienda):
    while True:
        # TODO:Separador
        opcion = opcionMultiple("Revisar los productos del local\nModificar la informacion de algun producto\nCalcular la prioridad de los productos\nCrear productos\nSalir")
        match opcion:
            case 1:
                revisarProductos(local)
            case 2:
                modificarProducto(local)
            case 3:
                calcularPrioridad(local)
            case 4:
                crearProducto(local)
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
def revisarProductos(local:Tienda):
    opcion = opcionMultiple("\nRevisar por tipo de producto\nRevisar todos los productos en la tienda\nRegresar")
    match opcion:
        case 1:
            lista = revisarTipoProducto(local)
            if lista is None:
                return
            orden = elegirOrden()
            lista = Producto.ordenar(orden, lista)
            for i in lista:
                print( f"Codigo: {i.getId}| Nombre: {i.getNombre()}\nPrecio: {i.getPrecio()}\nVentas: {i.calcular_ventas()}\nPrioridad: {i.getPrioridad()}")
        case 2:
            revisarTodosProductos(local)
        case 3:
            return

#Metodo para revisar los productos por tipo
def revisarTipoProducto(local:Tienda):
    opcion = opcionMultiple("Accesorio\nConsola\nJuego\nRegresar")
    lista = []
    match opcion:
        case 1:#Revisar por tipo Accesorio
            for i in local.get_inventario():
                if isinstance(i,Accesorio):
                    lista.append(i)
            if len(lista) == 0:
                print("No hay accesorios en el inventario")
                input("Presione enter para continuar")
                return None
        case 2:#Revisar por tipo Consola
            for i in local.get_inventario():
                if isinstance(i,Consola):
                    lista.append(i)
            if len(lista) == 0:
                print("No hay consolas en el inventario")
                input("Presione enter para continuar")
                return None
        case 3:#Revisar por tipo Juego
            for i in local.get_inventario():
                if isinstance(i,Juego):
                    lista.append(i)
            if len(lista) == 0:
                print("No hay juegos en el inventario")
                input("Presione enter para continuar")
                return None
        case 4:
            return None

    return lista
#Metodo para revisar todos los productos en la tienda
def revisarTodosProductos(local:Tienda):
    lista = []
    orden = elegirOrden()
    for i in local.get_inventario():
        lista.append(i)
    lista = Producto.ordenar(orden, lista)
    for i in lista:
        print(f"Nombre: {i.getNombre()}\nPrecio: {i.getPrecio()}\nVentas: {i.calcular_ventas()}\n")

#Metodo para modificar la informacion de un producto
def modificarProducto(local:Tienda):
    # TODO: terminar proceso tedioso
    lista = revisarTipoProducto(local)
    if lista is None:
        return
    while True:
        producto = None
        codigo = input("Ingrese el código del producto(Ingrese 0 para salir)")
        if codigo == 0:
            return
        for i in lista:
            if codigo == i.getId():
                producto = i
        if producto is None:
            print("El código ingresado no existe")
            continue

        if isinstance(producto,Accesorio):
            opcion = opcionMultiple("Nombre\nPrecio\nPrestable\nCondicion\nDescuento\nPuntos Requeridos\nMarca\nConsola\nSalir")
            match opcion:
                case 1:
                    nombre = input("Ingrese el nuevo nombre: ")
                    producto.setNombre(nombre)
                    return
                case 2:
                    while True:
                        precio = input("Ingrese el nuevo precio: ")
                        try:
                            precio = eval(precio)
                            producto.setPrecio(precio)
                            return
                        except ValueError:
                            print("Valor ingresado no valido")
                            continue
                case 3:
                    opcion = opcionMultiple("Si\No")
                    if opcion is None:
                        return
                    if opcion == 1:
                        producto.setPrestable(True)
                        return
                    else:
                        producto.setPrestable(False)
                        return
        elif isinstance(producto,Juego):
            opcion = opcionMultiple("Nombre\nPrecio\nPrestable\nCondicion\nDescuento\nPuntos Requeridos\nGenero\nPlataforma\nSalir")
            match opcion:
                case 1:
                    nombre = input("Ingrese el nuevo nombre: ")
                    producto.setNombre(nombre)
                    return
                case 2:
                    while True:
                        precio = input("Ingrese el nuevo precio: ")
                        try:
                            precio = eval(precio)
                            producto.setPrecio(precio)
                            return
                        except ValueError:
                            print("Valor ingresado no valido")
                            continue
                case 3:
                    opcion = opcionMultiple("Si\No")
                    if opcion is None:
                        return
                    if opcion == 1:
                        producto.setPrestable(True)
                        return
                    else:
                        producto.setPrestable(False)
        elif isinstance(producto,Consola):
            opcion = opcionMultiple("Nombre\nPrecio\nPrestable\nCondicion\nDescuento\nPuntos Requeridos\nMarca\nSalir")
            match opcion:
                case 1:
                    nombre = input("Ingrese el nuevo nombre: ")
                    producto.setNombre(nombre)
                    return
                case 2:
                    while True:
                        precio = input("Ingrese el nuevo precio: ")
                        try:
                            precio = eval(precio)
                            producto.setPrecio(precio)
                            return
                        except ValueError:
                            print("Valor ingresado no valido")
                            continue
                case 3:
                    opcion = opcionMultiple("Si\No")
                    if opcion is None:
                        return
                    if opcion == 1:
                        producto.setPrestable(True)
                        return
                    else:
                        producto.setPrestable(False)
                case 4:
                    pass
                case 5:
                    pass
                case 6:
                    pass
                case 7:
                    pass
                case 8:
                    return


#Metodo para calcular la prioridad de los productos
def calcularPrioridad(local:Tienda):
    for i in local.get_inventario():
        if (i.getCantidadInicial() - i.getCantidad()) > i.getCantidadInicial*0.8:
            i.setPrioridad("Prioridad muy alta")
        elif (i.getCantidadInicial() - i.getCantidad()) > i.getCantidadInicial*0.51:
            i.setPrioridad("Prioridad alta")
        elif (i.getCantidadInicial() - i.getCantidad()) > i.getCantidadInicial*0.21:
            i.setPrioridad("Prioridad media")
        else:
            i.setPrioridad("Prioridad baja")

    analizarMercado(local)
#Metodo para crear un producto
def crearProducto(local:Tienda):
    #TODO: terminar proceso tedioso
    pass
def analizarMercado(local:Tienda):
    opcion = opcionMultiple("Analizar el mercado\nRevisar prioridad de cada producto\nRegresar")
    match opcion:
        case 1:
            analisis(local)
        case 2:
            revisarPrioridad(local)
        case 3:
            return
def revisarPrioridad(local:Tienda):
    print("Desea ver los productos agrupados por tipo")
    SiNo = opcionMultiple("Si\nNo")
    match SiNo:
        case 1:
            lista = revisarTipoProducto(local)
            if lista is None:
                return
            lista = Producto.ordenar("prioridad", lista)
            for i in lista:
                print(f"Codigo: {i.getId()} | Nombre: {i.getNombre()} | Prioridad: {i.getPrioridad()}")
        case 2:
            print("Desea ver los productos agrupados por")
            opcion = opcionMultiple("Prioridad muy alta\nPrioridad alta\nPrioridad media\nPrioridad baja\nTodos\nRegresar")
            match opcion:
                case 1:
                    for i in local.get_inventario():
                        if i.getPrioridad() == "Prioridad muy alta":
                            print(f"Codigo: {i.getId()} | Nombre: {i.getNombre()} | Prioridad: {i.getPrioridad()}")
                case 2:
                    for i in local.get_inventario():
                        if i.getPrioridad() == "Prioridad alta":
                            print(f"Codigo: {i.getId()} | Nombre: {i.getNombre()} | Prioridad: {i.getPrioridad()}")
                case 3:
                    for i in local.get_inventario():
                        if i.getPrioridad() == "Prioridad media":
                            print(f"Codigo: {i.getId()} | Nombre: {i.getNombre()} | Prioridad: {i.getPrioridad()}")
                case 4:
                    for i in local.get_inventario():
                        if i.getPrioridad() == "Prioridad baja":
                            print(f"Codigo: {i.getId()} | Nombre: {i.getNombre()} | Prioridad: {i.getPrioridad()}")
                case 5:
                    lista = Producto.ordenar("prioridad", local.get_inventario())
                    for i in lista:
                        print(f"Codigo: {i.getId()} | Nombre: {i.getNombre()} | Prioridad: {i.getPrioridad()}")

                case 6:
                    return
def analisis(local:Tienda):
    while True:
        rangoVentas = []
        print("Ingrese la fecha inicial:\n")
        fechaInicial = pedirFecha()
        print("Ingrese la fecha final:\n")
        fechaFinal = pedirFecha()
        if fechaInicial.get_total_dias() > fechaFinal.get_total_dias():
            print("La fecha inicial no puede ser mayor que la fecha final")
            return
        for i in local.get_caja():
            if fechaInicial.get_total_dias() <= i.getFecha().get_total_dias() <= fechaFinal.get_total_dias():
                rangoVentas.append(i)
        if len(rangoVentas) == 0:
            print("No hay ventas en ese rango de fechas")
            return
        opcion = opcionMultiple("Ver ventas individuales\nOrdenes en este rango \nTendencias en este rango\nProceder al reabastecimiento\nRegresar")
        match opcion:
            case 1:
                # TODO:  hacer las opciones
                pass
            case 2:
                pass
            case 3:
                rebastecimiento(local)
            case 4:
                return

def rebastecimiento(local:Tienda):
    opcion = opcionMultiple("Rebastecer manualmente\nEn base a la prioridad\nSalir")
    match opcion:
        case 1:
            reabastecerManualmente(local)
        case 2:
            reabastecerPrioridad()
        case 3:
            return
def elegirOrden():
    opcion = opcionMultiple("Ordenar por nombre\nOrdenar por precio\nOrdenar por ventas\nRegresar")
    match opcion:
        case 1:
            return "nombre"
        case 2:
            return "precio"
        case 3:
            return "ventas"
        case 4:
            return
def pedirFecha():
    while True:
        # TODO: Agregar restricciones de fecha
        try:
            ano = input("Ingrese el año: ")
            mes = input("Ingrese el mes: ")
            dia = input("Ingrese el dia: ")
        except ValueError:
            print("Fecha no valida")
            continue
        return Fecha(ano,mes,dia)

def reabastecerManualmente(local:Tienda):
    opcion = opcionMultiple("Genero\nPlataforma\nRango de precio\nRegresar")
    match opcion:
        case 1:
            local.agregar_orden(reabastecerManualAux(local,))
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
def reabastecerPrioridad():
    pass
# TODO: terminar metodo
def reabastecerManualAux(local:Tienda,p:list[Juego],fechaActual:Fecha):
    while True:
        plataformas = []
        for i in p:
            if len(plataformas) == 0:
                plataformas.append(i.getPlataforma())
            elif i.getPlataforma() not in plataformas:
                plataformas.append(i.getPlataforma())
        for palabra in plataformas:
            print(f"•{palabra}")
        plataforma = input("Ingrese la plataforma: ")
        if plataforma.capitalize() not in plataformas:
            print("Plataforma no existe")
            continue

        while True:
            for i in p:
                if i.getPlataforma() == plataforma:
                    print(f" COD: {i.getId}| Nombre: {i.getNombre()} | Plataforma: {i.getPlataforma()}")
            opcion = input("Ingrese el codigo del producto que desea reabastecer(Ingrese 0 para salir)")
            if opcion == 0:
                return
            producto = None
            for i in p:
                if i.getId() == opcion:
                    producto = i
                    break
            if producto is None:
                print("El producto ingresado no existe")
                continue
            Nohay = False
            for t in Tienda.get_locales():
                for i in t.get_inventario() and t!=local:
                    if i.getNombre == producto.getNombre() and t!=local:
                        cant = i.getCantidad() - i.getCantidadInicial()*0.4
                        if cant < 0:
                            cant = 0
                        print(f"•Local {t.get_nombre()} | Cantidad disponible: {cant}")
                    elif Tienda.get_locales().index(t) == len(Tienda.get_locales())-1 and t.get_inventario().index(i) == len(t.get_inventario())-1:
                        print("No hay otros locales con este producto")
                        Nohay = True
            if Nohay:
                continue

            while True:
                nombre = ""
                localOrigen = None
                nombre = input("Ingrese el local del que desea reabastecer: ")
                for t in Tienda.get_locales():
                    if t.get_nombre() == nombre.capitalize():
                        localOrigen = t
                if localOrigen is None:
                    print("Local no existe")
                    continue
                break
            cant = 0
            for i in localOrigen.get_inventario():
                if i.getNombre() == producto.getNombre():
                    cant = i.getCantidad() - i.getCantidadInicial()*0.4
                    if cant < 0:
                        cant = 0
            if cant == 0:
                print("El local no tiene suficiente cantidad de este producto")
                continue
            while True:
                print(f"•{producto.getNombre()} | Cantidad disponible para el reabastecimiento: {cant}")
                try:
                    cantidad = input("Ingrese la cantidad a reabastecer: ")
                    cantidad = eval(cantidad)
                    if cantidad > producto.getCantidadInicial()*0.4:
                        print("La cantidad ingresada es mayor a la cantidad disponible"+f"\nCantidad disponible: {int(producto.getCantidadInicial()*0.4)}")
                        input("Presione enter para continuar")
                        continue
                except ValueError:
                    print("Valor no valido")
                    continue
    return