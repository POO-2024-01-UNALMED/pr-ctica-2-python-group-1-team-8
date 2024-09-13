import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import ttk

from PIL import Image, ImageTk
from colores import *  # Importar colores

from src.gestorAplicacion.manejoLocal.Fecha import Fecha
from src.gestorAplicacion.manejoLocal.Tienda import Tienda
from src.gestorAplicacion.productos.Accesorio import Accesorio
from src.gestorAplicacion.productos.Consola import Consola
from src.gestorAplicacion.productos.Juego import Juego

# Objetos de prueba

tienda1 = Tienda("Volador", 123)

tienda1.agregarProducto(Consola("Polystation 5", 400, 10, 10, False, 5, Fecha(11, 11, 2021), 5, 100, "Sony"))
tienda1.agregarProducto(Consola("Xbox 1080", 450, 10, 15, False, 5, Fecha(9, 11, 2021), 5, 0, "Microsoft"))
tienda1.agregarProducto(Consola("Xbox 720", 250, 15, 15, False, 5, Fecha(12, 12, 2013), 5, 100, "Microsoft"))
tienda1.agregarProducto(Consola("Noentiendo Swap", 300, 20, 20, False, 5, Fecha(13, 7, 2018), 5, 0, "Noentiendo"))
tienda1.agregarProducto(Consola("Polystation 4", 250, 25, 25, False, 5, Fecha(14, 11, 2013), 15, 200, "Sony"))
tienda1.agregarProducto(Consola("Xbox 360", 150, 15, 30, False, 5, Fecha(15, 12, 2005), 10, 0, "Microsoft"))
tienda1.agregarProducto(Consola("Polystation 6", 600, 1, 1, False, 5, Fecha(16, 11, 2028), 0, 0, "Sony"))
tienda1.agregarProducto(Consola("Arati 7800", 2000, 1, 1, False, 5, Fecha(17, 11, 1986), 0, 0, "Arati"))

tienda1.agregarProducto(Juego("Carlos Duty", 30, 40, 40, False, 5, Fecha(10, 7, 2018), 5, 0, "FPS", "Xbox 360"))
tienda1.agregarProducto(Juego("Carlos Duty 2, Ahora es personal", 30, 30, 60, False, 5, Fecha(20, 10, 2024), 0, 0, "FPS", "Xbox 720"))
tienda1.agregarProducto(Juego("Cyberpunk 2078", 55, 10, 15, False, 5, Fecha(15, 12, 2023), 0, 0, "RPG", "Xbox 1080"))
tienda1.agregarProducto(Juego("Arch", 45, 8, 10, False, 5, Fecha(20, 11, 2023), 0, 0, "Aventura", "Xbox 1080"))
tienda1.agregarProducto(Juego("Alive Space", 50, 12, 15, False, 5, Fecha(18, 10, 2023), 0, 0, "Horror", "Xbox 1080"))
tienda1.agregarProducto(Juego("Full Life", 60, 5, 10, False, 5, Fecha(25, 9, 2023), 0, 0, "FPS", "Xbox 1080"))
tienda1.agregarProducto(Juego("Meinkraft", 50, 7, 10, False, 5, Fecha(30, 8, 2023), 5, 10, "Sandbox", "Xbox 1080"))
tienda1.agregarProducto(
    Juego("Ronaldinho Soccer", 40, 40, 40, False, 5, Fecha(15, 8, 2020), 5, 0, "Deportes", "Polystation 5"))
tienda1.agregarProducto(
    Juego("Cyberpunk 2078", 60, 60, 60, False, 5, Fecha(15, 12, 2023), 10, 50, "RPG", "Polystation 5"))
tienda1.agregarProducto(
    Juego("Super Mario 256", 60, 50, 50, False, 5, Fecha(10, 10, 2022), 15, 30, "Plataformas", "Noentiendo Swap"))
