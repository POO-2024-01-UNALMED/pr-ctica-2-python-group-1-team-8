# Este script solo se corre para volver a serializar todos los objetos de prueba de cero

from gui import VentanaPrincipal
import pickle

from src.baseDatos.serializador import Serializador
from src.gestorAplicacion.informacionVenta.Transaccion import Transaccion
from src.gestorAplicacion.manejoLocal.Fecha import Fecha
from src.gestorAplicacion.manejoLocal.Tienda import Tienda
from src.gestorAplicacion.personas.Cliente import Cliente
from src.gestorAplicacion.personas.Empleado import Empleado
from src.gestorAplicacion.personas.Meta import Meta
from src.gestorAplicacion.productos.Accesorio import Accesorio
from src.gestorAplicacion.productos.Consola import Consola
from src.gestorAplicacion.productos.Juego import Juego

if __name__ == "__main__":
    # Objetos para pruebas

    tienda1 = Tienda("Volador", 123)

    tienda1.agregar_producto(Consola("Polystation 5", 400, 10, 10, False, 5, Fecha(11, 11, 2021), 5, 100, "Sony"))
    tienda1.agregar_producto(Consola("Xbox 1080", 450, 10, 15, False, 5, Fecha(9, 11, 2021), 5, 0, "Microsoft"))
    tienda1.agregar_producto(Consola("Xbox 720", 250, 15, 15, False, 5, Fecha(12, 12, 2013), 5, 100, "Microsoft"))
    tienda1.agregar_producto(Consola("Noentiendo Swap", 300, 20, 20, False, 5, Fecha(13, 7, 2018), 5, 0, "Noentiendo"))
    tienda1.agregar_producto(Consola("Polystation 4", 250, 25, 25, False, 5, Fecha(14, 11, 2013), 15, 200, "Sony"))
    tienda1.agregar_producto(Consola("Xbox 360", 150, 15, 30, False, 5, Fecha(15, 12, 2005), 10, 0, "Microsoft"))
    tienda1.agregar_producto(Consola("Polystation 6", 600, 1, 1, False, 5, Fecha(16, 11, 2028), 0, 0, "Sony"))
    tienda1.agregar_producto(Consola("Arati 7800", 2000, 1, 1, False, 5, Fecha(17, 11, 1986), 0, 0, "Arati"))

    tienda1.agregar_producto(Juego("Carlos Duty", 30, 40, 40, False, 5, Fecha(10, 7, 2018), 5, 0, "FPS", "Xbox 360"))
    tienda1.agregar_producto(Juego("Carlos Duty 2, Ahora es personal", 30, 30, 60, False, 5, Fecha(20, 10, 2024), 0, 0, "FPS", "Xbox 720"))
    tienda1.agregar_producto(Juego("Cyberpunk 2078", 55, 10, 15, False, 5, Fecha(15, 12, 2023), 0, 0, "RPG", "Xbox 1080"))
    tienda1.agregar_producto(Juego("Arch", 45, 8, 10, False, 5, Fecha(20, 11, 2023), 0, 0, "Aventura", "Xbox 1080"))
    tienda1.agregar_producto(Juego("Alive Space", 50, 12, 15, False, 5, Fecha(18, 10, 2023), 0, 0, "Horror", "Xbox 1080"))
    tienda1.agregar_producto(Juego("Full Life", 60, 5, 10, False, 5, Fecha(25, 9, 2023), 0, 0, "FPS", "Xbox 1080"))
    tienda1.agregar_producto(Juego("Meinkraft", 50, 7, 10, False, 5, Fecha(30, 8, 2023), 5, 10, "Sandbox", "Xbox 1080"))
    tienda1.agregar_producto(Juego("Ronaldinho Soccer", 40, 40, 40, False, 5, Fecha(15, 8, 2020), 5, 0, "Deportes", "Polystation 5"))
    tienda1.agregar_producto(Juego("Cyberpunk 2078", 60, 60, 60, False, 5, Fecha(15, 12, 2023), 10, 50, "RPG", "Polystation 5"))
    tienda1.agregar_producto(Juego("Super Mario 256", 60, 50, 50, False, 5, Fecha(10, 10, 2022), 15, 30, "Plataformas", "Noentiendo Swap"))
    tienda1.agregar_producto(Juego("Arch", 65, 55, 70, False, 5, Fecha(20, 11, 2023), 10, 50, "Aventura", "Polystation 5"))
    tienda1.agregar_producto(Juego("Alive Space", 50, 45, 50, False, 5, Fecha(18, 10, 2023), 0, 0, "Horror", "Polystation 5"))
    tienda1.agregar_producto(Juego("Full Life", 30, 40, 40, False, 5, Fecha(25, 9, 2023), 10, 0, "FPS", "Polystation 5"))
    tienda1.agregar_producto(Juego("Meinkraft", 20, 50, 100, False, 5, Fecha(30, 8, 2023), 30, 100, "Sandbox", "Polystation 5"))
    tienda1.agregar_producto(Juego("Super Mario 128", 60, 50, 50, False, 5, Fecha(10, 10, 2021), 5, 20, "Plataformas", "Noentiendo Swap"))
    #serializar = open("../temp/serializado.txt","wb")
    #pickle.dump(clientes,serializar)
    #serializar.close()

    tienda1.agregar_producto(Accesorio("Control Polystation 5", 50, 60, 60, False, 5, Fecha(11, 11, 2021), 0, 0, "Sony", "Polystation 5"))
    tienda1.agregar_producto(Accesorio("Control Polystation 4", 40, 50, 50, False, 5, Fecha(12, 12, 2013), 10, 0, "Sony", "Polystation 4"))
    tienda1.agregar_producto(Accesorio("Control Polystation 3", 30, 40, 40, False, 5, Fecha(13, 11, 2006), 20, 0, "Sony", "Polystation 3"))
    tienda1.agregar_producto(Accesorio("Control Xbox 720", 55, 30, 50, False, 5, Fecha(14, 11, 2021), 0, 0, "Microsoft", "Xbox 720"))
    tienda1.agregar_producto(Accesorio("Control Xbox 360", 45, 20, 40, False, 5, Fecha(15, 12, 2005), 20, 0, "Microsoft", "Xbox 360"))
    tienda1.agregar_producto(Accesorio("Control JoyCon Noentiendo Swap", 70, 40, 40, False, 5, Fecha(13, 7, 2018), 10, 0, "Noentiendo", "Noentiendo Swap"))
    tienda1.agregar_producto(Accesorio("Control Pro Noentiendo Swap", 80, 40, 40, False, 5, Fecha(13, 7, 2018), 10, 0, "Noentiendo", "Noentiendo Swap"))


    # productos de prestamo
    tienda1.agregar_producto(Consola("Polystation 3", 180, 10, 10, True, 4, Fecha(13, 11, 2006), 0, 0, "Sony"))
    tienda1.agregar_producto(Consola("Xbox 360", 200, 10, 10, True, 4, Fecha(15, 12, 2005), 10, 30, "Microsoft"))
    tienda1.agregar_producto(Consola("Polystation 4", 280, 5, 5, True, 4, Fecha(12, 12, 2013), 5, 15, "Sony"))
    tienda1.agregar_producto(Consola("Xbox 720", 350, 3, 3, True, 4, Fecha(12, 12, 2013), 7, 15, "Microsoft"))

    tienda1.agregar_producto(Juego("Ronaldinho Soccer", 40, 10, 10, True, 4, Fecha(15, 8, 2020), 0, 0, "Deportes", "Polystation 5"))
    tienda1.agregar_producto(Juego("Carlos Duty", 30, 10, 20, True, 4, Fecha(10, 7, 2018), 5, 15, "FPS", "Xbox 360"))
    tienda1.agregar_producto(Juego("Carlos Duty 2, Ahora es personal", 30, 10, 15, True, 4, Fecha(20, 10, 2024), 10, 20, "FPS", "Xbox 720"))
    tienda1.agregar_producto(Juego("Super Mario 128", 60, 10, 10, True, 4, Fecha(10, 10, 2021), 15, 40, "Plataformas", "Noentiendo Swap"))

    # productos usados
    tienda1.agregar_producto(Consola("Polystation 2", 50, 5, 5, False, 3, Fecha(11, 10, 2000), 0, 0, "Sony"))
    tienda1.agregar_producto(Consola("Polystation 3", 150, 8, 8, False, 3, Fecha(13, 11, 2006), 0, 0, "Sony"))
    tienda1.agregar_producto(Consola("Polystation 4", 200, 3, 5, False, 3, Fecha(12, 12, 2013), 10, 25, "Sony"))
    tienda1.agregar_producto(Consola("Xbox 360", 130, 5, 5, False, 3, Fecha(15, 12, 2005), 5, 15, "Microsoft"))
    tienda1.agregar_producto(Consola("Noentiendo Wii", 100, 3, 5, False, 3, Fecha(13, 7, 2006), 10, 30, "Noentiendo"))
    tienda1.agregar_producto(Consola("Noentiendo Wii", 80, 2, 2, False, 2, Fecha(13, 7, 2006), 15, 30, "Noentiendo"))
    tienda1.agregar_producto(Consola("Noentiendo DS", 100, 3, 3, False, 3, Fecha(21, 11, 2004), 6, 14, "Noentiendo"))
    tienda1.agregar_producto(Consola("Noentiendo 32", 150, 4, 4, False, 4, Fecha(29, 9, 1996), 0, 0, "Noentiendo"))
    tienda1.agregar_producto(Consola("Noentiendo SEN", 200, 1, 1, False, 3, Fecha(18, 10, 1985), 5, 15, "Noentiendo"))
    tienda1.agregar_producto(Consola("Arati 2600", 800, 1, 1, False, 4, Fecha(11, 9, 1977), 0, 0, "Arati"))
    tienda1.agregar_producto(Consola("Magnavox Odyssey", 900, 1, 1, False, 4, Fecha(27, 8, 1972), 0, 0, "Magnavox"))

    tienda1.agregar_producto(Juego("Ronaldinho Soccer 2010", 10, 10, 10, False, 3, Fecha(15, 6, 2010), 0, 0, "Deportes", "Polystation 3"))
    tienda1.agregar_producto(Juego("Carlos Duty 0.5", 10, 10, 10, False, 3, Fecha(20, 10, 2019), 10, 20, "FPS", "Xbox 360"))
    tienda1.agregar_producto(Juego("Carlos Duty 2, Ahora es personal", 30, 10, 10, False, 3, Fecha(20, 10, 2024), 0, 0, "FPS", "Xbox 720"))
    tienda1.agregar_producto(Juego("Super Mario 128", 50, 7, 7, False, 3, Fecha(10, 10, 2021), 5, 15, "Plataformas", "Noentiendo Swap"))
    tienda1.agregar_producto(Juego("Super Mario 32", 30, 5, 5, False, 2, Fecha(10, 10, 1996), 0, 0, "Plataformas", "Noentiendo 32"))
    tienda1.agregar_producto(Juego("Super Mario 8", 50, 1, 1, False, 3, Fecha(10, 10, 1985), 0, 0, "Plataformas", "Noentiendo SEN"))

    tienda1.agregar_producto(Accesorio("Control Polystation 3", 20, 10, 10, False, 3, Fecha(13, 11, 2006), 0, 0, "Sony", "Polystation 3"))
    tienda1.agregar_producto(Accesorio("Control Xbox 360", 35, 10, 10, False, 3, Fecha(15, 12, 2005), 7, 16, "Microsoft", "Xbox 360"))
    tienda1.agregar_producto(Accesorio("Control Polystation 4", 30, 10, 10, False, 3, Fecha(12, 12, 2013), 0, 0, "Sony", "Polystation 4"))
    tienda1.agregar_producto(Accesorio("Control Arati 2600", 50, 10, 10, False, 3, Fecha(11, 9, 1977), 10, 25, "Arati", "Arati 2600"))
    tienda1.agregar_producto(Accesorio("Control Magnavox Odyssey", 50, 10, 10, False, 3, Fecha(27, 8, 1972), 10, 40, "Magnavox", "Magnavox Odyssey"))


    # ~~~~~~~~~~~~~~~ personal ~~~~~~~~~~~~~~~
    empleado1 =   Empleado(1004, "Emanuel", "ehoyosi@hotmail.com", 3444404, 1000, 10,  5,20, tienda1)
    empleado2 =   Empleado(2004, "Joma", "jomachado@hotmail.com", 3444405, 1500, 12,  5,25, tienda1)

    #metas
    meta1 =  Meta(empleado1, 15, 6, 2024, 30, 8000)
    meta2 =  Meta(empleado1, 22, 6, 2024, 26, 8000)
    meta3 =  Meta(empleado1, 21, 6, 2024, 24, 8000)
    meta4 =  Meta(empleado1, 18, 6, 2024, 35, 10000)
    meta5 =  Meta(empleado1, 19, 6, 2024, 28, 10000)
    meta6 =  Meta(empleado1, 31, 6, 2024, 30, 10000)

    meta1.set_acumulado(29)
    meta2.set_acumulado(29)
    meta3.set_acumulado(29)
    meta4.set_acumulado(29)
    meta5.set_acumulado(29)
    meta6.set_acumulado(29)

    cliente1 = Cliente(1312, "David", "dad", 323)

    fecha1 =   Fecha(15,6,2024)
    fecha2 =   Fecha(11,6,2024)
    fecha3 =   Fecha(14,6,2024)
    fecha4 =   Fecha(13,6,2024)
    fecha5 =   Fecha(10,6,2024)
    fecha6 =   Fecha(12,6,2024)
    fecha7 =   Fecha(11,6,2024)

    fecha8 =   Fecha(8,6,2024)
    fecha9 =   Fecha(7,6,2024)
    fecha10 =   Fecha(8,6,2024)
    fecha11 =   Fecha(5,6,2024)
    fecha12 =   Fecha(7,6,2024)


    # Transaccion(fecha1, cliente1, empleado1, tienda1, [], 10000,10000)
    # Transaccion(fecha2, cliente1, empleado1, tienda1, [], 10000,10000)
    # Transaccion(fecha3, cliente1, empleado1, tienda1, [], 10000,10000)
    # Transaccion(fecha4, cliente1, empleado1, tienda1, [], 10000,10000)
    # Transaccion(fecha5, cliente1, empleado1, tienda1, [], 10000,10000)
    # Transaccion(fecha6, cliente1, empleado1, tienda1, [], 10000,10000)
    # Transaccion(fecha7, cliente1, empleado1, tienda1, [], 10000,10000)
    #
    # Transaccion(fecha8, cliente1, empleado1, tienda1,  [], 10000,10000)
    # Transaccion(fecha9, cliente1, empleado1, tienda1,  [], 10000,10000)
    # Transaccion(fecha10, cliente1, empleado1, tienda1,  [], 10000,10000)
    # Transaccion(fecha11, cliente1, empleado1, tienda1,  [], 10000,10000)
    # Transaccion(fecha12, cliente1, empleado1, tienda1,  [], 10000,10000)


    tienda2 =  Tienda("Robledo", 1420)

    empleado2_1 = Empleado(2008, 'Alejandro', 'alejo@mail.com', 300345, 900, 10, 5, 20, tienda2)
    empleado2_2 = Empleado(20090, 'Samuel', 'samo@mail.com', 300345, 1000, 111, 5, 18, tienda2)


    tienda2.agregar_producto(Consola("Polystation 5", 450, 40, 50, False, 5, Fecha(11, 11, 2021), 0, 0, "Sony"))
    tienda2.agregar_producto(Consola("Polystation 4", 280, 15, 15, False, 5, Fecha(12, 12, 2013), 10, 0, "Sony"))
    tienda2.agregar_producto(Consola("Polystation 3", 180, 20, 20, False, 5, Fecha(13, 11, 2006), 20, 0, "Sony"))
    tienda2.agregar_producto(Consola("Polystation 2", 100, 25, 25, False, 5, Fecha(14, 11, 2000), 20, 0, "Sony"))

    tienda2.agregar_producto(Juego("Ronaldinho Soccer", 40, 40, 50, False, 5, Fecha(15, 8, 2020), 15, 30, "Deportes", "Polystation 5"))
    tienda2.agregar_producto(Juego("Carlos Duty", 30, 40, 40, False, 5, Fecha(10, 7, 2018), 30, 0, "FPS", "Polystation 4"))
    tienda2.agregar_producto(Juego("Full Life", 25, 40, 40, False, 5, Fecha(25, 9, 2010), 15, 10, "FPS", "Polystation 3"))
    tienda2.agregar_producto(Juego("Meinkraft", 20, 40, 40, False, 5, Fecha(30, 8, 2013), 15, 10, "Sandbox", "Polystation 4"))

    tienda2.agregar_producto(Accesorio("Control Polystation 5", 50, 70, 70, False, 5, Fecha(11, 11, 2021), 5, 50, "Sony", "Polystation 5"))
    tienda2.agregar_producto(Accesorio("Control Polystation 4", 40, 60, 60, False, 5, Fecha(12, 12, 2013), 15, 100, "Sony", "Polystation 4"))
    tienda2.agregar_producto(Accesorio("Control Polystation 3", 30, 50, 50, False, 5, Fecha(13, 11, 2006), 40, 300, "Sony", "Polystation 3"))
    tienda2.agregar_producto(Accesorio("Control Polystation 2", 20, 40, 40, False, 5, Fecha(14, 11, 2000), 50, 500, "Sony", "Polystation 2"))

    # productos prestamo
    tienda2.agregar_producto(Consola("Polystation 3", 180, 8, 12, True, 4, Fecha(13, 11, 2006), 0, 0, "Sony"))
    tienda2.agregar_producto(Consola("Xbox 360", 200, 10, 10, True, 4, Fecha(15, 12, 2005), 0, 0, "Microsoft"))
    tienda2.agregar_producto(Consola("Polystation 4", 280, 5, 8, True, 4, Fecha(12, 12, 2013), 10, 15, "Sony"))
    tienda2.agregar_producto(Consola("Xbox 720", 350, 3, 3, True, 4, Fecha(12, 12, 2013), 10, 40, "Microsoft"))

    tienda2.agregar_producto(Juego("Ronaldinho Soccer", 40, 10, 10, True, 4, Fecha(15, 8, 2020), 0, 0, "Deportes", "Polystation 5"))
    tienda2.agregar_producto(Juego("Carlos Duty", 30, 10, 10, True, 4, Fecha(10, 7, 2018), 10, 15, "FPS", "Polystation 4"))
    tienda2.agregar_producto(Juego("Carlos Duty 2, Ahora es personal", 30, 10, 10, True, 4, Fecha(20, 10, 2024), 20, 25, "FPS", "Polystation 5"))

    tienda2.agregar_producto(Accesorio("Control Polystation 5", 50, 10, 10, True, 4, Fecha(13, 11, 2006), 5, 15, "Sony", "Polystation 5"))
    tienda2.agregar_producto(Accesorio("Control Polystation 4", 35, 10, 10, True, 3, Fecha(13, 11, 2006), 0, 0, "Sony", "Polystation 4"))
    tienda2.agregar_producto(Accesorio("Control Polystation 3", 20, 10, 10, True, 4, Fecha(13, 11, 2006), 0, 0, "Sony", "Polystation 3"))

    # productos usados
    tienda2.agregar_producto(Consola("Polystation 2", 50, 5, 5, False, 3, Fecha(11, 10, 2000), 0, 0, "Sony"))
    tienda2.agregar_producto(Consola("Polystation 3", 150, 8, 8, False, 3, Fecha(13, 11, 2006), 0, 0, "Sony"))
    tienda2.agregar_producto(Consola("Polystation 4", 200, 3, 5, False, 3, Fecha(12, 12, 2013), 10, 25, "Sony"))
    tienda2.agregar_producto(Consola("Xbox 360", 130, 5, 5, False, 3, Fecha(15, 12, 2005), 5, 15, "Microsoft"))
    tienda2.agregar_producto(Consola("Noentiendo Wii", 100, 3, 5, False, 3, Fecha(13, 7, 2006), 10, 30, "Noentiendo"))
    tienda2.agregar_producto(Consola("Noentiendo Wii", 80, 2, 2, False, 2, Fecha(13, 7, 2006), 15, 30, "Noentiendo"))
    tienda2.agregar_producto(Consola("Noentiendo DS", 100, 3, 3, False, 3, Fecha(21, 11, 2004), 6, 14, "Noentiendo"))
    tienda2.agregar_producto(Consola("Noentiendo 32", 150, 4, 4, False, 4, Fecha(29, 9, 1996), 0, 0, "Noentiendo"))
    tienda2.agregar_producto(Consola("Noentiendo SEN", 200, 1, 1, False, 3, Fecha(18, 10, 1985), 5, 15, "Noentiendo"))





    tienda3 =   Tienda("Laureles", 1421)
    tienda4 =   Tienda("Buenos Aires", 1422)


    tienda3.agregar_producto(Consola("Polystation 5", 400, 10, 10, False, 5, Fecha(11, 11, 2021), 5, 100, "Sony"))
    tienda3.agregar_producto(Consola("Xbox 1080", 450, 10, 15, False, 5, Fecha(9, 11, 2021), 5, 0, "Microsoft"))
    tienda3.agregar_producto(Consola("Noentiendo Swap", 300, 20, 20, False, 5, Fecha(13, 7, 2018), 5, 0, "Noentiendo"))
    tienda3.agregar_producto(Consola("Polystation 4", 250, 25, 25, False, 5, Fecha(14, 11, 2013), 15, 200, "Sony"))
    tienda3.agregar_producto(Consola("Xbox 360", 150, 15, 30, False, 5, Fecha(15, 12, 2005), 10, 0, "Microsoft"))
    tienda3.agregar_producto(Juego("Cyberpunk 2078", 55, 10, 15, False, 5, Fecha(15, 12, 2023), 0, 0, "RPG", "Xbox 1080"))
    tienda3.agregar_producto(Juego("Arch", 45, 8, 14, False, 5, Fecha(20, 11, 2023), 0, 0, "Aventura", "Xbox 1080"))
    tienda3.agregar_producto(Juego("Alive Space", 50, 12, 25, False, 5, Fecha(18, 10, 2023), 0, 0, "Horror", "Xbox 1080"))
    tienda3.agregar_producto(Juego("Full Life", 60, 5, 20, False, 5, Fecha(25, 9, 2023), 0, 0, "FPS", "Xbox 1080"))
    tienda3.agregar_producto(Juego("Meinkraft", 50, 7, 30, False, 5, Fecha(30, 8, 2023), 0, 0, "Sandbox", "Xbox 1080"))
    tienda3.agregar_producto(Accesorio("Control Polystation 5", 50, 60, 60, False, 5, Fecha(11, 11, 2021), 0, 0, "Sony", "Polystation 5"))
    tienda3.agregar_producto(Accesorio("Control Xbox 720", 55, 30, 50, False, 5, Fecha(14, 11, 2021), 0, 0, "Microsoft", "Xbox 720"))

    empleado3_1 =   Empleado(3001, "Jhorman", "jhorman@example.com", 3444406, 1200, 8,  6,10, tienda3)
    empleado3_2 =   Empleado(3002, "Sebastian", "sebastian@example.com", 3444407, 1300, 9,  6,12, tienda3)

    empleado4_1 =   Empleado(4001, "Pablo", "pablo@example.com", 3444408, 1400, 10,  6,12, tienda4)
    empleado4_2 =   Empleado(4002, "Miguel", "miguel@example.com", 3444409, 1500, 11,  6,10, tienda4)

    tienda4.agregar_producto(Consola("Polystation 5", 450, 10, 10, False, 5, Fecha(11, 11, 2021), 0, 0, "Sony"))
    tienda4.agregar_producto(Consola("Polystation 4", 280, 15, 15, False, 5, Fecha(12, 12, 2013), 10, 0, "Sony"))
    tienda4.agregar_producto(Consola("Polystation 3", 180, 20, 20, False, 5, Fecha(13, 11, 2006), 20, 0, "Sony"))
    tienda4.agregar_producto(Juego("Ronaldinho Soccer", 40, 40, 40, False, 5, Fecha(15, 8, 2020), 15, 0, "Deportes", "Polystation 5"))
    tienda4.agregar_producto(Juego("Carlos Duty", 30, 40, 40, False, 5, Fecha(10, 7, 2018), 30, 0, "FPS", "Polystation 4"))
    tienda4.agregar_producto(Juego("Cyberpunk 2078", 55, 10, 15, False, 5, Fecha(15, 12, 2023), 0, 0, "RPG", "Xbox 1080"))
    tienda4.agregar_producto(Juego("Arch", 45, 8, 10, False, 5, Fecha(20, 11, 2023), 0, 0, "Aventura", "Xbox 1080"))
    tienda4.agregar_producto(Juego("Alive Space", 50, 12, 15, False, 5, Fecha(18, 10, 2023), 0, 0, "Horror", "Xbox 1080"))
    tienda4.agregar_producto(Juego("Full Life", 60, 5, 10, False, 5, Fecha(25, 9, 2023), 0, 0, "FPS", "Xbox 1080"))
    tienda4.agregar_producto(Juego("Meinkraft", 50, 7, 10, False, 5, Fecha(30, 8, 2023), 0, 0, "Sandbox", "Xbox 1080"))
    tienda4.agregar_producto(Accesorio("Control Polystation 5", 50, 60, 60, False, 5, Fecha(11, 11, 2021), 0, 0, "Sony", "Polystation 5"))
    tienda4.agregar_producto(Accesorio("Control Xbox 720", 55, 30, 50, False, 5, Fecha(14, 11, 2021), 0, 0, "Microsoft", "Xbox 720"))
    tienda4.agregar_producto(Accesorio("Control Polystation 4", 40, 50, 50, False, 5, Fecha(12, 12, 2013), 10, 0, "Sony", "Polystation 4"))
    tienda4.agregar_producto(Accesorio("Control Polystation 3", 30, 40, 40, False, 5, Fecha(13, 11, 2006), 20, 0, "Sony", "Polystation 3"))

    # Objetos para el inventario usado
    tienda4.agregar_producto(Consola("Polystation 2", 50, 5, 5, False, 3, Fecha(11, 10, 2000), 0, 0, "Sony"))
    tienda4.agregar_producto(Consola("Polystation 3", 150, 8, 8, False, 3, Fecha(13, 11, 2006), 0, 0, "Sony"))
    tienda4.agregar_producto(Consola("Polystation 4", 200, 3, 5, False, 3, Fecha(12, 12, 2013), 10, 25, "Sony"))
    tienda4.agregar_producto(Consola("Xbox 360", 130, 5, 5, False, 3, Fecha(15, 12, 2005), 5, 15, "Microsoft"))
    tienda4.agregar_producto(Consola("Noentiendo Wii", 100, 3, 5, False, 3, Fecha(13, 7, 2006), 10, 30, "Noentiendo"))
    tienda4.agregar_producto(Consola("Noentiendo Wii", 80, 2, 2, False, 2, Fecha(13, 7, 2006), 15, 30, "Noentiendo"))
    tienda4.agregar_producto(Consola("Noentiendo DS", 100, 3, 3, False, 3, Fecha(21, 11, 2004), 6, 14, "Noentiendo"))
    tienda4.agregar_producto(Juego("Ronaldinho Soccer 2010", 10, 10, 10, False, 3, Fecha(15, 6, 2010), 0, 0, "Deportes", "Polystation 3"))
    tienda4.agregar_producto(Juego("Carlos Duty 0.5", 10, 10, 10, False, 3, Fecha(20, 10, 2019), 10, 20, "FPS", "Xbox 360"))
    tienda4.agregar_producto(Juego("Carlos Duty 2, Ahora es personal", 30, 10, 10, False, 3, Fecha(20, 10, 2024), 0, 0, "FPS", "Xbox 720"))
    tienda4.agregar_producto(Juego("Super Mario 128", 50, 7, 7, False, 3, Fecha(10, 10, 2021), 5, 15, "Plataformas", "Noentiendo Swap"))
    tienda4.agregar_producto(Accesorio("Control Polystation 3", 20, 10, 10, False, 3, Fecha(13, 11, 2006), 0, 0, "Sony", "Polystation 3"))
    tienda4.agregar_producto(Accesorio("Control Xbox 360", 35, 10, 10, False, 3, Fecha(15, 12, 2005), 7, 16, "Microsoft", "Xbox 360"))
    tienda4.agregar_producto(Accesorio("Control Polystation 4", 30, 10, 10, False, 3, Fecha(12, 12, 2013), 0, 0, "Sony", "Polystation 4"))
    tienda4.agregar_producto(Accesorio("Control Arati 2600", 50, 10, 10, False, 3, Fecha(11, 9, 1977), 10, 25, "Arati", "Arati 2600"))
    tienda4.agregar_producto(Accesorio("Control Magnavox Odyssey", 50, 10, 10, False, 3, Fecha(27, 8, 1972), 10, 40, "Magnavox", "Magnavox Odyssey"))

    # Objetos para el inventario prestamo
    tienda4.agregar_producto(Consola("Polystation 3", 180, 8, 12, True, 4, Fecha(13, 11, 2006), 0, 0, "Sony"))
    tienda4.agregar_producto(Consola("Xbox 360", 200, 10, 10, True, 4, Fecha(15, 12, 2005), 0, 0, "Microsoft"))
    tienda4.agregar_producto(Consola("Polystation 4", 280, 5, 8, True, 4, Fecha(12, 12, 2013), 10, 15, "Sony"))
    tienda4.agregar_producto(Consola("Xbox 720", 350, 3, 3, True, 4, Fecha(12, 12, 2013), 10, 40, "Microsoft"))
    tienda4.agregar_producto(Juego("Ronaldinho Soccer", 40, 10, 10, True, 4, Fecha(15, 8, 2020), 0, 0, "Deportes", "Polystation 5"))
    tienda4.agregar_producto(Juego("Carlos Duty", 30, 10, 10, True, 4, Fecha(10, 7, 2018), 10, 15, "FPS", "Polystation 4"))
    tienda4.agregar_producto(Juego("Carlos Duty 2, Ahora es personal", 30, 10, 10, True, 4, Fecha(20, 10, 2024), 20, 25, "FPS", "Polystation 5"))
    tienda4.agregar_producto(Accesorio("Control Polystation 5", 50, 10, 10, True, 4, Fecha(13, 11, 2006), 5, 15, "Sony", "Polystation 5"))
    tienda4.agregar_producto(Accesorio("Control Polystation 4", 35, 10, 10, True, 3, Fecha(13, 11, 2006), 0, 0, "Sony", "Polystation 4"))
    tienda4.agregar_producto(Accesorio("Control Polystation 3", 20, 10, 10, True, 4, Fecha(13, 11, 2006), 0, 0, "Sony", "Polystation 3"))

    # Clientes

    cliente1 =  Cliente(120, "Juan", "juan@mail.com", 311203, 1000)
    cliente2 =  Cliente(121, "Pedro", "pedro@mail.com", 311204, 300)
    cliente3 =  Cliente(122, "Maria", "maria@mail.com", 311205, 400)
    cliente4 =  Cliente(123, "Ana", "ana@mail.com", 311206, 2100)
    cliente5 =  Cliente(124, "Luis", "luis@mail.com", 311207, 1500)
    cliente6 =  Cliente(125, "Carlos", "carlos@mail.com", 311208, 200)
    cliente7 =  Cliente(126, "Sofia", "sofia@mail.com", 311209, 2000)
    cliente8 =  Cliente(127, "Laura", "laura@mail.com", 311210, 500)
    cliente9 =  Cliente(128, "Miguel", "miguel@mail.com", 311211, 700)
    cliente10 = Cliente(129, "Elena", "elena@mail.com", 311212, 900)
    cliente11 = Cliente(130, "Jorge", "jorge@mail.com", 311213, 0)
    cliente12 = Cliente(131, "Patricia", "patricia@mail.com", 311214, 1200)
    cliente13 = Cliente(132, "Fernando", "fernando@mail.com", 311215, 1400)
    cliente14 = Cliente(133, "Lucia", "lucia@mail.com", 311216, 1600)
    cliente15 = Cliente(134, "Andres", "andres@mail.com", 311217, 1800)
    cliente16 = Cliente(135, "Monica", "monica@mail.com", 311218, 2000)
    cliente17 = Cliente(136, "Ricardo", "ricardo@mail.com", 311219, 2200)

    Serializador.serializar_todo(Tienda.get_locales(), Cliente.clientes, Fecha(1, 1, 2021))

    # deserializarLocales = open("../baseDatos/temp/locales.txt", "rb")
    # locales = pickle.load(deserializarLocales)
    # deserializarClientes = open("../baseDatos/temp/clientes.txt", "rb")
    # cliente = pickle.load(deserializarClientes)

    a = VentanaPrincipal()

    # deserializarLocales.close()
    # deserializarClientes.close()