tienda1.agregarProducto(Juego("Arch", 65, 55, 70, False, 5, Fecha(20, 11, 2023), 10, 50, "Aventura", "Polystation 5"))
tienda1.agregarProducto(
    Juego("Alive Space", 50, 45, 50, False, 5, Fecha(18, 10, 2023), 0, 0, "Horror", "Polystation 5"))
tienda1.agregarProducto(Juego("Full Life", 30, 40, 40, False, 5, Fecha(25, 9, 2023), 10, 0, "FPS", "Polystation 5"))
tienda1.agregarProducto(
    Juego("Meinkraft", 20, 50, 100, False, 5, Fecha(30, 8, 2023), 30, 100, "Sandbox", "Polystation 5"))
tienda1.agregarProducto(
    Juego("Super Mario 128", 60, 50, 50, False, 5, Fecha(10, 10, 2021), 5, 20, "Plataformas", "Noentiendo Swap"))

tienda1.agregarProducto(
    Accesorio("Control Polystation 5", 50, 60, 60, False, 5, Fecha(11, 11, 2021), 0, 0, "Sony", "Polystation 5"))
tienda1.agregarProducto(
    Accesorio("Control Polystation 4", 40, 50, 50, False, 5, Fecha(12, 12, 2013), 10, 0, "Sony", "Polystation 4"))
tienda1.agregarProducto(
    Accesorio("Control Polystation 3", 30, 40, 40, False, 5, Fecha(13, 11, 2006), 20, 0, "Sony", "Polystation 3"))


tienda_actual = tienda1
fecha = Fecha(1, 1, 2021)

class VentanaPrincipal:
    # Atributos de clase
    # estos atributos son con el fin de permitir la funcion de metodos en la clase
    num_imagen_local = 0
    num_imagen_integrante = 0
    saludo = 'Hola, bienvenido a Villajuegos. Aqui podras encontrar los mejores juegos para ti y tus amigos.'
    descripcion = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cr'

    # Imagenes de local
    paths_local = ['imagenes/tienda/tienda1.jpg', 'imagenes/tienda/tienda2.jpg', 'imagenes/tienda/tienda3.jpg', 'imagenes/tienda/tienda4.jpg', 'imagenes/tienda/tienda5.jpg']

    # Imagenes de integrantes
    paths1 = ['imagenes/integrantes/villa/images1.jpg', 'imagenes/integrantes/villa/images2.jpg',
              'imagenes/integrantes/villa/images3.jpg', 'imagenes/integrantes/villa/images4.jpg']
    paths2 = ['imagenes/integrantes/seba/images1.jpg', 'imagenes/integrantes/seba/images2.jpg',
              'imagenes/integrantes/seba/images3.jpg', 'imagenes/integrantes/seba/images4.jpg']
    paths3 = ['imagenes/integrantes/andres/images1.jpg', 'imagenes/integrantes/andres/images2.jpg',
              'imagenes/integrantes/andres/images3.jpg', 'imagenes/integrantes/andres/images4.jpg']

    paths = [paths1, paths2, paths3]

    def __init__(self, ventana_activa=None):
        self.__class__.num_imagen_integrante = 0 # Reiniciar numero de integrante cada que
                                                 # se crea una instancia de la ventana

        # Si ya hay otra ventana abierta, cerrarla
        if type(ventana_activa) == tk.Tk: ventana_activa.destroy()

        self.root = tk.Tk()
        self.root.title("Inicio")

        self.root.geometry("540x540")
        self.root.configure(bg=FONDO)

        # Configuracion de las filas y columnas
        # Columnas
        self.root.columnconfigure((0,1), weight=1, uniform='a')
        # Filas
        self.root.rowconfigure(1, weight=10, uniform='b')

        # FRAME 1
        self.frame = tk.Frame(self.root, bg=FONDO, highlightbackground=DETALLES, highlightthickness=4)
        self.frame.grid(row=1, column=0, sticky='nsew', padx=15, pady=20)
        # Columnas y filas de FRAME 1
        self.frame.columnconfigure(0, weight=1, uniform='aa')
        self.frame.rowconfigure(0, weight=4, uniform='bb')
        self.frame.rowconfigure(1, weight=7, uniform='bb')
        # ~~~~~~~
        # Elementos
        # Saludo
        self.texto_saludo = tk.Text(self.frame, fg='black', bg=FONDO_2, font=('Arial', 15, 'bold'), wrap='word', cursor='hand2', highlightbackground=DETALLES, highlightthickness=2, bd=0)
        self.texto_saludo.insert(tk.END, self.__class__.saludo)
        self.texto_saludo.grid(row=0, column=0, sticky='nsew', padx=8, pady=8)
        self.texto_saludo.config(state=tk.DISABLED)

        # Subframe 1
        self.subframe1 = tk.Frame(self.frame, bg=FONDO)
        self.subframe1.grid(row=1, column=0, sticky='nsew')
        self.subframe1.columnconfigure(0, weight=1, uniform='aaaa')
        self.subframe1.rowconfigure(0, weight=7, uniform='bbbb')
        self.subframe1.rowconfigure(1, weight=1, uniform='bbbb')

        # Imagenes del local

        self.canvas = tk.Canvas(self.subframe1, bg=FONDO, highlightbackground=DETALLES, highlightthickness=2)
        self.canvas.grid(row=0, column=0, sticky='nsew', padx=8, pady=8)

        self.imagen = ImageTk.PhotoImage(Image.open(self.__class__.paths_local[0]))
        self.imagen_id = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.imagen)

        self.canvas.bind("<Leave>", lambda event: self.cambiar_foto_tienda())

        # Boton para siguiente ventana
        self.boton_secundaria = tk.Button(self.subframe1, text='Abrir programa', font=('Arial', 12, 'bold'), bg=RESALTO, fg='black', cursor='hand2', highlightbackground=DETALLES, highlightthickness=2, bd=0,
                                          command=lambda: VentanaSecundaria(self.root))
        self.boton_secundaria.grid(row=1, column=0, sticky='nsew', padx=8, pady=8)
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # FRAME 2
        self.frame2 = tk.Frame(self.root, bg=FONDO, highlightbackground=DETALLES, highlightthickness=4)
        self.frame2.grid(row=1, column=1, sticky='nsew', padx=15, pady=20)
        # Columnas y filas de FRAME 2
        self.frame2.columnconfigure(0, weight=1, uniform='aa')
        self.frame2.rowconfigure(0, weight=4, uniform='bb')
        self.frame2.rowconfigure(1, weight=7, uniform='bb')
        # ~~~~~~
        # Elementos
        # Subframe 2
        self.subframe2 = tk.Frame(self.frame2, bg=FONDO)
        self.subframe2.grid(row=1, column=0, sticky='nsew')
        self.subframe2.columnconfigure((0,1), weight=1, uniform='aaa')
        self.subframe2.rowconfigure((0,1), weight=1, uniform='bbb')

        # Canvas de imagenes
        self.canvas2_1 = tk.Canvas(self.subframe2, bg=FONDO, highlightbackground=DETALLES, highlightthickness=2)
        self.canvas2_1.grid(row=0, column=0, sticky='nsew', padx=8, pady=8)
        self.canvas2_2 = tk.Canvas(self.subframe2, bg=FONDO, highlightbackground=DETALLES, highlightthickness=2)
        self.canvas2_2.grid(row=0, column=1, sticky='nsew', padx=8, pady=8)
        self.canvas2_3 = tk.Canvas(self.subframe2, bg=FONDO, highlightbackground=DETALLES, highlightthickness=2)
        self.canvas2_3.grid(row=1, column=0, sticky='nsew', padx=8, pady=8)
        self.canvas2_4 = tk.Canvas(self.subframe2, bg=FONDO, highlightbackground=DETALLES, highlightthickness=2)
        self.canvas2_4.grid(row=1, column=1, sticky='nsew', padx=8, pady=8)

        # Mostrar integrantes y hoja de vida y cambiar con click en esta
        # Hojas de vida
        self.text = tk.Text(self.frame2, fg='black', bg=FONDO_2, font=('Arial', 9, 'bold'), wrap='word', cursor='hand2', highlightbackground=DETALLES, highlightthickness=2, bd=0)
        self.text.grid(row=0, column=0, sticky='nsew', padx=8, pady=8)
        self.text.bind("<Button-1>", lambda event: self.cambiar_integrante())

        self.cambiar_integrante() # Llamada inicial a la funcion

        # Menubar
        menubar = tk.Menu(self.root)
        iniciomenu = tk.Menu(menubar, tearoff=0)
        iniciomenu.add_command(label="Descripcion", command=lambda: self.alternar_saludo())
        iniciomenu.add_command(label="Salir", command=self.root.destroy)
        menubar.add_cascade(label="Inicio", menu=iniciomenu)

        self.root.config(menu=menubar)

        self.root.bind("<Configure>", self.resizer)
        self.root.mainloop()

    def resizer(self, event):
        # CANVAS 1 (izquierda)
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        self.imagen_og = Image.open(self.__class__.paths_local[self.__class__.num_imagen_local])
        self.imagen_resizeada = self.imagen_og.resize((width, height))
        self.imagen_nueva = ImageTk.PhotoImage(self.imagen_resizeada)

        self.canvas.itemconfig(self.imagen_id, image=self.imagen_nueva)

        # CANVAS DE SUBFRAME2 (derecha, abajo)
        width2 = self.canvas2_1.winfo_width()
        height2 = self.canvas2_1.winfo_height()

        path_actual = self.__class__.paths[self.__class__.num_imagen_integrante - 1]
        self.imagen1_og = Image.open(path_actual[0])
        self.imagen1_resizeada = self.imagen1_og.resize((width2, height2))
        self.imagen1_nueva = ImageTk.PhotoImage(self.imagen1_resizeada)
        self.canvas2_1.itemconfig(self.imagen1_id, image=self.imagen1_nueva)

        self.imagen2_og = Image.open(path_actual[1])
        self.imagen2_resizeada = self.imagen2_og.resize((width2, height2))
        self.imagen2_nueva = ImageTk.PhotoImage(self.imagen2_resizeada)
        self.canvas2_2.itemconfig(self.imagen2_id, image=self.imagen2_nueva)

        self.imagen3_og = Image.open(path_actual[2])
        self.imagen3_resizeada = self.imagen3_og.resize((width2, height2))
        self.imagen3_nueva = ImageTk.PhotoImage(self.imagen3_resizeada)
        self.canvas2_3.itemconfig(self.imagen3_id, image=self.imagen3_nueva)

        self.imagen4_og = Image.open(path_actual[3])
        self.imagen4_resizeada = self.imagen4_og.resize((width2, height2))
        self.imagen4_nueva = ImageTk.PhotoImage(self.imagen4_resizeada)
        self.canvas2_4.itemconfig(self.imagen4_id, image=self.imagen4_nueva)

    def cambiar_integrante(self):
        p = self.__class__.num_imagen_integrante

        # Limpiar canvas
        self.canvas2_1.delete('all')
        self.canvas2_2.delete('all')
        self.canvas2_3.delete('all')
        self.canvas2_4.delete('all')

        # Imagenes de integrantes
        height = self.canvas2_1.winfo_height()
        width = self.canvas2_1.winfo_width()

        self.imagen1 = ImageTk.PhotoImage(Image.open(self.__class__.paths[p][0]).resize((width, height)))
        self.imagen1_id = self.canvas2_1.create_image(0, 0, anchor=tk.NW, image=self.imagen1)

        self.imagen2 = ImageTk.PhotoImage(Image.open(self.__class__.paths[p][1]).resize((width, height)))
        self.imagen2_id = self.canvas2_2.create_image(0, 0, anchor=tk.NW, image=self.imagen2)

        self.imagen3 = ImageTk.PhotoImage(Image.open(self.__class__.paths[p][2]).resize((width, height)))
        self.imagen3_id = self.canvas2_3.create_image(0, 0, anchor=tk.NW, image=self.imagen3)

        self.imagen4 = ImageTk.PhotoImage(Image.open(self.__class__.paths[p][3]).resize((width, height)))
        self.imagen4_id = self.canvas2_4.create_image(0, 0, anchor=tk.NW, image=self.imagen4)

        self.__class__.num_imagen_integrante += 1
        if self.__class__.num_imagen_integrante > 2:
            self.__class__.num_imagen_integrante = 0

        # Hoja de vida TODO: Quitar texto placeholder
        hv_villa = """villavillavillavillavillavillavillavillavillavillavilla"""
        hv_seba = """sebasebasebasebasebasebasebasebasebasebasebasebaseba"""
        hv_andres = """aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"""
        hojas_vida = [hv_villa, hv_seba, hv_andres]

        self.text.config(state=tk.NORMAL)
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, hojas_vida[p])
        self.text.config(state=tk.DISABLED)

    def cambiar_foto_tienda(self):
        self.__class__.num_imagen_local += 1

        if self.__class__.num_imagen_local > 4:
            self.__class__.num_imagen_local = 0

        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        self.canvas.itemconfig(self.imagen_id, image=ImageTk.PhotoImage(Image.open(self.__class__.paths_local[self.__class__.num_imagen_local])))
        self.resizer(None)

    def alternar_saludo(self):
        self.texto_saludo.config(state=tk.NORMAL)
        if self.texto_saludo.get(1.0, tk.END).strip() == self.__class__.saludo:
            self.texto_saludo.delete(1.0, tk.END)
            self.texto_saludo.insert(tk.END, self.__class__.descripcion)
        else:
            self.texto_saludo.delete(1.0, tk.END)
            self.texto_saludo.insert(tk.END, self.__class__.saludo)
        self.texto_saludo.config(state=tk.DISABLED)

    def recibir_fecha_local(self):
        emergente = tk.Toplevel(self.root)
        emergente.geometry("300x200")
        emergente.title('Ingreso de local y fecha')
        emergente.configure(bg=FONDO)
        # columnas y filas
        emergente.columnconfigure((0,1), weight=1, uniform='f')
        emergente.rowconfigure((0,1,2), weight=1, uniform='g')

        # Frame
        frame = tk.Frame(emergente, bg=FONDO, highlightbackground=DETALLES, highlightthickness=2)

        # labels
        tk.Label(frame, text='Local', font=('Arial', 15, 'bold'), bg=FONDO).grid(row=0, column=0, padx=15, pady=15)
        tk.Label(frame, text='Fecha', font=('Arial', 15, 'bold'), bg=FONDO).grid(row=1, column=0, padx=15, pady=15)

        # entries
        # local
        nombres_locales = list(map(lambda local: local.get_nombre(), Tienda.get_locales()))
        valor_defecto = tk.StringVar(value='Elija un local que gestionar')
        ttk.Combobox(frame, values=nombres_locales, textvariable=valor_defecto).grid(row=0, column=1, padx=15, pady=15)

        # fecha

        emergente.mainloop()

    def cambiar_ventana(self):
        self.recibir_fecha_local()
        #TODO hacer que el llamado a la ventana secundaria se haga desde un boton dentro de recibir_fecha_local
        VentanaSecundaria(self.root)

class VentanaSecundaria:
    def __init__(self, ventana_activa=None):
        # Si ya hay otra ventana abierta, cerrarla
        if type(ventana_activa) == tk.Tk: ventana_activa.destroy()

        self.root = tk.Tk()
        self.root.title("Villaware")
        self.root.geometry("700x600")
        self.root.configure(bg=FONDO)

        # Columnas
        self.root.columnconfigure((0), weight=1, uniform='a')
        # Filas
        self.root.rowconfigure(0, weight=1, uniform='b')

        # prueba_fieldframe = FieldFrame(self.root, "Criterios", ["nombre", "precio", "cantidad", "plataforma", "genero", "descripcion", "fecha_lanzamiento", "desarrolladora", "distribuidora"], "Valores")
        # prueba_fieldframe.grid(row=0,column=0,sticky='nswe', padx=40,pady=40)

        prueba_subfieldframe = FieldFrameProducto(self.root)
        prueba_subfieldframe.grid(row=0, column=0, sticky='nswe', padx=40, pady=40)

        # Menubar
        menubar = tk.Menu(self.root)

        archivomenu = tk.Menu(menubar, tearoff=0)
        descripcion_app = 'Villajuegos es un software completo para compañias de tiendas especializadas en el mundo de los videojuegos que permite tanto llevar a cabo ventas, prestamos y subastas como gestionar y analizar el inventario de cada local y sus empleados'
        archivomenu.add_command(label="Aplicacion", command=lambda: messagebox.showinfo('Informacion', descripcion_app))
        archivomenu.add_command(label="Salir", command=lambda: VentanaPrincipal(self.root))
        menubar.add_cascade(label="Archivo", menu=archivomenu)

        procesomenu = tk.Menu(menubar, tearoff=0)
        procesomenu.add_command(label="Registrar compra")
        procesomenu.add_command(label="Hacer prestamo")
        procesomenu.add_command(label="Administrar inventario")
        procesomenu.add_command(label="Gestionar empleados")
        procesomenu.add_command(label="Subastar")
        menubar.add_cascade(label="Procesos y Consultas", menu=procesomenu)

        ayudamenu = tk.Menu(menubar, tearoff=0)
        descripcion_integrantes = ('Programa de la autoria de:'
                                   '\n- David Villa Alzate'
                                   '\n- Sebastian Cepeda Jaimes'
                                   '\n- Andres Santiago Garces Barrero')
        ayudamenu.add_command(label="Acerca de", command=lambda: messagebox.showinfo('Acerca de', descripcion_integrantes))
        menubar.add_cascade(label="Ayuda", menu=ayudamenu)

        self.root.config(menu=menubar)

        self.root.mainloop()

class FieldFrame(tk.Frame):
    def __init__(self, ventana, titulo_criterios, criterios, titulo_valores, valores=None, habilitados=None):
        super().__init__(ventana, bg=FONDO, highlightbackground=DETALLES, highlightthickness=2)

        self.criterios = criterios
        self.valores = criterios if valores is None else valores

        numeros_criterios = []
        for i in range(1, len(criterios) + 1): numeros_criterios.append(i)

        # Configuracion de columnas y filas
        self.columnconfigure((0,1), weight=1, uniform='a') # Columnas para criterio y valor
        self.rowconfigure((0, len(criterios) + 1), weight=1,uniform='b') # Fila para titulo y botones
        self.rowconfigure(tuple(numeros_criterios), weight=1, uniform='b')

        # Titulos
        (tk.Label(self, text=titulo_criterios, font=('Arial', 15, 'bold'), bg=FONDO)  # Criterio
         .grid(row=0, column=0, ipadx=15, padx=35, pady=10, sticky='e'))
        (tk.Label(self, text=titulo_valores, font=('Arial', 15, 'bold'), bg=FONDO)  # Valor
         .grid(row=0, column=1, ipadx=15, padx=35, pady=10, sticky='w'))

        self.dibujar_campos(criterios, valores, habilitados)

        # Botones
        (tk.Button(self, text='Aceptar', bg=RESALTO, bd=0, command=lambda: self.aceptar(self.entries_val, self.criterios))
        .grid(row=len(criterios) + 1, column=0, padx=35, sticky='e'))
        (tk.Button(self, text='Cancelar', bg= POWER, bd=0)
        .grid(row=len(self.valores) + 1, column=1, padx=35, sticky='w'))

    # Metodos
    def getValue(self, criterio):
        indice = self.criterios.index(criterio)
        # Leer el valor del Entry correspondiente
        return self.entries_val[indice].get()

    def dibujar_campos(self, criterios, valores=None, habilitados=None):

        for cri in criterios:
            (tk.Label(self, text=cri, bg=FONDO)
             .grid(row=criterios.index(cri) + 1, column=0, padx=35, sticky='e'))

        self.entries_val = [] # Lista para registrar cada entry
        for val in self.valores:
            entr = tk.Entry(self)

            # Insertar valor inicial en el Entry si corresponde
            if valores is not None:
                if type(val) == str: entr.insert(0, val)

            # Habilitar o deshabilitar los Entry segun la lista habilitados
            if habilitados is not None: entr.config(state='normal' if habilitados[self.valores.index(val)] else 'disabled')
            entr.grid(row=self.valores.index(val) + 1, column=1, ipadx=45, padx=35, sticky='w')
            self.entries_val.append(entr)

    def aceptar(self, entries_val, criterios):
        try:
            # Buscar si hay algun campo vacio
            for entry in entries_val:
                if entry.get() == '':
                    raise ExceptionCampoVacio(entries_val, criterios)

        # TODO agregar retorno y mas manejo de exepciones
        except ExceptionCampoVacio:
            # volver a colorear los campos invalidos una vez que se cierre la ventana emergente
            for entry in entries_val:
                entry.config(bg='white')

class FieldFrameProducto(tk.Frame):
    # TODO destruir este frame y colocar el de pago al presionar Comprar
    carrito = []

    def __init__(self, ventana):
        super().__init__(ventana, bg=FONDO)

        self.framemain = tk.Frame(ventana, bg=FONDO)
        self.framemain.grid(row=0, column=0, sticky='nswe')
        self.framemain.rowconfigure((0,2), weight=1, uniform='a')
        self.framemain.rowconfigure(1, weight=4, uniform='a')
        self.framemain.columnconfigure(0, weight=1, uniform='b')

        self.subframe1 = tk.Frame(self.framemain, bg=FONDO, bd=0)
        self.subframe1.grid(row=0, column=0, sticky='s')
        self.subframe1.rowconfigure((0, 1), weight=1, uniform='aa')
        self.subframe1.columnconfigure((0, 1, 2), weight=1, uniform='bb')

        # Titulos
        tk.Label(self.subframe1, text='Categoria', font=('Arial', 11, 'bold'), bg=FONDO).grid(row=0, column=0, padx=15, sticky='e')
        tk.Label(self.subframe1, text='Producto', font=('Arial', 11, 'bold'), bg=FONDO).grid(row=1, column=0, padx=15, sticky='e')

        # Comboboxes
        categorias = ['Consola', 'Juego', 'Accesorio']

        categoria_default = tk.StringVar(value='Elige una categoria')
        self.combobox_categoria = ttk.Combobox(self.subframe1, values=categorias, textvariable=categoria_default)
        self.combobox_categoria.grid(row=0, column=1, padx=15, pady=15)

        # Crear combobox con listado de productos segun la categoria ingresada
        def identificar_categoria_nombres(cat:str):
            return list(map(lambda producto: producto.getNombre(), tienda_actual.get_productos_categoria(cat)))

        self.listado_productos = []
        self.combobox_producto = ttk.Combobox(self.subframe1)

        def crear_listado(frame):
            listado_default = tk.StringVar(value='Elige un producto')
            listado_nombres = identificar_categoria_nombres(self.combobox_categoria.get())
            self.listado_productos = tienda_actual.get_productos_categoria(self.combobox_categoria.get())

            self.combobox_producto.config(values=listado_nombres, textvariable=listado_default)
            self.combobox_producto.grid(row=1, column=1, padx=15, pady=15)

        # Boton para crear combobox listado
        self.boton_listado = tk.Button(self.subframe1, text='Buscar', font=('Arial', 7, 'bold'), bg=RESALTO, bd=0, command=lambda: crear_listado(self.subframe1))
        self.boton_listado.grid(row=0, column=2, padx=15, pady=15, sticky='w')

        # Insertar producto seleccionado
        self.producto_actual = None
        def identificar_producto():
            self.producto_actual = self.listado_productos[self.combobox_producto.current()]
            # Espacio del FieldFrame
            criterios = ['ID', 'Nombre', 'Precio', 'Cantidad', 'Fecha de lanzamiento']
            valores = [str(self.producto_actual.getId()), self.producto_actual.getNombre(), str(self.producto_actual.getPrecio()), str(self.producto_actual.getCantidad()), str(self.producto_actual.getFechaLanzamiento())]
            cri_habilitados = [False, False, False, False, False]

            self.subframe2 = tk.Frame(self.framemain, bg=FONDO, bd=0)
            self.subframe2.grid(row=1, column=0)
            FieldFrame(self.subframe2, 'Dato', criterios, 'Valor', valores, cri_habilitados).grid(row=0, column=0, padx=15, pady=15)
            # TODO que fieldframe tambien reciba el comando de aceptar para que se pueda hacer la modificacion, o que aceptar devuelva los valores y asi agregarlos al carrito en fieldframeproducto

        # Boton para insertar producto seleccionado
        self.boton_producto = tk.Button(self.subframe1, text='Insertar', font=('Arial', 7, 'bold'), bg=RESALTO, bd=0, command=lambda: identificar_producto())
        self.boton_producto.grid(row=1, column=2, padx=15, pady=15, sticky='w')

        self.total_carrito()

    def total_carrito(self):
        subframe3 = tk.Frame(self.framemain, bg=FONDO, bd=0)
        subframe3.grid(row=2, column=0)
        subframe3.columnconfigure((0,1), weight=1, uniform='a')
        subframe3.rowconfigure((0, 1), weight=1, uniform='b')

        tk.Label(subframe3, text='Total', font=('Arial', 11, 'bold'), bg=FONDO).grid(row=0, column=0, padx=15, pady=15, sticky='e')
        tk.Entry(subframe3, state='disabled').grid(row=0, column=1, padx=15, pady=15, sticky='w')

        tk.Button(subframe3, text='Comprar', font=('Arial', 7, 'bold'), bg=RESALTO, bd=0).grid(row=1, column=0, padx=15, pady=15, sticky='e')
        tk.Button(subframe3, text='Limpiar carrito', font=('Arial', 7, 'bold'), bg=POWER, bd=0).grid(row=1, column=1, padx=15, pady=15, sticky='w')

# Excepciones
class ErrorAplicacion(Exception):
    def __init__(self, mensaje):
        self.mensaje = 'Manejo de errores de la Aplicacion\n' + mensaje
        messagebox.showerror('Error', self.mensaje)

# Grupo 1
class ExceptionLogica(ErrorAplicacion):
    def __init__(self, mensaje):
        super().__init__('Error logico en la aplicacion:\n' + mensaje)

class ExceptionFechaInvalida(ExceptionLogica):
    def __init__(self, fecha):
        super().__init__('Ingrese una fecha posterior a ' + fecha)

class ExceptionCantidadInvalida(ExceptionLogica):
    def __init__(self):
        super().__init__('Este local no posee suficientes unidades de este producto')

class ExceptionNoEncontrado(ExceptionLogica):
    def __init__(self):
        super().__init__('No se encontro ninguna instancia con este dato')

# Grupo 2
class ExceptionCampos(ErrorAplicacion):
    def __init__(self, mensaje):
        super().__init__('Error en los campos:\n' + mensaje)

class ExceptionValorInvalido(ExceptionCampos):
    def identificar_valor_invalido(self, entries_val, criterios):
        self.valores_invalidos = []
        self.mensaje = ''

        #TODO encontrar una forma de hacer que se compruebe que el tipo de dato ingresado sea el esperado para cada fieldframe

class ExceptionCampoVacio(ExceptionCampos):
    def __init__(self, entries_val, criterios):
        super().__init__(self.identificar_campos_vacios(entries_val, criterios))

    def identificar_campos_vacios(self, entries_val, criterios):
        self.campos_vacios = []
        self.mensaje = ''

        for entry in entries_val:
            if entry.get() == '':
                entry.config(bg='red')
                self.campos_vacios.append(criterios[entries_val.index(entry)])

        return('Campos vacios: ' + ', '.join(self.campos_vacios))

if __name__ == '__main__':
    v = VentanaPrincipal()