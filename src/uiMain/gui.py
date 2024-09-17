# En esta clase ocurre toda la creacion de ventanas y escenas necesarias para llevar a cabo las funcionalidades del programa

import copy
import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import ttk, Frame

from PIL import Image, ImageTk
from src.uiMain.colores import *  # Importar colores

from src.gestorAplicacion.manejoLocal.Fecha import Fecha
from src.gestorAplicacion.manejoLocal.Tienda import Tienda
from src.gestorAplicacion.personas.Cliente import Cliente
from src.gestorAplicacion.productos.Producto import Producto

import os

from src.uiMain.funcionalidad4 import gestionarMeta, verRendimiento, ampliarMeta, compararRendimiento

from src.baseDatos.deserializador import Deserializador
Deserializador.deserializar_locales()
Deserializador.deserializar_clientes()
Deserializador.deserializar_fecha()

locales = Tienda.get_locales()

class VentanaPrincipal:
    # Atributos de clase

    ultima_fecha = Fecha.ultima_fecha_acceso

    # estos atributos son con el fin de permitir la funcion de metodos en la clase
    num_imagen_local = 0
    num_imagen_integrante = 0
    saludo = 'Hola, bienvenido a Villajuegos. Aqui podras encontrar los mejores juegos para ti y tus amigos.'
    descripcion = 'Villajuegos es un programa que permite gestionar transacciones tales como compras, prestamos y subastas asi como gestionar su inventario y empleados y sin dejar de lado la posibilidad de analizar su rendimiento'

    # Obtener la carpeta actual
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Path absoluto para la carpeta de imagenes
    imagenes_dir = os.path.join(current_dir, 'imagenes')

    # Imagenes de local
    paths_local = [
        os.path.join(imagenes_dir, 'tienda', 'tienda1.jpg'),
        os.path.join(imagenes_dir, 'tienda', 'tienda2.jpg'),
        os.path.join(imagenes_dir, 'tienda', 'tienda3.jpg'),
        os.path.join(imagenes_dir, 'tienda', 'tienda4.jpg'),
        os.path.join(imagenes_dir, 'tienda', 'tienda5.jpg')
    ]

    # Imagenes de integrantes
    paths1 = [
        os.path.join(imagenes_dir, 'integrantes', 'villa', 'images1.jpg'),
        os.path.join(imagenes_dir, 'integrantes', 'villa', 'images2.jpg'),
        os.path.join(imagenes_dir, 'integrantes', 'villa', 'images3.jpg'),
        os.path.join(imagenes_dir, 'integrantes', 'villa', 'images4.jpg')
    ]

    paths2 = [
        os.path.join(imagenes_dir, 'integrantes', 'seba', 'images1.jpg'),
        os.path.join(imagenes_dir, 'integrantes', 'seba', 'images2.jpg'),
        os.path.join(imagenes_dir, 'integrantes', 'seba', 'images3.jpg'),
        os.path.join(imagenes_dir, 'integrantes', 'seba', 'images4.jpg')
    ]

    paths3 = [
        os.path.join(imagenes_dir, 'integrantes', 'andres', 'images1.jpg'),
        os.path.join(imagenes_dir, 'integrantes', 'andres', 'images2.jpg'),
        os.path.join(imagenes_dir, 'integrantes', 'andres', 'images3.jpg'),
        os.path.join(imagenes_dir, 'integrantes', 'andres', 'images4.jpg')
    ]

    paths = [paths1, paths2, paths3]

    def __init__(self, ventana_activa=None):
        self.__class__.num_imagen_integrante = 0 # Reiniciar numero de integrante cada que
                                                 # se crea una instancia de la ventana

        # Si ya hay otra ventana abierta, cerrarla
        if type(ventana_activa) == tk.Tk: ventana_activa.destroy()

        self.root = tk.Tk()
        self.root.title("Inicio")

        self.root.geometry("640x640")
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
                                          command=lambda: self.recibir_fecha_local())
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
        iniciomenu.add_command(label="Salir", command=self.salir_y_serializar)
        menubar.add_cascade(label="Inicio", menu=iniciomenu)

        self.root.config(menu=menubar)

        self.root.bind("<Configure>", self.resizer)
        self.root.mainloop()

    def salir_y_serializar(self):
        # Serializar locales y clientes
        from src.baseDatos.serializador import Serializador
        Serializador.serializar_todo(Tienda.get_locales(), Cliente.clientes, self.__class__.ultima_fecha)

        self.root.destroy()


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

        hv_villa = """David Villa Alzate. 19 años. Estudiante de Ingenieria de Sistemas e informatica. Solo bacaneria. """
        hv_seba = """Sebastian Cepeda Jaimes, 18 años. Estudiante de Ingenieria de Sistemas e informatica. Platinado el Forager y Celeste. Le gustan los animales y no sabe programar interfaces. """
        hv_andres = """Santiago Garces. 19 años. Estudiante de Ingenieria de Sistemas e informatica. Tiene conocimientos basicos en programacion orientada a objetos con Java, Python y Rust. Tiene tantos loros como errores en sus programas (muchos)."""
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
        emergente.rowconfigure((0,1,2,3), weight=1, uniform='g')

        # labels
        tk.Label(emergente, text='Local', font=('Arial', 10, 'bold'), bg=FONDO).grid(row=0, column=0, padx=3, pady=2)
        tk.Label(emergente, text='Fecha', font=('Arial', 10, 'bold'), bg=FONDO).grid(row=1, column=0, padx=3, pady=2)

        tk.Label(emergente, text='Ultima fecha de ingreso: ' + str(self.__class__.ultima_fecha), font=('Arial', 10, 'bold'), bg=FONDO).grid(row=2, column=0, columnspan=2, padx=3, pady=2)

        # entries
        # local
        nombres_locales = list(map(lambda local: local.get_nombre(), locales))
        lista_locales = locales

        valor_defecto = tk.StringVar(value='Elija un local que gestionar')
        self.combobox = ttk.Combobox(emergente, values=nombres_locales, textvariable=valor_defecto)
        self.combobox.grid(row=0, column=1, padx=3, pady=2)

        # fecha
        self.entry_fecha = tk.Entry(emergente)
        self.entry_fecha.grid(row=1, column=1, padx=3, pady=2)

        def aceptar():
            try:
                # Convertir la fecha ingresada a un objeto Fecha
                fecha_ingreso = self.entry_fecha.get().split('/')

                    # Buscar correcto formateo de fecha
                if len(fecha_ingreso) != 3:
                    raise ExceptionFormatoFecha()

                fecha_ingreso = Fecha(int(fecha_ingreso[0]), int(fecha_ingreso[1]), int(fecha_ingreso[2]))

                # Buscar si hay algun campo vacio
                if self.combobox.get() == '' or self.entry_fecha.get() == '':
                    raise ExceptionCampoVacio([self.combobox, self.entry_fecha], ['Local', 'Fecha'])

                # Comprobar que la fecha sea posterior o igual a la ultima registrada

                if fecha_ingreso.get_total_dias() < self.__class__.ultima_fecha.get_total_dias():
                    raise ExceptionFechaInvalida(self.__class__.ultima_fecha)

                local_actual = lista_locales[nombres_locales.index(self.combobox.get())]

            except ExceptionCampoVacio:
                pass
            except ExceptionFechaInvalida:
                pass
            except ExceptionFormatoFecha:
                pass
            else:
                # Actualizar fecha y local actuales
                self.__class__.ultima_fecha = fecha_ingreso

                # Destruir esta ventana y llamar la siguiente
                VentanaSecundaria(self.root, local_actual, fecha_ingreso)

        # botones
        tk.Button(emergente, text='Aceptar', background=RESALTO, bd=0, command=aceptar).grid(row=3, column=0, padx=3, pady=2)
        tk.Button(emergente, text='Cancelar', background=POWER, bd=0).grid(row=3, column=1, padx=3, pady=2)

        emergente.mainloop()

class VentanaSecundaria:
    def __init__(self, ventana_activa, local, fecha):
        # Si ya hay otra ventana abierta, cerrarla
        if type(ventana_activa) == tk.Tk: ventana_activa.destroy()

        self.root = tk.Tk()
        self.root.title("Villajuegos")
        self.root.geometry("900x700")
        self.root.configure(bg=FONDO)

        # Columnas
        self.root.columnconfigure(0, weight=1, uniform='a')
        # Filas
        self.root.rowconfigure(0, weight=1, uniform='b')

        self.master_frame = tk.Frame(self.root, bg=FONDO)
        self.master_frame.grid(row=0, column=0, sticky='nswe')
        self.master_frame.columnconfigure(0, weight=1, uniform='a')
        self.master_frame.rowconfigure(0, weight=2, uniform='b')
        self.master_frame.rowconfigure(1, weight=11, uniform='b')

        def llamar_compra():
            self.limpiar_frame(self.master_frame)

            titulo_func = 'Registrar compra'
            descripcion_func = 'Esta funcionalidad permite registrar una compra en el local seleccionado de un conjunto de productos almacenados en un carrito.'

            subframe_descripcion = tk.Frame(self.master_frame, bg=FONDO)
            subframe_descripcion.grid(row=0, column=0, sticky='nswe', padx=20, ipady=20)
            subframe_descripcion.rowconfigure(0, weight=1, uniform='a')
            subframe_descripcion.rowconfigure(1, weight = 2, uniform='a')
            subframe_descripcion.columnconfigure(0, weight=1, uniform='a')

            tk.Label(subframe_descripcion, text=titulo_func, font=('Arial', 12, 'bold'), bg=FONDO).grid(row=0, column=0, padx=5, pady=5)
            descrp_func_widget = tk.Text(subframe_descripcion, bg=FONDO_2, font=('Arial', 9), wrap='word', bd=0)
            descrp_func_widget.insert(tk.END, descripcion_func)
            descrp_func_widget.grid(row=1, column=0, padx=5, pady=5)

            subframe_func = tk.Frame(self.master_frame, bg=FONDO, highlightbackground=DETALLES)
            subframe_func.grid(row=1, column=0, sticky='nswe')
            subframe_func.columnconfigure(0, weight=1, uniform='a')
            subframe_func.rowconfigure(0, weight=1, uniform='b')
            prueba_subfieldframe = FieldFrameProducto(subframe_func, local)
            prueba_subfieldframe.grid(row=1, column=0, sticky='nswe', padx=40, pady=40)

        def llamar_prestamo():
            self.limpiar_frame(self.master_frame)

            titulo_func = 'Registrar prestamo'
            descripcion_func = 'Desde aqui puedes gestionar todo lo relacionado a prestamos, desde su creacion hasta su devolucion y cobro de multas'

            subframe_descripcion = tk.Frame(self.master_frame, bg=FONDO)
            subframe_descripcion.grid(row=0, column=0, sticky='nswe', padx=20, ipady=20)
            subframe_descripcion.rowconfigure(0, weight=1, uniform='a')
            subframe_descripcion.rowconfigure(1, weight = 2, uniform='a')
            subframe_descripcion.columnconfigure(0, weight=1, uniform='a')

            tk.Label(subframe_descripcion, text=titulo_func, font=('Arial', 12, 'bold'), bg=FONDO).grid(row=0, column=0, padx=5, pady=5)
            descrp_func_widget = tk.Text(subframe_descripcion, bg=FONDO_2, font=('Arial', 9), wrap='word', bd=0)
            descrp_func_widget.insert(tk.END, descripcion_func)
            descrp_func_widget.grid(row=1, column=0, padx=5, pady=5)

            subframe_func = tk.Frame(self.master_frame, bg=FONDO, highlightbackground=DETALLES)
            subframe_func.grid(row=1, column=0, sticky='nswe')
            subframe_func.columnconfigure(0, weight=1, uniform='a')
            subframe_func.rowconfigure(0, weight=1, uniform='b')

            prueba_subfieldframe = FieldFramePrestamo(subframe_func, local, fecha)
            prueba_subfieldframe.grid(row=0, column=0, sticky='nswe', padx=40, pady=40)

        def llamar_administrar():
            self.limpiar_frame(self.master_frame)

            titulo_func = 'Administrar inventario '
            descripcion_func = 'Esta funcionalidad da la posibilidad de revisar el inventario de la tienda elegida, analizar sus estadisticas de venta o bien ordenar reabastecimientos entre locales.'

            subframe_descripcion = tk.Frame(self.master_frame, bg=FONDO)
            subframe_descripcion.grid(row=0, column=0, sticky='nswe', padx=20, ipady=20)
            subframe_descripcion.rowconfigure(0, weight=1, uniform='a')
            subframe_descripcion.rowconfigure(1, weight = 2, uniform='a')
            subframe_descripcion.columnconfigure(0, weight=1, uniform='a')

            tk.Label(subframe_descripcion, text=titulo_func, font=('Arial', 12, 'bold'), bg=FONDO).grid(row=0, column=0, padx=5, pady=5)
            descrp_func_widget = tk.Text(subframe_descripcion, bg=FONDO_2, font=('Arial', 9), wrap='word', bd=0)
            descrp_func_widget.insert(tk.END, descripcion_func)
            descrp_func_widget.grid(row=1, column=0, padx=5, pady=5)

            subframe_func = tk.Frame(self.master_frame, bg=FONDO, highlightbackground=DETALLES)
            subframe_func.grid(row=1, column=0, sticky='nswe')
            subframe_func.columnconfigure(0, weight=1, uniform='a')
            subframe_func.rowconfigure(0, weight=1, uniform='b')

            prueba_subfieldframe = FieldFrameAdministrar(subframe_func, local)
            prueba_subfieldframe.grid(row=0, column=0, sticky='nswe', padx=40, pady=40)

        def llamar_subasta():
            self.limpiar_frame(self.master_frame)

            titulo_func = 'Subastar'
            descripcion_func = 'Con esta funcionalidad es posible llevar a cabo subastas asi como su respectivo sistema de ofertado y designacion de ganadores.'

            subframe_descripcion = tk.Frame(self.master_frame, bg=FONDO)
            subframe_descripcion.grid(row=0, column=0, sticky='nswe', padx=20, ipady=20)
            subframe_descripcion.rowconfigure(0, weight=1, uniform='a')
            subframe_descripcion.rowconfigure(1, weight = 2, uniform='a')
            subframe_descripcion.columnconfigure(0, weight=1, uniform='a')

            tk.Label(subframe_descripcion, text=titulo_func, font=('Arial', 12, 'bold'), bg=FONDO).grid(row=0, column=0, padx=5, pady=5)
            descrp_func_widget = tk.Text(subframe_descripcion, bg=FONDO_2, font=('Arial', 9), wrap='word', bd=0)
            descrp_func_widget.insert(tk.END, descripcion_func)
            descrp_func_widget.grid(row=1, column=0, padx=5, pady=5)

            subframe_func = tk.Frame(self.master_frame, bg=FONDO, highlightbackground=DETALLES)
            subframe_func.grid(row=1, column=0, sticky='nswe')
            subframe_func.columnconfigure(0, weight=1, uniform='a')
            subframe_func.rowconfigure(0, weight=1, uniform='b')

            pantalla_subasta = FieldFrameSubasta(subframe_func, local, fecha)
            pantalla_subasta.grid(row=0, column=0, sticky='nswe', padx=40, pady=40)

        def llamar_empleado():
            self.limpiar_frame(self.master_frame)

            titulo_func = 'Gestionar empleado'
            descripcion_func = 'Mediante esta funcionalidad es posible analizar el rendimiento de los empleados del local y asignarles incentivos segun su rendimiento.'

            subframe_descripcion = tk.Frame(self.master_frame, bg=FONDO)
            subframe_descripcion.grid(row=0, column=0, sticky='nswe', padx=20, ipady=20)
            subframe_descripcion.rowconfigure(0, weight=1, uniform='a')
            subframe_descripcion.rowconfigure(1, weight = 2, uniform='a')
            subframe_descripcion.columnconfigure(0, weight=1, uniform='a')

            tk.Label(subframe_descripcion, text=titulo_func, font=('Arial', 12, 'bold'), bg=FONDO).grid(row=0, column=0, padx=5, pady=5)
            descrp_func_widget = tk.Text(subframe_descripcion, bg=FONDO_2, font=('Arial', 9), wrap='word', bd=0)
            descrp_func_widget.insert(tk.END, descripcion_func)
            descrp_func_widget.grid(row=1, column=0, padx=5, pady=5)

            subframe_func = tk.Frame(self.master_frame, bg=FONDO, highlightbackground=DETALLES)
            subframe_func.grid(row=1, column=0, sticky='nswe')
            subframe_func.columnconfigure(0, weight=1, uniform='a')
            subframe_func.rowconfigure(0, weight=1, uniform='b')

            prueba_subfieldframe = FieldFrameEmpleado(subframe_func, local, fecha)
            prueba_subfieldframe.grid(row=0, column=0, sticky='nswe', padx=40, pady=40)

        # Menubar
        menubar = tk.Menu(self.root)

        archivomenu = tk.Menu(menubar, tearoff=0)
        descripcion_app = 'Villajuegos es un software completo para compañias de tiendas especializadas en el mundo de los videojuegos que permite tanto llevar a cabo ventas, prestamos y subastas como gestionar y analizar el inventario de cada local y sus empleados'
        archivomenu.add_command(label="Aplicacion", command=lambda: messagebox.showinfo('Informacion', descripcion_app))
        archivomenu.add_command(label="Salir", command=lambda: VentanaPrincipal(self.root))
        menubar.add_cascade(label="Archivo", menu=archivomenu)

        procesomenu = tk.Menu(menubar, tearoff=0)
        procesomenu.add_command(label="Registrar compra", command=llamar_compra)
        procesomenu.add_command(label="Hacer prestamo", command=llamar_prestamo)
        procesomenu.add_command(label="Administrar inventario", command=llamar_administrar)
        procesomenu.add_command(label="Gestionar empleados", command=llamar_empleado)
        procesomenu.add_command(label="Subastar", command=llamar_subasta)
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

    @staticmethod
    def limpiar_frame(frame):
        for widget in frame.winfo_children():
            widget.destroy()

class FieldFrame(tk.Frame):
    def __init__(self, ventana, titulo_criterios, criterios, titulo_valores, valores=None, habilitados=None, aceptar_callback=None, tipos_esperados=None):
        super().__init__(ventana, bg=FONDO, highlightbackground=DETALLES, highlightthickness=2)

        self.aceptar_callback = aceptar_callback
        self.criterios = criterios
        self.valores = criterios if valores is None else valores
        self.tipos_esperados = tipos_esperados

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
        (tk.Button(self, text='Aceptar', bg=RESALTO, bd=0, command=self.al_aceptar)
        .grid(row=len(criterios) + 1, column=0, padx=35, sticky='e'))
        (tk.Button(self, text='Cancelar', bg= POWER, bd=0, command=lambda: self.cancelar(self.entries_val))
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

        for i in range(len(self.valores)):
            val = self.valores[i]
            fila = i + 1
            entr = tk.Entry(self)

            # Insertar valor inicial en el Entry si corresponde
            if valores is not None:
                if type(val) == str: entr.insert(0, val)

            # Habilitar o deshabilitar los Entry segun la lista habilitados
            if habilitados is not None: entr.config(state='normal' if habilitados[self.valores.index(val)] else 'disabled')
            entr.grid(row=fila, column=1, ipadx=45, padx=35, sticky='w')
            self.entries_val.append(entr)

    # Este metodo llama al metodo callback que se le ingrese al inicializado para que se pueda retornar el resultado de darle click al boton aceptar
    def al_aceptar(self):
        result = self.aceptar()
        if self.aceptar_callback:
            self.aceptar_callback(result)  # llamar el callback con los valores obtenidos

    def aceptar(self):
        try:
            lista_values = []
            # Buscar si hay algun campo vacio o de tipo invalido
            for cri in self.criterios:
                valor = self.getValue(cri)
                if valor == '': # Revisar si el campo esta vacio
                    raise ExceptionCampoVacio(self.entries_val, self.criterios)

                if self.tipos_esperados is not None:
                    if self.tipos_esperados[self.criterios.index(cri)] == 'str': # Si el tipo esperado es str
                        if valor.isdigit():
                            raise ExceptionTipoInvalido(self.entries_val, self.criterios, self.tipos_esperados)

                    if self.tipos_esperados[self.criterios.index(cri)] == 'int': # Si el tipo esperado es int
                        if not valor.isdigit():
                            raise ExceptionTipoInvalido(self.entries_val, self.criterios, self.tipos_esperados)

                lista_values.append(self.getValue(cri))

            return lista_values

        except ExceptionCampoVacio:
            # volver a colorear los campos invalidos una vez que se cierre la ventana emergente
            for entry in self.entries_val:
                entry.config(bg='white')

        except ExceptionTipoInvalido:
            # volver a colorear los campos invalidos una vez que se cierre la ventana emergente
            for entry in self.entries_val:
                entry.config(bg='white')

    def cancelar(self, entries_val):
        for entry in entries_val:
            # Si el entry esta deshabilitado, habilitarlo
            estaba_habilitado = False

            if entry.cget('state') == 'disabled':
                estaba_habilitado = True
                entry.config(state='normal')
            entry.delete(0, tk.END)
            if estaba_habilitado: entry.config(state='disabled')

# Fieldframes de funcionalidades

# Compra
class FieldFrameProducto(tk.Frame):
    def __init__(self, ventana, tienda_actual):
        super().__init__(ventana, bg=FONDO)

        self.carrito = []
        self.cliente_actual = None
        self.tienda_actual = tienda_actual

        self.framemain = tk.Frame(ventana, bg=FONDO)
        self.framemain.grid(row=0, column=0, sticky='nswe')

        self.identificar_cliente(self.framemain)

    # pantalla para seleccionar productos
    def identificar_producto(self):
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
        self.combobox_categoria.grid(row=0, column=1, padx=15, ipadx=40, pady=9)

        # Crear combobox con listado de productos segun la categoria ingresada
        def identificar_categoria_nombres(cat:str):
            return list(map(lambda producto: producto.__str__(), self.tienda_actual.get_productos_categoria_inventario(cat)))
        # ^ Ligadura dinámica

        self.listado_productos = []
        self.combobox_producto = ttk.Combobox(self.subframe1)

        def crear_listado(frame):
            listado_default = tk.StringVar(value='Elige un producto')
            listado_nombres = identificar_categoria_nombres(self.combobox_categoria.get())
            self.listado_productos = self.tienda_actual.get_productos_categoria_inventario(self.combobox_categoria.get())

            self.combobox_producto.config(values=listado_nombres, textvariable=listado_default)
            self.combobox_producto.grid(row=1, column=1, padx=15, ipadx=40, pady=9)

        # Boton para crear combobox listado
        self.boton_listado = tk.Button(self.subframe1, text='Buscar', font=('Arial', 9, 'bold'), bg=RESALTO, bd=0, command=lambda: crear_listado(self.subframe1))
        self.boton_listado.grid(row=0, column=2, padx=15, pady=9, sticky='w')

        # Insertar producto seleccionado
        self.producto_actual = None
        def insertar_producto():
            self.producto_actual = self.listado_productos[self.combobox_producto.current()]
            # Espacio del FieldFrame
            criterios = ['ID', 'Nombre', 'Precio', 'Cantidad', 'Fecha de lanzamiento']
            valores = [str(self.producto_actual.get_id()), self.producto_actual.get_nombre(), str(self.producto_actual.get_precio()), str(self.producto_actual.get_cantidad()), str(self.producto_actual.get_fecha_lanzamiento())]
            cri_habilitados = [False, False, False, False, False]

            def al_aceptar_callback(resultado):
                # buscar id del producto recibido en el inventario de la tienda actual
                producto_en_field = self.tienda_actual.buscar_producto_id(int(resultado[0]))

                try:
                    # identificar producto en el carrito si ya esta
                    producto_en_carrito = None
                    for producto in self.carrito:
                        if producto.get_id() == producto_en_field.get_id():  # Si el producto es reconocido
                            producto_en_carrito = producto
                            # Si la cantidad es insuficiente
                            if producto_en_field.get_cantidad() - producto_en_carrito.get_cantidad() == 0:
                                raise ExceptionCantidadInvalida()
                            break


                    if producto_en_carrito is not None:
                        producto_en_carrito.set_cantidad(producto_en_carrito.get_cantidad() + 1)
                    else:
                        # Agregar clon del producto al carrito
                        # la idea de usar un clon es para que el carrito maneje un atributo cantidad independiente
                        if producto_en_field.get_cantidad() == 0: # Si la cantidad es insuficiente
                            raise ExceptionCantidadInvalida()
                        producto_clonado = copy.deepcopy(producto_en_field)
                        producto_clonado.set_cantidad(1)
                        self.carrito.append(producto_clonado)

                    # mostrar nuevo total del carrito en la entry correspondiente
                    self.entry_total_carrito.config(state='normal')
                    self.entry_total_carrito.delete(0, tk.END)
                    nuevo_total = str(sum(map(lambda prod: prod.get_precio() * prod.get_cantidad(), self.carrito)))
                    self.entry_total_carrito.insert(0, nuevo_total)
                    self.entry_total_carrito.config(state='disabled')
                except ExceptionCantidadInvalida:
                    pass

            self.subframe2 = tk.Frame(self.framemain, bg=FONDO, bd=0)
            self.subframe2.grid(row=1, column=0)
            (FieldFrame(self.subframe2, 'Dato', criterios, 'Valor', valores, cri_habilitados, aceptar_callback=al_aceptar_callback)
                        .grid(row=0, column=0, padx=15, pady=9))

        # Boton para insertar producto seleccionado
        self.boton_producto = tk.Button(self.subframe1, text='Insertar', font=('Arial', 9, 'bold'), bg=RESALTO, bd=0, command=lambda: insertar_producto())
        self.boton_producto.grid(row=1, column=2, padx=15, pady=9, sticky='w')

        self.total_carrito()

    # metodo que muestra en un frame pequeño el costo total actual de los productos en el carrito y se actualiza
    def total_carrito(self):
        subframe3 = tk.Frame(self.framemain, bg=FONDO, bd=0)
        subframe3.grid(row=2, column=0)
        subframe3.columnconfigure((0,1), weight=1, uniform='a')
        subframe3.rowconfigure((0, 1), weight=1, uniform='b')

        tk.Label(subframe3, text='Total', font=('Arial', 11, 'bold'), bg=FONDO).grid(row=0, column=0, padx=15, pady=9, sticky='e')
        self.entry_total_carrito = tk.Entry(subframe3, state='disabled')
        self.entry_total_carrito.grid(row=0, column=1, padx=15, pady=9, sticky='w')

        def limpiar_carrito():
            self.carrito = []
            self.entry_total_carrito.config(state='normal')
            self.entry_total_carrito.delete(0, tk.END)
            self.entry_total_carrito.insert(0, '0')
            self.entry_total_carrito.config(state='disabled')

        tk.Button(subframe3, text='Comprar', font=('Arial', 9, 'bold'), bg=RESALTO, bd=0, command=self.pantalla_pago).grid(row=1, column=0, padx=15, pady=9, sticky='e')
        tk.Button(subframe3, text='Limpiar carrito', font=('Arial', 9, 'bold'), bg=POWER, bd=0, command=limpiar_carrito).grid(row=1, column=1, padx=15, pady=9, sticky='w')

    # metodo que limpia por completo el interior de el frame que reciba
    @staticmethod
    def limpiar_frame(frame):
        for widget in frame.winfo_children():
            widget.destroy()

    # pantalla para el pago de los productos de la compra
    def pantalla_pago(self):
        if len(self.carrito) == 0: # Si el carrito esta vacio, no hacer nada
            return

        self.limpiar_frame(self.framemain)
        subframe = tk.Frame(self.framemain, bg=FONDO, bd=0)
        subframe.grid(row=0, column=0, rowspan=2)
        subframe.columnconfigure(0, weight=1, uniform='a')
        subframe.rowconfigure(0, weight=3, uniform='b')
        subframe.rowconfigure((1,2), weight=1, uniform='b')

        def calcular_descuentos(carrito, cliente):
            total_final = 0
            puntos_usados = 0

            for prod in carrito:
                precio_final_individual = 0
                valor_temp = 0

                if prod.get_descuento() > 0: # En caso de que el producto tenga descuento
                    if prod.get_puntos_requeridos() == 0: # En caso de que el producto no requiera puntos
                        valor_temp = prod.get_precio() * prod.get_cantidad()
                        precio_final_individual = valor_temp - (valor_temp * prod.get_descuento() / 100) # calcular descuento
                        total_final += precio_final_individual

                    elif prod.get_puntos_requeridos() > 0 and (cliente.get_puntos_fidelidad() - puntos_usados) >= prod.get_puntos_requeridos():
                        valor_temp = prod.get_precio() * prod.get_cantidad()
                        precio_final_individual = valor_temp - (valor_temp * prod.get_descuento() / 100)
                        total_final += precio_final_individual

                        puntos_usados += prod.get_puntos_requeridos()
                    else: # En caso de que el cliente no tenga suficientes puntos
                        total_final += prod.get_precio() * prod.get_cantidad()

                else: # En caso de que el producto no tenga descuento
                    total_final += prod.get_precio() * prod.get_cantidad()

            return total_final, puntos_usados

        def confirmacion_pago(carrito, total, puntos, empleado):
            # Reflejar productos del carrito en el inventario del local
            for prod in carrito:
                prod_actual = self.tienda_actual.buscar_producto_id(prod.get_id())
                prod_actual.set_cantidad(prod_actual.get_cantidad() - prod.get_cantidad())

            # Actualizar puntos de fidelidad del cliente
            # Puntos gastados
            self.cliente_actual.set_puntos_fidelidad(self.cliente_actual.get_puntos_fidelidad() - puntos)

            # Puntos obtenidos
            puntos_obtenidos = int(total * 0.15)
            self.cliente_actual.set_puntos_fidelidad(self.cliente_actual.get_puntos_fidelidad() + puntos_obtenidos)

            # Limpiar carrito
            messagebox.showinfo('Compra realizada', f'Compra realizada con exito\nTotal: {total}\nPuntos usados: {puntos}\nPuntos obtenidos: {puntos_obtenidos}\nEmpleado: {empleado.get_nombre()}')

            # Hallar total sin descuentos
            total_sin_descuentos = sum(map(lambda prod: prod.get_precio() * prod.get_cantidad(), carrito))

            from src.gestorAplicacion.informacionVenta.Transaccion import Transaccion
            Transaccion(self.cliente_actual, empleado, self.tienda_actual, self.carrito, total_sin_descuentos, total)

            self.limpiar_frame(self.framemain)
            self.framemain.destroy()
            self.destroy()

        def al_confirmar_personal():
            try:
                from src.gestorAplicacion.personas.Empleado import Empleado
                cedula = int(combobox_empleado.get().split(' - ')[0])
                empleado_encontrado = Empleado.buscar_empleado(cedula, self.tienda_actual)

                # Comprobar que el empleado exista
                if empleado_encontrado is None:
                    raise ExceptionNoEncontrado('Empleado')

                # Entry con el pago total con descuentos aplicados
                pago_total, puntos_usados = calcular_descuentos(self.carrito, self.cliente_actual)

                total_entry = tk.Entry(subframe)
                total_entry.insert(0, str(pago_total))
                total_entry.grid(row=1, column=0, padx=15, pady=5)
                total_entry.config(state='disabled')

                # Boton para completar la compra
                (tk.Button(subframe, text='Completar compra', font=('Arial', 9, 'bold'), bg=RESALTO, bd=0, command=lambda: confirmacion_pago(self.carrito, pago_total, puntos_usados, empleado_encontrado))
                            .grid(row=2, column=0, padx=15, pady=5))

            except ExceptionNoEncontrado:
                pass

        subtotal = sum(map(lambda prod: prod.get_precio() * prod.get_cantidad(), self.carrito))

        # Subframe para poder organizar subtotal y empleado y sus entries
        subframe_subtotal_empleado = tk.Frame(subframe, bg=FONDO, bd=0)
        subframe_subtotal_empleado.grid(row=0, column=0)
        subframe_subtotal_empleado.columnconfigure((0,1), weight=1, uniform='a')
        subframe_subtotal_empleado.rowconfigure((0, 1, 2), weight=1, uniform='b')

        # Subtotal
        tk.Label(subframe_subtotal_empleado, text='Subtotal', font=('Arial', 11, 'bold'), bg=FONDO).grid(row=0, column=0, padx=15, pady=9, sticky='e')
        entry_subtotal = tk.Entry(subframe_subtotal_empleado)
        entry_subtotal.insert(0, str(subtotal))
        entry_subtotal.config(state='disabled')
        entry_subtotal.grid(row=0, column=1, padx=15, pady=9, sticky='w')

        # Empleado
        tk.Label(subframe_subtotal_empleado, text='Empleado', font=('Arial', 11, 'bold'), bg=FONDO).grid(row=1, column=0, padx=15, pady=9, sticky='e')

        values_empleados = []
        for empleado in self.tienda_actual.get_empleados():
            values_empleados.append(str(empleado.get_cedula()) + ' - ' + empleado.get_nombre())
        combobox_empleado = ttk.Combobox(subframe_subtotal_empleado, values=values_empleados)
        combobox_empleado.grid(row=1, column=1, padx=15, pady=9, sticky='w')

        # Boton para confirmar empleado
        tk.Button(subframe_subtotal_empleado, text='Confirmar', font=('Arial', 9, 'bold'), bg=RESALTO, bd=0, command=al_confirmar_personal).grid(row=2, column=0, columnspan=2, padx=15, pady=9)

    # metodo que genera temporalmente un frame para la creacion de un cliente
    def identificar_cliente(self, frame_c):
        frame_c.rowconfigure(0, weight=1, uniform='a')
        frame_c.columnconfigure(0, weight=1, uniform='b')

        # Crear frame para identificar o crear un cliente que despues se destruira
        mainframe_cliente = tk.Frame(frame_c, bg=FONDO, bd=0)
        mainframe_cliente.grid(row=0, column=0)

        # columnas y filas
        mainframe_cliente.columnconfigure((0, 1), weight=1, uniform='f')
        mainframe_cliente.rowconfigure((0, 1), weight=1, uniform='g')

        def cliente_existente():
            self.limpiar_frame(mainframe_cliente)

            def al_cliente_existente_callback(resultado):
                try:
                    cliente_encontrado = Cliente.buscar_cliente(int(resultado[0]))
                    if cliente_encontrado is None:
                        raise ExceptionNoEncontrado('Cliente')

                    self.cliente_actual = cliente_encontrado

                    messagebox.showinfo('Cliente encontrado', f'Cliente {cliente_encontrado.get_nombre()} identificado con exito\n')

                    mainframe_cliente.destroy()
                    self.identificar_producto()
                except ExceptionNoEncontrado:
                    pass

            # fieldframe para identificacion
            criterios_cliente = ['Identificacion']
            FieldFrame(mainframe_cliente, 'Dato', criterios_cliente, 'Valor', None, None, aceptar_callback=al_cliente_existente_callback, tipos_esperados=['int']).grid(row=0, column=0, rowspan=2, columnspan=2)

        def crear_cliente():
            self.limpiar_frame(mainframe_cliente)

            def al_crear_cliente_callback(resultado):
                cedula = int(resultado[0])
                nombre = resultado[1]
                correo = resultado[2]
                telefono = resultado[3]

                # Crear cliente
                cliente_creado = Cliente(cedula, nombre, correo, telefono)

                self.cliente_actual = cliente_creado

                messagebox.showinfo('Cliente creado', f'Cliente {nombre} creado con exito')
                mainframe_cliente.destroy()
                self.identificar_producto()

            # fieldframe para creacion
            criterios_cliente = ['Identificacion', 'Nombre', 'Correo', 'Telefono']
            FieldFrame(mainframe_cliente, 'Dato', criterios_cliente, 'Valor', None, None, aceptar_callback=al_crear_cliente_callback, tipos_esperados=['int', 'str', 'str', 'int']).grid(row=0, column=0, rowspan=2, columnspan=2)

        tk.Label(mainframe_cliente, text='¿El cliente esta registrado o es nuevo?', font=('Arial', 11, 'bold'), bg=FONDO).grid(row=0, column=0, columnspan=2, padx=15, pady=9, ipadx=30)
        # Botones
        tk.Button(mainframe_cliente, text='Registrado', font=('Arial', 9, 'bold'), bg=RESALTO, bd=0, command=cliente_existente).grid(row=1, column=0, padx=15, pady=9, sticky='e')
        tk.Button(mainframe_cliente, text='Nuevo', font=('Arial', 9, 'bold'), bg=POWER, bd=0, command=crear_cliente).grid(row=1, column=1, padx=15, pady=9, sticky='w')

# Prestamo
class FieldFramePrestamo(FieldFrameProducto):
    def __init__(self, ventana, tienda_actual, fecha_actual):
        super().__init__(ventana, tienda_actual)
        self.fecha_actual = fecha_actual
        self.hay_vencidos = False

    # pantalla para seleccionar productos para el prestamo
    def identificar_producto(self):
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
            return list(map(lambda producto: producto.get_nombre(), self.tienda_actual.get_productos_categoria_inventario(cat, 'prestamo')))

        self.listado_productos = []
        self.combobox_producto = ttk.Combobox(self.subframe1)

        def crear_listado(frame):
            listado_default = tk.StringVar(value='Elige un producto')
            listado_nombres = identificar_categoria_nombres(self.combobox_categoria.get())
            self.listado_productos = self.tienda_actual.get_productos_categoria_inventario(self.combobox_categoria.get(), 'prestamo')

            self.combobox_producto.config(values=listado_nombres, textvariable=listado_default)
            self.combobox_producto.grid(row=1, column=1, padx=15, pady=15)

        # Boton para crear combobox listado
        self.boton_listado = tk.Button(self.subframe1, text='Buscar', font=('Arial', 9, 'bold'), bg=RESALTO, bd=0, command=lambda: crear_listado(self.subframe1))
        self.boton_listado.grid(row=0, column=2, padx=15, pady=15, sticky='w')

        # Insertar producto seleccionado
        self.producto_actual = None
        def insertar_producto():
            self.producto_actual = self.listado_productos[self.combobox_producto.current()]
            # Espacio del FieldFrame
            criterios = ['ID', 'Nombre', 'Costo/dia', 'Cantidad', 'Fecha de lanzamiento']
            valores = [str(self.producto_actual.get_id()), self.producto_actual.get_nombre(), str(self.producto_actual.get_precio()), str(self.producto_actual.get_cantidad()), str(self.producto_actual.get_fecha_lanzamiento())]
            cri_habilitados = [False, False, False, False, False]

            def al_aceptar_callback(resultado):
                # buscar id del producto recibido en el inventario de la tienda actual
                producto_en_field = self.tienda_actual.buscar_producto_id(int(resultado[0]), 'prestamo')

                try:
                    # identificar producto en el carrito si ya esta
                    producto_en_carrito = None
                    for producto in self.carrito:
                        if producto.get_id() == producto_en_field.get_id():  # Si el producto es reconocido
                            producto_en_carrito = producto
                            # Si la cantidad es insuficiente
                            if producto_en_field.get_cantidad() - producto_en_carrito.get_cantidad() == 0:
                                raise ExceptionCantidadInvalida()
                            break


                    if producto_en_carrito is not None:
                        producto_en_carrito.set_cantidad(producto_en_carrito.get_cantidad() + 1)
                    else:
                        # Agregar clon del producto al carrito
                        # la idea de usar un clon es para que el carrito maneje un atributo cantidad independiente
                        if producto_en_field.get_cantidad() == 0: # Si la cantidad es insuficiente
                            raise ExceptionCantidadInvalida()
                        producto_clonado = copy.deepcopy(producto_en_field)
                        producto_clonado.set_cantidad(1)
                        self.carrito.append(producto_clonado)

                    # mostrar nuevo total del carrito en la entry correspondiente
                    self.entry_total_carrito.config(state='normal')
                    self.entry_total_carrito.delete(0, tk.END)
                    nuevo_total = str(sum(map(lambda prod: prod.get_precio() * prod.get_cantidad(), self.carrito)))
                    self.entry_total_carrito.insert(0, nuevo_total)
                    self.entry_total_carrito.config(state='disabled')
                except ExceptionCantidadInvalida:
                    pass

            self.subframe2 = tk.Frame(self.framemain, bg=FONDO, bd=0)
            self.subframe2.grid(row=1, column=0)
            (FieldFrame(self.subframe2, 'Dato', criterios, 'Valor', valores, cri_habilitados, aceptar_callback=al_aceptar_callback)
                        .grid(row=0, column=0, padx=15, pady=15))

        # Boton para insertar producto seleccionado
        self.boton_producto = tk.Button(self.subframe1, text='Insertar', font=('Arial', 9, 'bold'), bg=RESALTO, bd=0, command=lambda: insertar_producto())
        self.boton_producto.grid(row=1, column=2, padx=15, pady=15, sticky='w')

        self.total_carrito()

    # metodo que muestra en un frame pequeño el costo total actual de los productos en el carrito y se actualiza
    def pantalla_pago(self):
        if len(self.carrito) == 0: # Si el carrito esta vacio, no hacer nada
            return

        self.limpiar_frame(self.framemain)
        subframe = tk.Frame(self.framemain, bg=FONDO, bd=0)
        subframe.grid(row=0, column=0, rowspan=2)
        subframe.columnconfigure(0, weight=1, uniform='a')
        subframe.rowconfigure(0, weight=3, uniform='b')
        subframe.rowconfigure((1,2), weight=1, uniform='b')

        def confirmacion_pago(valor_total, dias):
            # Reflejar productos del carrito en el inventario del local
            for prod in self.carrito:
                prod_actual = self.tienda_actual.buscar_producto_id(prod.get_id(), 'prestamo')
                prod_actual.set_cantidad(prod_actual.get_cantidad() - prod.get_cantidad())

            # Crear prestamo
            fecha_fin = Fecha(int(self.fecha_actual.get_total_dias() + dias))

            from src.gestorAplicacion.informacionVenta.Prestamo import Prestamo
            Prestamo(fecha_fin, self.cliente_actual, self.carrito, valor_total, 'Activo')

            # Limpiar
            messagebox.showinfo('Prestamo realizado', f'Prestamo realizado con exito\nTotal: {valor_total}\nDias de plazo: {dias}\nCliente: ' + self.cliente_actual.get_nombre())
            self.limpiar_frame(self.framemain)
            self.framemain.destroy()
            self.destroy()

        def al_confirmar_prest():
            try:
                if combobox_plazo.get() == '':
                    raise ExceptionCampoVacio([combobox_plazo], 'Plazo')

                valor_total = sum(map(lambda prod: (prod.get_precio() * prod.get_cantidad()), self.carrito))
                dias = 0
                total_dias = int(combobox_plazo.get())

                match total_dias:
                    case 14:
                        dias = 14
                        valor_total = valor_total * dias
                    case 30:
                        dias = 30
                        valor_total = valor_total * dias
                    case 45:
                        dias = 45
                        valor_total = int(valor_total * dias * 0.9)
                    case 60:
                        dias = 60
                        valor_total = int(valor_total * dias * 0.85)
                    case _:
                        raise ExceptionCampos('Error en ingreso de plazo')

                total_entry = tk.Entry(subframe)
                total_entry.insert(0, str(valor_total))
                total_entry.grid(row=1, column=0, padx=15, pady=5)
                total_entry.config(state='disabled')

                # Boton para completar la compra
                (tk.Button(subframe, text='Completar compra', font=('Arial', 9, 'bold'), bg=RESALTO, bd=0, command=lambda: confirmacion_pago(valor_total, dias))
                            .grid(row=2, column=0, padx=15, pady=5))

            except ExceptionCampos:
                pass

        subtotal = sum(map(lambda prod: prod.get_precio() * prod.get_cantidad(), self.carrito))

        # Subframe para poder organizar subtotal y empleado y sus entries
        subframe_subtotal_empleado = tk.Frame(subframe, bg=FONDO, bd=0)
        subframe_subtotal_empleado.grid(row=0, column=0)
        subframe_subtotal_empleado.columnconfigure((0,1), weight=1, uniform='a')
        subframe_subtotal_empleado.rowconfigure((0, 1, 2), weight=1, uniform='b')

        # Subtotal
        tk.Label(subframe_subtotal_empleado, text='Subtotal', font=('Arial', 11, 'bold'), bg=FONDO).grid(row=0, column=0, padx=15, pady=15, sticky='e')
        entry_subtotal = tk.Entry(subframe_subtotal_empleado)
        entry_subtotal.insert(0, str(subtotal))
        entry_subtotal.config(state='disabled')
        entry_subtotal.grid(row=0, column=1, padx=15, pady=15, sticky='w')

        # Plazo
        tk.Label(subframe_subtotal_empleado, text='Dias de plazo', font=('Arial', 11, 'bold'), bg=FONDO).grid(row=1, column=0, padx=15, pady=15, sticky='e')

        values_dias = [str(14), str(30), str(45), str(60)]
        combobox_plazo = ttk.Combobox(subframe_subtotal_empleado, values=values_dias)
        combobox_plazo.grid(row=1, column=1, padx=15, pady=15, sticky='w')

        # Boton para confirmar prestamo
        tk.Button(subframe_subtotal_empleado, text='Confirmar', font=('Arial', 9, 'bold'), bg=RESALTO, bd=0, command=al_confirmar_prest).grid(row=2, column=0, columnspan=2, padx=15, pady=15)

    # genera temporalmente un frame para la creacion de un cliente
    def identificar_cliente(self, frame_c):
        frame_c.rowconfigure(0, weight=1, uniform='a')
        frame_c.columnconfigure(0, weight=1, uniform='b')

        # Crear frame para identificar o crear un cliente que despues se destruira
        mainframe_cliente = tk.Frame(frame_c, bg=FONDO, bd=0)
        mainframe_cliente.grid(row=0, column=0)

        # Columnas y filas
        mainframe_cliente.columnconfigure((0, 1), weight=1, uniform='f')
        mainframe_cliente.rowconfigure((0, 1), weight=1, uniform='g')

        def cliente_existente():
            self.limpiar_frame(mainframe_cliente)

            def al_cliente_existente_callback(resultado):
                try:
                    cliente_encontrado = Cliente.buscar_cliente(int(resultado[0]))
                    if cliente_encontrado is None:
                        raise ExceptionNoEncontrado('Cliente')

                    self.cliente_actual = cliente_encontrado

                    messagebox.showinfo('Cliente encontrado', f'Cliente {cliente_encontrado.get_nombre()} identificado con exito\n')

                    # Comprobacion de prestamos vencidos
                    self.hay_vencidos = False
                    for prestamo in self.cliente_actual.get_prestamos():
                        if prestamo.get_fecha_fin().get_total_dias() < self.fecha_actual.get_total_dias() and prestamo.get_estado() == 'Activo':
                            prestamo.set_estado('Vencido')
                            self.hay_vencidos = True

                        elif prestamo.get_estado() == 'Vencido':
                            self.hay_vencidos = True

                    # Elegir entre devolver o realizar prestamo
                    mainframe_cliente.destroy()
                    self.elegir_prestar_devolver()
                except ExceptionNoEncontrado:
                    pass

            # fieldframe para identificacion
            criterios_cliente = ['Identificacion']
            FieldFrame(mainframe_cliente, 'Dato', criterios_cliente, 'Valor', None, None, aceptar_callback=al_cliente_existente_callback).grid(row=0, column=0, rowspan=2, columnspan=2)

        def crear_cliente():
            self.limpiar_frame(mainframe_cliente)

            def al_crear_cliente_callback(resultado):
                cedula = int(resultado[0])
                nombre = resultado[1]
                correo = resultado[2]
                telefono = resultado[3]

                # Crear cliente
                cliente_creado = Cliente(cedula, nombre, correo, telefono)

                self.cliente_actual = cliente_creado

                messagebox.showinfo('Cliente creado', f'Cliente {nombre} creado con exito')
                mainframe_cliente.destroy()
                self.identificar_producto()

            # fieldframe para creacion
            criterios_cliente = ['Identificacion', 'Nombre', 'Correo', 'Telefono']
            FieldFrame(mainframe_cliente, 'Dato', criterios_cliente, 'Valor', None, None, aceptar_callback=al_crear_cliente_callback, tipos_esperados=['int', 'str', 'str', 'int']).grid(row=0, column=0, rowspan=2, columnspan=2)

        tk.Label(mainframe_cliente, text='¿El cliente esta registrado o es nuevo?', font=('Arial', 11, 'bold'), bg=FONDO).grid(row=0, column=0, columnspan=2, padx=15, pady=15, ipadx=30)
        # Botones
        tk.Button(mainframe_cliente, text='Registrado', font=('Arial', 9, 'bold'), bg=RESALTO, bd=0, command=cliente_existente).grid(row=1, column=0, padx=15, pady=15, sticky='e')
        tk.Button(mainframe_cliente, text='Nuevo', font=('Arial', 9, 'bold'), bg=POWER, bd=0, command=crear_cliente).grid(row=1, column=1, padx=15, pady=15, sticky='w')

    # pantalla para escoger entre prestar o devolver una vez ya este seleccionado el cliente
    def elegir_prestar_devolver(self):
        self.limpiar_frame(self.framemain)

        self.framemain.columnconfigure(0, weight=1, uniform='a')
        self.framemain.rowconfigure(0, weight=1, uniform='b')

        subframe1 = tk.Frame(self.framemain, bg=FONDO, bd=0)
        subframe1.grid(row=0, column=0)
        subframe1.rowconfigure((0, 1), weight=1, uniform='a')
        subframe1.columnconfigure((0, 1), weight=1, uniform='b')

        tk.Label(subframe1, text='¿Desea prestar o devolver un producto?', font=('Arial', 11, 'bold'), bg=FONDO).grid(row=0, column=0, columnspan=2, padx=15, pady=15, ipadx=30)
        tk.Button(subframe1, text='Prestar', font=('Arial', 9, 'bold'), bg=RESALTO, bd=0, command=self.prestar).grid(row=1, column=0, padx=15, pady=15, sticky='e')
        tk.Button(subframe1, text='Devolver', font=('Arial', 9, 'bold'), bg=POWER, bd=0, command=self.devolver).grid(row=1, column=1, padx=15, pady=15, sticky='w')

    # metodo que llama a la pantalla para seleccion de productos para el prestamo. No se ejecuta si hay prestamos vencidos para el cliente
    def prestar(self):
        # Comprobacion de prestamos vencidos
        self.hay_vencidos = False
        for prestamo in self.cliente_actual.get_prestamos():
            if prestamo.get_fecha_fin().get_total_dias() < self.fecha_actual.get_total_dias() and prestamo.get_estado() == 'Activo':
                prestamo.set_estado('Vencido')
                self.hay_vencidos = True

            elif prestamo.get_estado() == 'Vencido':
                self.hay_vencidos = True

        if self.hay_vencidos:
            messagebox.showinfo('Prestamo no disponible', 'No se puede realizar prestamo, el cliente tiene prestamos vencidos')
            return

        self.limpiar_frame(self.framemain)
        self.identificar_producto()

    # pantalla para seleccion de prestamos activos o vencidos para devolver
    def devolver(self):
        hay_prestamos_activos_vencidos = False
        for prestamo in self.cliente_actual.get_prestamos():
            if prestamo.get_estado() == 'Activo' or prestamo.get_estado() == 'Vencido':
                hay_prestamos_activos_vencidos = True
                break

        if not hay_prestamos_activos_vencidos:
            messagebox.showinfo('Devolucion no disponible', 'No se puede realizar devolucion, el cliente no tiene prestamos activos o vencidos')
            return

        self.limpiar_frame(self.framemain)
        subframe1 = tk.Frame(self.framemain, bg=FONDO, bd=0)
        subframe1.grid(row=0, column=0,sticky='nswe')
        subframe1.columnconfigure((0,1), weight=1, uniform='a')
        subframe1.rowconfigure((0,2), weight=1, uniform='b')
        subframe1.rowconfigure(1, weight=4, uniform='b')
        #filas: seleccionar prestamo - boton confirmar prestamo -> dibujar:  mostrar total dias - mostrar total a pagar - mostrar productos en combobox - boton confirmar

        self.ids_prestamos = []

        def actualizar_prestamos_activos():
            values_prestamos = []
            self.ids_prestamos = []
            for prestamo in self.cliente_actual.get_prestamos():
                if prestamo.get_estado() == 'Activo' or prestamo.get_estado() == 'Vencido':
                    values_prestamos.append('ID: ' + str(prestamo.get_id()) + ' | Fecha fin: ' + str(
                        prestamo.get_fecha_fin()) + ' | ' + prestamo.get_estado())
                    self.ids_prestamos.append(prestamo.get_id())

            return values_prestamos

        def confirmar_prestamo_seleccionado():
            # Buscar id del prestamo en la lista de prestamos del cliente
            try:
                if self.combobox_prestamo_selec.get() == 'Elige un prestamo' or self.combobox_prestamo_selec.get() == '':
                    raise ExceptionCampoVacio([self.combobox_prestamo_selec], ['Prestamo'])

                id_prestamo = self.ids_prestamos[self.combobox_prestamo_selec.current()]
                prestamo_seleccionado = None
                for prestamo in self.cliente_actual.get_prestamos():
                    if prestamo.get_id() == id_prestamo:
                        prestamo_seleccionado = prestamo
                        break

                if prestamo_seleccionado is None:
                    raise ExceptionNoEncontrado('Prestamo')

                # Abrir subframe para mostrar total de dias y total a pagar
                subframe2 = tk.Frame(self.framemain, bg=FONDO, bd=0)
                subframe2.grid(row=1, column=0)
                subframe2.columnconfigure((0,1,2,3), weight=1, uniform='a')

                # total dias
                total_dias = int(prestamo_seleccionado.get_fecha_fin().get_total_dias() - self.fecha_actual.get_total_dias())

                tk.Label(subframe2, text='Total dias', font=('Arial', 11, 'bold'), bg=FONDO).grid(row=0, column=0, padx=15, pady=15, sticky='e')
                entry_total_dias = tk.Entry(subframe2)
                entry_total_dias.insert(0, str(total_dias))
                entry_total_dias.config(state='disabled')
                entry_total_dias.grid(row=0, column=1, padx=15, pady=15, sticky='w')

                # total a pagar si el prestamo esta vencido
                tk.Label(subframe2, text='Total a pagar', font=('Arial', 11, 'bold'), bg=FONDO).grid(row=1, column=0, padx=15, pady=15, sticky='e')
                total_pagar = 0
                if prestamo_seleccionado.get_estado() == 'Vencido':
                    for producto in prestamo_seleccionado.get_productos():
                        total_pagar += producto.get_precio() * abs(total_dias) * 1.1
                entry_total_a_pagar = tk.Entry(subframe2)
                entry_total_a_pagar.insert(0, str(total_pagar))
                entry_total_a_pagar.config(state='disabled')
                entry_total_a_pagar.grid(row=1, column=1, padx=15, pady=15, sticky='w')

                # listado de productos en combobox
                tk.Label(subframe2, text='Productos', font=('Arial', 11, 'bold'), bg=FONDO).grid(row=2, column=0, padx=15, pady=15, sticky='e')
                combobox_producto = ttk.Combobox(subframe2, values=prestamo_seleccionado.get_productos(), state='readonly')
                combobox_producto.grid(row=2, column=1, padx=15, pady=15, sticky='w')

                def confirmar_devolucion():
                    # Cambiar estado del prestamo a 'Devuelto'
                    prestamo_seleccionado.set_estado('Devuelto')

                    # Actualizar cantidad de productos en el inventario
                    for producto in prestamo_seleccionado.get_productos():
                        producto_actual = self.tienda_actual.buscar_producto_id(producto.get_id(), 'prestamo')
                        producto_actual.set_cantidad(producto_actual.get_cantidad() + producto.get_cantidad())

                    messagebox.showinfo('Devolucion realizada', f'Devolucion realizada con exito')
                    self.limpiar_frame(self.framemain)
                    self.elegir_prestar_devolver()

                # boton para confirmar devolucion
                tk.Button(subframe2, text='Confirmar devolucion', font=('Arial', 9, 'bold'), bg=RESALTO, bd=0, command=confirmar_devolucion).grid(row=3, column=0, rowspan=2, columnspan=2, padx=15, pady=15)


            except ExceptionNoEncontrado:
                pass
            except ExceptionCampoVacio:
                pass

        # Seleccionar prestamo

        valor_defecto = tk.StringVar(value='Elige un prestamo')
        self.combobox_prestamo_selec = ttk.Combobox(subframe1, values=actualizar_prestamos_activos(), textvariable=valor_defecto)
        self.combobox_prestamo_selec.grid(row=0, column=0, padx=15, pady=15, ipadx=60, sticky='e')

        tk.Button(subframe1, text='Confirmar prestamo', font=('Arial', 9, 'bold'), bg=RESALTO, bd=0, command=confirmar_prestamo_seleccionado).grid(row=0, column=1, padx=15, pady=15, ipadx=60, sticky='w')
        tk.Button(subframe1, text='Volver', font=('Arial', 9, 'bold'), bg=POWER, bd=0, command=self.elegir_prestar_devolver).grid(row=2, column=0, columnspan=2, padx=15, pady=15, ipadx=60)

# Administrar inventario
class FieldFrameAdministrar(tk.Frame):
    etiquetas = []
    def __init__(self,ventana,tienda_actual:Tienda):
        super().__init__(ventana,bg=FONDO)
        self.tienda_actual = tienda_actual
        self.ventana = ventana

        self.framemain = tk.Frame(ventana,bg=FONDO)
        self.framemain.grid(row=0,column=0,sticky='nswe')
        self.framemain.rowconfigure(0,weight=1,uniform='a')
        self.framemain.columnconfigure(0,weight=1,uniform='b')

        self.subframe1 = tk.Frame(self.framemain,bg=FONDO,bd=0)
        self.subframe1.grid(row=0,column=0,sticky='nswe')
        self.subframe1.rowconfigure((0,5),weight=3,uniform='aa')
        self.subframe1.rowconfigure((1,2,3,4),weight=2,uniform='aa')
        self.subframe1.columnconfigure((0,2),weight=2,uniform='bb')
        self.subframe1.columnconfigure(1,weight=1,uniform='bb')
        self.subframe2 = tk.Frame(self.framemain,bg=FONDO,bd=0)
        self.subframe3 = tk.Frame(self.framemain,bg=FONDO,bd=0)
        self.subframe4 = tk.Frame(self.framemain,bg=FONDO,bd=0)
        self.subframe5 = tk.Frame(self.framemain,bg=FONDO,bd=0)

        #Metodos

        def revisar_producto():
            self.subframe1 = tk.Frame(self.framemain,bg=FONDO,bd=0)
            self.subframe1.grid(row=0,column=0,sticky='nswe')
            self.limpiar_frame(self.subframe1)

            self.framemain.rowconfigure((0,1,2), weight=1, uniform='a')
            self.framemain.rowconfigure(3, weight=10, uniform='a')
            self.framemain.rowconfigure(4, weight=2, uniform='a')

            #parte de arriba
            self.subframe1 = tk.Frame(self.framemain, bg=FONDO, bd=0)
            self.subframe1.grid(row=0, column=0, sticky='nswe')
            self.subframe1.rowconfigure((0,1), weight=1, uniform='aa')
            self.subframe1.columnconfigure((0,1,2), weight=1, uniform='bb')
            self.subframe2 = tk.Frame(self.framemain, bg=FONDO, bd=0)
            self.subframe2.grid(row=1, column=0, sticky='nswe')
            self.subframe3 = tk.Frame(self.framemain, bg=FONDO, bd=0)
            self.subframe3.grid(row=2, column=0, sticky='nswe')
            self.subframe4 = tk.Frame(self.framemain, bg=FONDO, bd=0)
            self.subframe4.grid(row=3, column=0, sticky='nswe')
            self.subframe5 = tk.Frame(self.framemain, bg=FONDO, bd=0)
            self.subframe5.grid(row=4, column=0, sticky='nswe')

            tk.Label(self.subframe1, text='Revisar', font=('Arial', 11, 'bold'), bg=FONDO).grid(row=0, column=0, padx=15, pady=0, sticky='e')

            revisar_default = tk.StringVar(value=' ---- ')
            combobox_eleccion = ttk.Combobox(self.subframe1, values=['Todos', 'Tipo'], textvariable=revisar_default)
            combobox_eleccion.grid(row=0, column=1, padx=5, pady=0, sticky='we')
            def llamareleccion(elec):
                if elec == 'Todos':
                    self.limpiar_frame(self.subframe2)
                    self.limpiar_frame(self.subframe3)
                    self.limpiar_frame(self.subframe4)
                    self.limpiar_frame(self.subframe5)
                    self.ordenar(["nombre","ventas","precio"],2)

                elif elec == 'Tipo':
                    self.limpiar_frame(self.subframe2)
                    self.limpiar_frame(self.subframe3)
                    self.limpiar_frame(self.subframe4)
                    self.categoria()

            tk.Button(self.subframe1, text='Buscar', bg=RESALTO, bd=0, command=lambda: llamareleccion(combobox_eleccion.get())).grid(row=0, column=2, padx=15, pady=0, sticky='w')
            tk.Button(self.subframe5, text='Regresar', bg=RESALTO, bd=0, command=lambda: self.regreso()).grid(row=0, column=3, padx=15, pady=0, sticky='w')

        def modificar_producto():
            self.limpiar_frame(self)
            self.limpiar_frame(self.subframe1)
            self.framemain.rowconfigure(0, weight=1, uniform='a')
            self.framemain.rowconfigure((2,3),weight=1,uniform='a')
            self.framemain.rowconfigure(1, weight=10,uniform='a')
            self.subframe1 = tk.Frame(self.framemain,bg=FONDO,bd=0)
            self.subframe2.grid(row=1,column=0,sticky='nswe')
            self.subframe2.columnconfigure(0,weight=1,uniform='a')
            self.subframe3.grid(row=2,column=0,sticky='nswe')
            self.subframe3.columnconfigure((0,1,2),weight=1,uniform='a')
            tk.Label(self.subframe3, text='Ingrese el código', font=('Arial', 11, 'bold'), bg=FONDO).grid(row=0,column=0, padx=15,pady=0,sticky='e')
            codigo = tk.Entry(self.subframe3)
            codigo.grid(row=0, column=1, padx=15, pady=0, sticky='we')
            def comprobarCodigo(valor):
                try:
                    cod = eval(valor)
                    producto = self.tienda_actual.buscar_producto_id(cod)
                    if producto is None:
                        raise ExceptionNoEncontrado('Producto')
                    self.cambiarinfo(producto)
                except ExceptionNoEncontrado:
                    pass
            tk.Button(self.subframe3, text='Buscar', bg=RESALTO, bd=0, command=lambda: comprobarCodigo(codigo.get())).grid(row=0,column=2,padx=15,pady=0,sticky='w')

            self.categoria1()

        def revisar_prioridad():
            self.limpiar_frame(self.subframe1)

        # Botones
        tk.Button(self.subframe1, text='Revisar productos', bg=botoncito, bd=0,
                  command=lambda: revisar_producto()).grid(row=1, column=1, padx=15, pady=15, sticky='nswe')
        tk.Button(self.subframe1, text='Modificar producto', bg=botoncito, bd=0,
                  command=lambda: modificar_producto()).grid(row=2, column=1, padx=15, pady=15, sticky='nswe')
        tk.Button(self.subframe1, text='Revisar prioridad', bg=botoncito, bd=0,
                  command=lambda: revisar_prioridad()).grid(row=3, column=1, padx=15, pady=15, sticky='nswe')
        tk.Button(self.subframe1, text='Regresar', bg=botoncito, bd=0).grid(row=4, column=1, padx=15, pady=15,
                                                                            sticky='nswe')
    def regreso(self):
        self.limpiar_frame(self.framemain)
        self.framemain.destroy()
        self.destroy()
        FieldFrameAdministrar(self.ventana,self.tienda_actual)

    def categoria1(self):
        # Crear un combobox para elegir categoria y su boton de acción
        self.subframe1.grid(row=0, column=0, sticky='nswe')
        self.subframe1.columnconfigure((0, 1, 2), weight=1, uniform='aa')
        tk.Label(self.subframe1, text='Categoria', font=('Arial', 11, 'bold'), bg=FONDO).grid(row=0, column=0, padx=15,
                                                                                              pady=0, sticky='e')
        categoriaDefault = tk.StringVar(value='-------')
        combobox_categoria = ttk.Combobox(self.subframe1, values=['Consola', 'Juego', 'Accesorio'],
                                          textvariable=categoriaDefault)
        combobox_categoria.grid(row=0, column=1, padx=5, pady=0, sticky='we')
        self.subframe2.grid(row=1, column=0, sticky='nswe')
        def cosas():
            self.subframe2.destroy()
            self.subframe2 = tk.Frame(self.framemain, bg=FONDO, bd=0)
            self.subframe2.grid(row=1, column=0, sticky='nswe')
            self.subframe2.rowconfigure(0, weight=1, uniform='aa')
            self.crear_etiquetas(self.subframe2,self.tienda_actual.get_productos_categoria_inventario(combobox_categoria.get()))
        tk.Button(self.subframe1, text='Buscar', bg=RESALTO, bd=0,command=lambda: cosas()).grid(row=0,column=2,padx=15,pady=0,sticky='w')

    def cambiarinfo(self,producto:Producto):
        self.limpiar_frame(self.subframe2)
        self.subframe2 = FieldFrame(self.subframe2, 'Cambiar', ['ID','Nuevo ID', 'Nombre','Nuevo Nombre' ,'Precio','Nuevo Precio' , 'Fecha de lanzamiento','Nueva Fecha'], 'Valor', [f'{producto.get_id()}', '', f'{producto.get_nombre()}', '', f'{producto.get_precio()}', '', f'{producto.get_fecha_lanzamiento()}', ''], [False, True, False, True, False, True, False, True])
        self.subframe2.grid(row=1,column=0,sticky='nswe')
    def categoria(self):
        #Crear un combobox para elegir categoria y su boton de acción
        self.subframe2.grid(row=1, column=0, sticky='nswe')
        self.subframe2.columnconfigure((0,1,2), weight=1, uniform='aa')
        tk.Label( self.subframe2,text='Categoria', font=('Arial', 11, 'bold'), bg=FONDO).grid(row=1, column=0, padx=15, pady=0, sticky='e')
        categoriaDefault = tk.StringVar(value='-------')
        combobox_categoria = ttk.Combobox(self.subframe2, values=['Consola', 'Juego', 'Accesorio'], textvariable=categoriaDefault)
        combobox_categoria.grid(row=1, column=1, padx=5, pady=0, sticky='we')
        tk.Button(self.subframe2, text='Buscar', bg=RESALTO, bd=0,command=lambda: self.ordenar(["nombre","ventas","precio"],2,combobox_categoria.get())).grid(row=1, column=2, padx=15, pady=0, sticky='w')

    def ordenar(self,lista:list[str],fila,cat=None):
        if cat not in ['Consola','Juego','Accesorio']:
            cat = None
        self.subframe3.grid(row=2, column=0, sticky='nswe')
        self.subframe3.columnconfigure((0,1,2), weight=1, uniform='aa')
        #crear un combobox para elegir como ordenar y su boton de accion
        tk.Label(self.subframe3,text='Ordenar',font=('Arial', 11, 'bold'),bg=FONDO).grid(row=fila, column=0, padx=15, pady=0, sticky='e')
        ordenarDefecto = tk.StringVar(value=' -------- ')
        #crear combobox
        combobox_ordenar = ttk.Combobox(self.subframe3,values=lista,textvariable=ordenarDefecto)
        combobox_ordenar.grid(row=fila,column= 1,padx=5,pady=0, sticky='we')
        if cat is not None:
            listaObjetos = self.tienda_actual.get_productos_categoria_inventario(cat)
        else:
            listaObjetos = self.tienda_actual.get_inventario()
        def miniordenar(orden,lista1):
            Producto.ordenar(orden, lista1)
            self.eleccion(lista1)
        #Boton para buscar
        tk.Button(self.subframe3,text='Buscar',bg=RESALTO,bd=0,command=lambda:miniordenar(combobox_ordenar.get(),listaObjetos)).grid(row=fila,column=2,padx=15,pady=0,sticky='w')

    @staticmethod
    def crear_etiquetas(frame:Frame,lista:list[Producto]):
        # Obtener el número ingresado por el usuario
        # Limpiar etiquetas anteriores
        for label in frame.grid_slaves(column=0):
            label.destroy()
        p = -1
        q = -1
        # Crear las nuevas etiquetas
        for i in lista:
            frame.rowconfigure(q + 1, weight=1, uniform='aa')
            etiqueta = tk.Label(frame, text=f"COD: {i.get_id()} | Nombre: {i.get_nombre()} | Ventas: {i.calcular_ventas()} | Precio: {i.get_precio()}", font=('Arial', 11), bg=FONDO)
            etiqueta.grid(row=p + 1, column=0, pady=2, sticky='nswe')
            p+=1
            q+=1

    def eleccion(self,lista:list[Producto],cat=None):
        self.limpiar_frame(self.subframe4)
        if cat is None:
            self.subframe4.grid(row=3,column=0,sticky='nswe')
            self.subframe4.rowconfigure(0, weight=1, uniform='aa')
            self.subframe4.columnconfigure(0, weight=1, uniform='bb')
            self.crear_etiquetas(self.subframe4, lista)

        else:
            self.subframe4.grid(row=1,sticky='nswe',column=0)
            self.subframe4.rowconfigure(0, weight=1, uniform='aa')
            self.subframe4.columnconfigure(0, weight=1, uniform='bb')
            self.crear_etiquetas(self.subframe4, lista)

    @staticmethod
    def limpiar_frame(frame):
        for widget in frame.winfo_children():
            widget.destroy()

# Gestionar empleados
class FieldFrameEmpleado(tk.Frame):
    def __init__(self, ventana, tienda_actual, fecha_actual):
        super().__init__(ventana, bg=FONDO)

        self.empleado_actual = None
        self.tienda_actual = tienda_actual
        self.fecha_actual = fecha_actual

        self.framemain = tk.Frame(ventana, bg=FONDO)
        self.framemain.grid(row=0, column=0, sticky='nswe')

        self.identidicar_empleado()

    #pantalla identificar empleado
    def identidicar_empleado(self):
        self.framemain.rowconfigure((0, 2), weight=1, uniform='a')
        self.framemain.rowconfigure(1, weight=4, uniform='a')
        self.framemain.columnconfigure(0, weight=1, uniform='b')

        self.subframe1 = tk.Frame(self.framemain, bg=FONDO, bd=0)
        self.subframe1.grid(row=0, column=0, sticky='s')
        self.subframe1.rowconfigure((0, 1), weight=1, uniform='aa')
        self.subframe1.columnconfigure((0, 1, 2), weight=1, uniform='bb')

        # Titulos
        tk.Label(self.subframe1, text='Empleados', font=('Arial', 11, 'bold'), bg=FONDO).grid(row=0, column=0, padx=15, sticky='e')

        # Comboboxes

        def identificar_categoria_nombres():
            return list(map(lambda empleado: empleado.get_nombre(), self.tienda_actual.get_empleados()))

        self.listado_empleados = []
        self.combobox_empleado = ttk.Combobox(self.subframe1)

        def crear_listado_empleados(frame):
            listado_default = tk.StringVar(value='Elige un empleado')
            listado_nombres = identificar_categoria_nombres()
            self.listado_empleados = self.tienda_actual.get_empleados()

            self.combobox_empleado.config(values=listado_nombres, textvariable=listado_default)
            self.combobox_empleado.grid(row=0, column=1, padx=15, pady=15)

        crear_listado_empleados(self.subframe1)

        # Insertar empleado seleccionado
        self.empleado_actual = None
        def insertar_empleado():
            self.empleado_actual = self.listado_empleados[self.combobox_empleado.current()]
            # Espacio del FieldFrame

            def identificar_meta_codigo():
                return list(map(lambda meta: meta.get_codigo(), self.empleado_actual.get_metas()))

            criterios = identificar_meta_codigo()

            def calcular_porcentaje(meta):
                porcentaje = meta.get_acumulado() / meta.get_valor_alcanzar() * 100
                return str(porcentaje)

            def identificar_meta_porcentaje():
                return list(map(calcular_porcentaje, self.empleado_actual.get_metas()))

            valores = identificar_meta_porcentaje()

            cri_habilitados = []
            for i in range(len(valores)):
                cri_habilitados.append(False)

            def al_aceptar_callback(resultado):
                self.pantalla_metas_alcanzadas()

            self.subframe2 = tk.Frame(self.framemain, bg=FONDO, bd=0)
            self.subframe2.grid(row=1, column=0)
            (FieldFrame(self.subframe2, 'Codigo', criterios, 'Porcentaje de progreso', valores, cri_habilitados, aceptar_callback=al_aceptar_callback)
                        .grid(row=0, column=0, padx=15, pady=15))


        # Boton para insertar empleado seleccionado
        self.boton_empleado = tk.Button(self.subframe1, text='Insertar', font=('Arial', 7, 'bold'), bg=RESALTO, bd=0, command=lambda: insertar_empleado())
        self.boton_empleado.grid(row=0, column=2, padx=15, pady=15, sticky='w')

        # metodo que limpia por completo el interior de el frame que reciba

    @staticmethod
    def limpiar_frame(frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def pantalla_metas_alcanzadas(self):
        self.limpiar_frame(self.framemain)

        self.framemain.rowconfigure((0, 2), weight=1, uniform='a')
        self.framemain.rowconfigure(1, weight=4, uniform='a')
        self.framemain.columnconfigure(0, weight=1, uniform='b')

        self.subframe = tk.Frame(self.framemain, bg=FONDO, bd=0)
        self.subframe.grid(row=0, column=0, sticky='s')
        self.subframe.rowconfigure(0, weight=1, uniform='aa')
        self.subframe.columnconfigure(0, weight=1, uniform='bb')

        gestionarMeta(self.empleado_actual, self.fecha_actual)

        # Titulos
        tk.Label(self.subframe, text='Códigos de metas alcanzadas', font=('Arial', 11, 'bold'), bg=FONDO).grid(row=0, column=0, padx=15, pady=15, sticky='e')

        # Comboboxes

        def identificar_metas_alcanzadas():
            return list(map(lambda meta: meta.get_codigo(), self.empleado_actual.get_metas_alcanzadas()))

        self.listado_metas_alcanzadas = []


        listado_default = tk.StringVar(value='Elige una meta alcanzada')
        listado_nombres = identificar_metas_alcanzadas()
        listado_metas_alcanzadas = self.empleado_actual.get_metas_alcanzadas()

        combobox_meta_alcanzada = ttk.Combobox(self.subframe, values=listado_nombres, textvariable=listado_default)
        combobox_meta_alcanzada.grid(row=0, column=1, padx=15, pady=15)

        if listado_metas_alcanzadas == []:
            messagebox.showinfo('No hay metas alcanzadas', 'No hay metas alcanzadas para este empleado')
            self.pantalla_metas_caducadas()
            return

        # Insertar meta seleccionada
        self.meta_alcanzada_actual = None
        def insertar_meta():
            self.meta_alcanzada_actual = self.listado_metas_alcanzadas[combobox_meta_alcanzada.current()]

            # Espacio del FieldFrame
            criterios = ['Codigo', 'Fecha', 'Valor a alcanzar', 'Valor bonificacion']
            valores = [str(self.meta_alcanzada_actual.get_codigo()), str(self.meta_alcanzada_actual.get_fecha()), str(self.meta_alcanzada_actual.get_valor_alcanzar()), str(self.meta_alcanzada_actual.get_valor_bonificacion())]
            cri_habilitados = [False, False, False, False]

            def al_aceptar_callback(resultado):
                self.pantalla_metas_caducadas()

            self.subframe2 = tk.Frame(self.framemain, bg=FONDO, bd=0)
            self.subframe2.grid(row=1, column=0)
            (FieldFrame(self.subframe2, 'Dato', criterios, 'Valor', valores, cri_habilitados, aceptar_callback=al_aceptar_callback)
                        .grid(row=0, column=0, padx=15, pady=15))

        #Boton para insertar meta seleccionada
        self.boton_meta_alcanzada = tk.Button(self.subframe, text='Mostrar', font=('Arial', 7, 'bold'), bg=RESALTO, bd=0, command=lambda: insertar_meta())
        self.boton_meta_alcanzada.grid(row=0, column=2, padx=15, pady=15, sticky='w')

    def pantalla_metas_caducadas(self):
        self.limpiar_frame(self.framemain)

        self.framemain.rowconfigure((0, 2), weight=1, uniform='a')
        self.framemain.rowconfigure(1, weight=4, uniform='a')
        self.framemain.columnconfigure(0, weight=1, uniform='b')

        self.subframe = tk.Frame(self.framemain, bg=FONDO, bd=0)
        self.subframe.grid(row=0, column=0, sticky='s')
        self.subframe.rowconfigure(0, weight=1, uniform='aa')
        self.subframe.columnconfigure(0, weight=1, uniform='bb')

        gestionarMeta(self.empleado_actual, self.fecha_actual)

        # Titulos
        tk.Label(self.subframe, text='Códigos de metas caducadas', font=('Arial', 11, 'bold'), bg=FONDO).grid(row=0, column=0, padx=15, pady=15, sticky='e')

        # Comboboxes

        def identificar_metas_caducadas():
            return list(map(lambda meta: meta.get_codigo(), self.empleado_actual.get_metas_caducadas()))

        self.listado_metas_caducadas = []
        self.combobox_meta_caducada = ttk.Combobox(self.subframe)

        def crear_listado_metas(frame):
            listado_default = tk.StringVar(value='Elige una meta caducada')
            listado_nombres = identificar_metas_caducadas()
            self.listado_metas_caducadas = self.empleado_actual.get_metas_caducadas()

            self.combobox_meta_caducada.config(values=listado_nombres, textvariable=listado_default)
            self.combobox_meta_caducada.grid(row=0, column=1, padx=15, pady=15)

            if self.listado_metas_caducadas == []:
                self.pantalla_rendimiento()
                messagebox.showinfo('No hay metas caducadas', 'No hay metas caducadas para este empleado')
                return

        crear_listado_metas(self.subframe)

        # Insertar meta seleccionada
        self.meta_caducada_actual = None
        def insertar_meta_caducada():
            self.meta_caducada_actual = self.listado_metas_caducadas[self.combobox_meta_caducada.current()]

            # Espacio del FieldFrame
            criterios = ['Codigo', 'Fecha', 'Valor a alcanzar', 'Valor bonificacion']
            valores = [str(self.meta_caducada_actual.get_codigo()), str(self.meta_caducada_actual.get_fecha()), str(self.meta_caducada_actual.get_valor_alcanzar()), str(self.meta_caducada_actual.get_valor_bonificacion())]
            cri_habilitados = [False, False, False, False]

            def al_aceptar_callback(resultado):
                criterios = ['Ingrese el año en el que desea ampliar la meta', 'Ingrese el mes en el que desea ampliar la meta', 'Ingrese el día en el que desea ampliar la meta']
                valores = None
                cri_habilitados = [True, True, True]

                def al_aceptar_callback(resultado):
                    messagebox.showinfo('Meta actualizada', 'La meta ha sido actualizada con exito')
                    ampliarMeta(self.empleado_actual, self.meta_caducada_actual, self.fecha_actual, int(resultado[0]), int(resultado[1]), int(resultado[2]))

                self.subframe2.destroy()
                self.subframe3 = tk.Frame(self.framemain, bg=FONDO, bd=0)
                self.subframe3.grid(row=1, column=0)
                (FieldFrame(self.subframe3, 'Dato', criterios, 'Valor', valores, cri_habilitados, aceptar_callback=al_aceptar_callback)
                            .grid(row=0, column=0, padx=15, pady=15))

            self.subframe2 = tk.Frame(self.framemain, bg=FONDO, bd=0)
            self.subframe2.grid(row=1, column=0)
            (FieldFrame(self.subframe2, 'Dato', criterios, 'Valor', valores, cri_habilitados, aceptar_callback=al_aceptar_callback)
                        .grid(row=0, column=0, padx=15, pady=15))

        #Boton para insertar meta seleccionada
        self.boton_meta_caducada = tk.Button(self.subframe, text='Mostrar', font=('Arial', 7, 'bold'), bg=RESALTO, bd=0, command=lambda: insertar_meta_caducada())
        self.boton_meta_caducada.grid(row=0, column=2, padx=15, pady=15, sticky='w')

        self.total_metas()

    def total_metas(self):
        subframe3 = tk.Frame(self.framemain, bg=FONDO, bd=0)
        subframe3.grid(row=2, column=0)
        subframe3.columnconfigure((0, 1), weight=1, uniform='a')
        subframe3.rowconfigure((0, 1), weight=1, uniform='b')

        tk.Button(subframe3, text='Continuar a rendimiento', font=('Arial', 7, 'bold'), bg=RESALTO, bd=0, command=self.pantalla_rendimiento).grid(row=0, column=0, padx=15, pady=15, sticky='e')


    def pantalla_rendimiento(self):
        self.limpiar_frame(self.framemain)

        self.framemain.rowconfigure((0, 2), weight=1, uniform='a')
        self.framemain.rowconfigure(1, weight=4, uniform='a')
        self.framemain.columnconfigure(0, weight=1, uniform='b')

        self.subframe = tk.Frame(self.framemain, bg=FONDO, bd=0)
        self.subframe.grid(row=0, column=0, sticky='s')
        self.subframe.rowconfigure(0, weight=1, uniform='aa')
        self.subframe.columnconfigure(0, weight=1, uniform='bb')

        #Titulos
        tk.Label(self.subframe, text='Rendimiento', font=('Arial', 11, 'bold'), bg=FONDO).grid(row=0, column=0, padx=15, pady=15, sticky='e')

        #Comboboxes
        redimientos = ['Semanal', 'Mensual', 'Anual']

        categoria_default = tk.StringVar(value='Elige un rendimiento')
        self.combobox_rendimiento = ttk.Combobox(self.subframe, values=redimientos, textvariable=categoria_default)
        self.combobox_rendimiento.grid(row=0, column=1, padx=15, pady=15)

        def insertar_rendimiento():
            self.rendimiento_actual = self.combobox_rendimiento.get()
            rendimiento = verRendimiento(self.empleado_actual, self.fecha_actual, self.combobox_rendimiento.get())

            # Espacio del FieldFrame
            criterios = ['Rendimiento']
            valores = [rendimiento]
            cri_habilitados = [False]

            def al_aceptar_callback(resultado):
                criterios = ['Rendimiento en período anterior', 'Rendimiento en período actual']
                rendimiento_pasado = compararRendimiento(self.empleado_actual, self.fecha_actual, self.rendimiento_actual)
                valores = [resultado[0], rendimiento_pasado]
                cri_habilitados = [False, False]

                def al_aceptar_callback(resultado):
                    self.pantalla_modificar_salario()

                self.subframe2.destroy()
                self.subframe3 = tk.Frame(self.framemain, bg=FONDO, bd=0)
                self.subframe3.grid(row=1, column=0)
                (FieldFrame(self.subframe3, 'Dato', criterios, 'Valor', valores, cri_habilitados, aceptar_callback=al_aceptar_callback)
                            .grid(row=0, column=0, padx=15, pady=15))

            self.subframe2 = tk.Frame(self.framemain, bg=FONDO, bd=0)
            self.subframe2.grid(row=1, column=0)
            (FieldFrame(self.subframe2, 'Dato', criterios, 'Valor', valores, cri_habilitados, aceptar_callback=al_aceptar_callback)
                        .grid(row=0, column=0, padx=15, pady=15))

        #Boton para insertar rendimiento
        self.boton_rendimiento = tk.Button(self.subframe, text='Insertar', font=('Arial', 7, 'bold'), bg=RESALTO, bd=0, command=lambda: insertar_rendimiento())
        self.boton_rendimiento.grid(row=0, column=2, padx=15, pady=15, sticky='w')

    def pantalla_modificar_salario(self):
        pass



# Subastar
class FieldFrameSubasta(tk.Frame):
    def __init__(self, ventana, tienda_actual, fecha_actual):
        super().__init__(ventana, bg=FONDO)
        super().__init__(ventana, bg=FONDO)

        self.carrito = []
        self.tienda_actual = tienda_actual
        self.fecha_actual = fecha_actual

        self.cliente_oferta = None

        self.framemain = tk.Frame(ventana, bg=FONDO)
        self.framemain.grid(row=0, column=0, sticky='nswe')
        self.framemain.rowconfigure(0, weight=1, uniform='a')
        self.framemain.columnconfigure(0, weight=1, uniform='a')

        self.seleccion_accion()

    # pantalla para seleccionar entre subastar, ofertar o terminar una subasta
    def seleccion_accion(self):
        self.reiniciar_frame()
        self.carrito = []

        self.comprobar_subastas_finalizadas()

        self.subframe_selec = tk.Frame(self.framemain, bg=FONDO)
        self.subframe_selec.grid(row=0, column=0, sticky='nswe')
        self.subframe_selec.columnconfigure(0, weight=1, uniform='a')
        self.subframe_selec.rowconfigure((0,1,2), weight=1, uniform='b')

        # subastar
        tk.Button(self.subframe_selec, text='Subastar', font=('Arial', 15, 'bold'), bg=RESALTO, bd=0, command=self.subastar).grid(row=0, column=0, padx=15, pady=15, sticky='s')

        # ofertar
        tk.Button(self.subframe_selec, text='Ofertar', font=('Arial', 15, 'bold'), bg=POWER, bd=0, command=self.ofertar).grid(row=1, column=0, padx=15, pady=15)

        # terminar subasta
        tk.Button(self.subframe_selec, text='Actualizar subasta descendente', font=('Arial', 15, 'bold'), bg=RESALTO, bd=0, command=self.actualizar_subasta).grid(row=2, column=0, padx=15, pady=15, sticky='n')

    def subastar(self):
        self.reiniciar_frame()

        def identificar_producto():
            self.frame_ident_producto = tk.Frame(self.framemain, bg=FONDO, bd=0)
            self.frame_ident_producto.rowconfigure((0, 2), weight=1, uniform='a')
            self.frame_ident_producto.rowconfigure(1, weight=4, uniform='a')
            self.frame_ident_producto.columnconfigure(0, weight=1, uniform='b')
            self.frame_ident_producto.grid(row=0, column=0, sticky='nswe')

            self.subframe1 = tk.Frame(self.frame_ident_producto, bg=FONDO, bd=0)
            self.subframe1.grid(row=0, column=0, sticky='s')
            self.subframe1.rowconfigure((0, 1), weight=1, uniform='aa')
            self.subframe1.columnconfigure((0, 1, 2), weight=1, uniform='bb')

            # Titulos
            tk.Label(self.subframe1, text='Categoria', font=('Arial', 11, 'bold'), bg=FONDO).grid(row=0, column=0,
                                                                                                  padx=15, sticky='e')
            tk.Label(self.subframe1, text='Producto', font=('Arial', 11, 'bold'), bg=FONDO).grid(row=1, column=0,
                                                                                                 padx=15, sticky='e')

            # Comboboxes
            categorias = ['Consola', 'Juego', 'Accesorio']

            categoria_default = tk.StringVar(value='Elige una categoria')
            self.combobox_categoria = ttk.Combobox(self.subframe1, values=categorias, textvariable=categoria_default)
            self.combobox_categoria.grid(row=0, column=1, padx=15, pady=15)

            # Crear combobox con listado de productos segun la categoria ingresada
            def identificar_categoria_nombres(cat: str):
                return list(map(lambda producto: producto.get_nombre(),
                                self.tienda_actual.get_productos_categoria_inventario(cat, 'usado')))

            self.listado_productos = []
            self.combobox_producto = ttk.Combobox(self.subframe1)

            def crear_listado(frame):
                listado_default = tk.StringVar(value='Elige un producto')
                listado_nombres = identificar_categoria_nombres(self.combobox_categoria.get())
                self.listado_productos = self.tienda_actual.get_productos_categoria_inventario(
                    self.combobox_categoria.get(), 'usado')

                self.combobox_producto.config(values=listado_nombres, textvariable=listado_default)
                self.combobox_producto.grid(row=1, column=1, padx=15, pady=15)

            # Boton para crear combobox listado
            self.boton_listado = tk.Button(self.subframe1, text='Buscar', font=('Arial', 9, 'bold'), bg=RESALTO, bd=0,
                                           command=lambda: crear_listado(self.subframe1))
            self.boton_listado.grid(row=0, column=2, padx=15, pady=15, sticky='w')

            # Insertar producto seleccionado
            self.producto_actual = None

            def insertar_producto():
                self.producto_actual = self.listado_productos[self.combobox_producto.current()]
                # Espacio del FieldFrame
                criterios = ['ID', 'Nombre', 'Valor inicial', 'Cantidad', 'Fecha de lanzamiento']
                valores = [str(self.producto_actual.get_id()), self.producto_actual.get_nombre(),
                           str(self.producto_actual.get_precio()), str(self.producto_actual.get_cantidad()),
                           str(self.producto_actual.get_fecha_lanzamiento())]
                cri_habilitados = [False, False, False, False, False]

                def al_aceptar_callback(resultado):
                    # buscar id del producto recibido en el inventario de la tienda actual
                    producto_en_field = self.tienda_actual.buscar_producto_id(int(resultado[0]), 'usado')

                    try:
                        # identificar producto en el carrito si ya esta
                        producto_en_carrito = None
                        for producto in self.carrito:
                            if producto.get_id() == producto_en_field.get_id():  # Si el producto es reconocido
                                producto_en_carrito = producto
                                # Si la cantidad es insuficiente
                                if producto_en_field.get_cantidad() - producto_en_carrito.get_cantidad() == 0:
                                    raise ExceptionCantidadInvalida()
                                break

                        if producto_en_carrito is not None:
                            producto_en_carrito.set_cantidad(producto_en_carrito.get_cantidad() + 1)
                        else:
                            # Agregar clon del producto al carrito
                            # la idea de usar un clon es para que el carrito maneje un atributo cantidad independiente
                            if producto_en_field.get_cantidad() == 0:  # Si la cantidad es insuficiente
                                raise ExceptionCantidadInvalida()
                            producto_clonado = copy.deepcopy(producto_en_field)
                            producto_clonado.set_cantidad(1)
                            self.carrito.append(producto_clonado)

                        # mostrar nuevo total del carrito en la entry correspondiente
                        self.entry_total_carrito.config(state='normal')
                        self.entry_total_carrito.delete(0, tk.END)
                        nuevo_total = str(sum(map(lambda prod: prod.get_cantidad(), self.carrito)))
                        self.entry_total_carrito.insert(0, nuevo_total)
                        self.entry_total_carrito.config(state='disabled')
                    except ExceptionCantidadInvalida:
                        pass

                self.subframe2 = tk.Frame(self.frame_ident_producto, bg=FONDO, bd=0)
                self.subframe2.grid(row=1, column=0)
                (FieldFrame(self.subframe2, 'Dato', criterios, 'Valor', valores, cri_habilitados,
                            aceptar_callback=al_aceptar_callback)
                 .grid(row=0, column=0, padx=15, pady=15))

            # Boton para insertar producto seleccionado
            self.boton_producto = tk.Button(self.subframe1, text='Insertar', font=('Arial', 9, 'bold'), bg=RESALTO,
                                            bd=0, command=lambda: insertar_producto())
            self.boton_producto.grid(row=1, column=2, padx=15, pady=15, sticky='w')

            self.total_carrito(self.frame_ident_producto)

        identificar_producto()

    # metodo que muestra en un frame pequeño la cantidad total actual de los productos en el carrito y se actualiza
    def total_carrito(self, frame_ident_producto):
        subframe3 = tk.Frame(frame_ident_producto, bg=FONDO, bd=0)
        subframe3.grid(row=2, column=0)
        subframe3.columnconfigure((0, 1), weight=1, uniform='a')
        subframe3.rowconfigure((0, 1), weight=1, uniform='b')

        tk.Label(subframe3, text='Cantidad total', font=('Arial', 11, 'bold'), bg=FONDO).grid(row=0, column=0, padx=15,
                                                                                              pady=15, sticky='e')
        self.entry_total_carrito = tk.Entry(subframe3, state='disabled')
        self.entry_total_carrito.grid(row=0, column=1, padx=15, pady=15, sticky='w')

        def limpiar_carrito():
            self.carrito = []
            self.entry_total_carrito.config(state='normal')
            self.entry_total_carrito.delete(0, tk.END)
            self.entry_total_carrito.insert(0, '0')
            self.entry_total_carrito.config(state='disabled')

        def commando_llamar_pantalla_tipo_sub():
            frame_ident_producto.destroy()
            self.pantalla_tipo_subasta()

        tk.Button(subframe3, text='Comprar', font=('Arial', 9, 'bold'), bg=RESALTO, bd=0,
                  command=commando_llamar_pantalla_tipo_sub).grid(row=1, column=0, padx=15, pady=15, sticky='e')
        tk.Button(subframe3, text='Limpiar carrito', font=('Arial', 9, 'bold'), bg=POWER, bd=0, command=limpiar_carrito).grid(row=1, column=1,padx=15, pady=15,sticky='w')

    def pantalla_tipo_subasta(self):
        self.reiniciar_frame()

        subframe_tipo_s = tk.Frame(self.framemain, bg=FONDO, bd=0)
        subframe_tipo_s.grid(row=0, column=0, rowspan=3, sticky='nswe')
        subframe_tipo_s.columnconfigure((0,1), weight=1, uniform='a')
        subframe_tipo_s.rowconfigure((0, 1, 2, 3, 4, 5), weight=1, uniform='b')
        # tipo de subasta - valor sin modificaciones de subasta - boton para obtener una oferta inicial recomendada - oferta inicial de subasta - plazo en dias - boton para confirmar

        # tipo de subasta
        tk.Label(subframe_tipo_s, text='Tipo de subasta', font=('Arial', 11, 'bold'), bg=FONDO).grid(row=0, column=0, padx=15, pady=15, sticky='e')
        combobox_tipo_subasta = ttk.Combobox(subframe_tipo_s, values=['Ascendente', 'Descendente', 'Anonima'], state='readonly')
        combobox_tipo_subasta.grid(row=0, column=1, padx=15, pady=15, sticky='w')

        # valor sin modificaciones
        tk.Label(subframe_tipo_s, text='Valor base', font=('Arial', 11, 'bold'), bg=FONDO).grid(row=1, column=0, padx=15, pady=15, sticky='e')
        entry_valor_base = tk.Entry(subframe_tipo_s)
        entry_valor_base.insert(0, str(sum(map(lambda prod: prod.get_precio() * prod.get_cantidad(), self.carrito))))
        entry_valor_base.config(state='disabled')
        entry_valor_base.grid(row=1, column=1, padx=15, pady=15, sticky='w')

        # fecha fin
        tk.Label(subframe_tipo_s, text='Fecha fin (DD/MM/AAAA)', font=('Arial', 11, 'bold'), bg=FONDO).grid(row=2, column=0, padx=15, pady=15, sticky='e')
        entry_fecha_fin = tk.Entry(subframe_tipo_s)
        entry_fecha_fin.grid(row=2, column=1, padx=15, pady=15, sticky='w')

        # oferta inicial recomendada
        label_oferta_inicial = tk.Label(subframe_tipo_s, text='Oferta inicial', font=('Arial', 11, 'bold'), bg=FONDO)
        entry_oferta_inicial = tk.Entry(subframe_tipo_s)

        # boton para obtener oferta inicial recomendada
        def al_obtener_oferta_inicial():
            try:
                # Obtener oferta inicial a partir del tipo de subasta
                from src.gestorAplicacion.informacionVenta.Subasta import Subasta
                criterio = combobox_tipo_subasta.get()
                if criterio == 'Ascendente':
                    entry_oferta_inicial.delete(0, tk.END)
                    entry_oferta_inicial.insert(0, str(Subasta.calcular_valoracion_ascendente(self.carrito, self.fecha_actual)))
                elif criterio == 'Descendente':
                    entry_oferta_inicial.delete(0, tk.END)
                    entry_oferta_inicial.insert(0, str(Subasta.calcular_valoracion_descendente(self.carrito, self.fecha_actual)))
                elif criterio == 'Anonima':
                    entry_oferta_inicial.delete(0, tk.END)
                    entry_oferta_inicial.insert(0, '0')
                    entry_oferta_inicial.config(state='disabled')
                else:
                    raise ExceptionCampoVacio([combobox_tipo_subasta], ['Tipo de subasta'])

                label_oferta_inicial.grid(row=4, column=0, padx=15, pady=15, sticky='e')
                entry_oferta_inicial.grid(row=4, column=1, padx=15, pady=15, sticky='w')

                # Boton para confirmar la creacion de la subasta
                def confimar_creacion_subasta():
                    # Convertir la fecha ingresada a un objeto Fecha
                    fecha_fin = entry_fecha_fin.get().split('/')
                    fecha_fin = Fecha(int(fecha_fin[0]), int(fecha_fin[1]), int(fecha_fin[2]))

                    try:
                        # Buscar si hay algun campo vacio
                        if entry_fecha_fin.get() == '' or entry_oferta_inicial.get() == '':
                            raise ExceptionCampoVacio([entry_fecha_fin, entry_oferta_inicial], ['Fecha', 'Oferta inicial'])

                        # Comprobar que la fecha sea posterior o igual a la ultima registrada
                        if fecha_fin.get_total_dias() < self.fecha_actual.get_total_dias():
                            raise ExceptionFechaInvalida(self.fecha_actual)

                    except ExceptionCampoVacio:
                        pass
                    except ExceptionFechaInvalida:
                        pass
                    else:
                        # Crear subasta
                        from src.gestorAplicacion.informacionVenta.Subasta import Subasta
                        Subasta(fecha_fin, self.carrito, int(entry_oferta_inicial.get()), self.tienda_actual, combobox_tipo_subasta.get())

                        # Reflejar en inventario que los productos han sido puestos en subasta

                        for prod_carro in self.carrito:
                            prod_invent = self.tienda_actual.buscar_producto_id(prod_carro.get_id(), 'usado')
                            prod_invent.set_cantidad(prod_invent.get_cantidad() - prod_carro.get_cantidad())

                        messagebox.showinfo('Subasta creada', 'Subasta creada con exito. Finaliza en ' + str(fecha_fin))
                        self.seleccion_accion()
                        pass

                tk.Button(subframe_tipo_s, text='Confirmar', font=('Arial', 9, 'bold'), bg=RESALTO, bd=0, command=confimar_creacion_subasta).grid(row=5, column=0, columnspan=2, padx=15, pady=15)
            except ExceptionCampoVacio:
                pass

        tk.Button(subframe_tipo_s, text='Obtener oferta inicial recomendada', font=('Arial', 11, 'bold'), bg=RESALTO, bd=0, command=al_obtener_oferta_inicial).grid(row=3, column=0, columnspan=2, padx=15, ipadx=30, pady=15)


    def ofertar(self):
        self.reiniciar_frame()

        #ASCENDENTE seleccion subasta - boton confirmacion - ingreso cliente - ultima oferta - cantidad a ofertar - boton para ofertar
        #DESCENDENTE seleccion subasta - boton confirmacion - ingreso cliente - oferta actual (disabled) - boton para ofertar
        #ANONIMA seleccion subasta - boton confirmacion - ingreso cliente - cantidad a ofertar - boton para ofertar
        subframe_oferta = tk.Frame(self.framemain, bg=FONDO, bd=0)
        subframe_oferta.grid(row=0, column=0, sticky='nswe')
        subframe_oferta.columnconfigure((0, 1), weight=1, uniform='a')
        subframe_oferta.rowconfigure((0, 1), weight=1, uniform='b')
        subframe_oferta.rowconfigure(2, weight=5, uniform='b')

        subframe_opciones_oferta = tk.Frame(subframe_oferta, bg=FONDO, bd=0)
        subframe_opciones_oferta.grid(row=2, column=0, columnspan=2, sticky='nswe')
        subframe_opciones_oferta.columnconfigure((0, 1), weight=1, uniform='a')
        subframe_opciones_oferta.rowconfigure((0,1,2,3), weight=1, uniform='b')

        # seleccion subasta
        tk.Label(subframe_oferta, text='Subasta', font=('Arial', 11, 'bold'), bg=FONDO).grid(row=0, column=0, padx=15, pady=15, sticky='e')
        values_subastas = []
        for subasta in self.tienda_actual.get_subastas():
            if subasta.get_estado() == 'Activa':
                values_subastas.append('ID: ' + str(subasta.get_id()) + ' | Tipo: ' + subasta.get_tipo() +  ' | Finaliza en: ' + subasta.get_fecha_fin().__str__())

        combobox_selec_subasta = ttk.Combobox(subframe_oferta, values=values_subastas, state='readonly')
        combobox_selec_subasta.grid(row=0, column=1, padx=15, pady=15, ipadx=60, sticky='w')

        # boton confirmacion
        def confirmar_subasta():
            self.limpiar_frame(subframe_opciones_oferta)
            # opciones subasta ascendente
            def subasta_ascendente(subasta):
                def aceptar_oferta_callback(resultado):
                    try:
                        # Chequear cedula del cliente
                        cliente_encontrado = Cliente.buscar_cliente(int(resultado[0]))
                        if cliente_encontrado is None:
                            raise ExceptionNoEncontrado('Cliente')

                        self.cliente_actual = cliente_encontrado

                        # Chequear cantidad a ofertar
                        oferta = int(resultado[2])
                        if oferta <= subasta.get_oferta_mayor():
                            raise ExceptionLogica('El monto a ofertar debe ser mayor a la ultima oferta')

                        # Revisar puntos de cliente
                        puntos_cliente = cliente_encontrado.get_puntos_fidelidad()
                        if puntos_cliente < oferta:
                            raise ExceptionLogica('El cliente no tiene suficientes puntos para ofertar')

                        # Registrar oferta
                        subasta.agregar_oferta(oferta, cliente_encontrado)
                        messagebox.showinfo('Oferta realizada', 'Oferta realizada con exito a nombre de ' + str(cliente_encontrado.get_nombre()))
                        self.seleccion_accion()

                    except ExceptionNoEncontrado:
                        pass
                    except ExceptionLogica:
                        pass

                criterios = ['Cedula cliente', 'Ultima oferta', 'Cantidad a ofertar']
                valores = [None, str(subasta.get_oferta_mayor()), None]
                ff_opciones_ascendente = FieldFrame(subframe_opciones_oferta, 'Dato', criterios, 'Valor', valores, [True, False, True], aceptar_callback=aceptar_oferta_callback, tipos_esperados=['int', 'int', 'int'])
                ff_opciones_ascendente.grid(row=0, column=0, rowspan=4, columnspan=2, padx=15, pady=15)

            # opciones subasta descendente
            def subasta_descendente(subasta):
                def aceptar_oferta_callback(resultado):
                    try:
                        # Chequear cedula del cliente
                        cliente_encontrado = Cliente.buscar_cliente(int(resultado[0]))
                        if cliente_encontrado is None:
                            raise ExceptionNoEncontrado('Cliente')

                        self.cliente_actual = cliente_encontrado

                        # Chequear saldo de puntos de cliente que va a tomar la oferta actual de la subasta
                        puntos_cliente = cliente_encontrado.get_puntos_fidelidad()
                        if puntos_cliente < subasta.get_oferta_mayor():
                            raise ExceptionLogica('El cliente no tiene suficientes puntos para tomar la oferta actual')

                        # Registrar oferta
                        subasta.registrar_oferta_ganadora(cliente_encontrado)
                        messagebox.showinfo('Subasta terminada', 'El cliente ' + str(cliente_encontrado.get_nombre()) + ' ha tomado la oferta actual de esta subasta')
                        self.seleccion_accion()

                    except ExceptionNoEncontrado:
                        pass
                    except ExceptionLogica:
                        pass

                criterios = ['Cedula cliente', 'Oferta actual']
                valores = [None, str(subasta.get_oferta_mayor())]
                ff_opciones_descendente = FieldFrame(subframe_opciones_oferta, 'Dato', criterios, 'Valor', valores, [True, False], aceptar_callback=aceptar_oferta_callback)
                ff_opciones_descendente.grid(row=0, column=0, rowspan=4, columnspan=2, padx=15, pady=15)

            # opciones subasta anonima
            def subasta_anonima(subasta):
                def aceptar_oferta_callback(resultado):
                    try:
                        # Chequear cedula del cliente
                        cliente_encontrado = Cliente.buscar_cliente(int(resultado[0]))
                        if cliente_encontrado is None:
                            raise ExceptionNoEncontrado('Cliente')

                        self.cliente_actual = cliente_encontrado

                        # Chequear cantidad a ofertar
                        oferta = int(resultado[2])

                        # Revisar puntos de cliente
                        puntos_cliente = cliente_encontrado.get_puntos_fidelidad()
                        if puntos_cliente < oferta:
                            raise ExceptionLogica('El cliente no tiene suficientes puntos para realizar esta oferta')

                        # Registrar oferta
                        subasta.agregar_oferta(oferta, cliente_encontrado)
                        messagebox.showinfo('Oferta realizada', 'Oferta realizada con exito a nombre de ' + str(cliente_encontrado.get_nombre()))
                        self.seleccion_accion()

                    except ExceptionNoEncontrado:
                        pass
                    except ExceptionLogica:
                        pass

                criterios = ['Cedula cliente', 'Cantidad a ofertar']
                ff_opciones_anonima = FieldFrame(subframe_opciones_oferta, 'Dato', criterios, 'Valor', None, None, aceptar_callback=aceptar_oferta_callback, tipos_esperados=['int', 'int'])
                ff_opciones_anonima.grid(row=0, column=0, rowspan=4, columnspan=2, padx=15, pady=15)

            try:
                # Buscar campo vacio
                if combobox_selec_subasta.get() == '':
                    raise ExceptionCampoVacio([combobox_selec_subasta], ['Subasta'])

                # Identificar tipo de subasta
                id_subasta_selec = combobox_selec_subasta.get().split(' | ')
                id_subasta_selec = int(id_subasta_selec[0].split(': ')[1])

                subasta_selec = None

                for subast in self.tienda_actual.get_subastas():
                    if subast.get_id() == id_subasta_selec:
                        subasta_selec = subast
                        break

                if subasta_selec.get_tipo() == 'Ascendente':
                    subasta_ascendente(subasta_selec)
                elif subasta_selec.get_tipo() == 'Descendente':
                    subasta_descendente(subasta_selec)
                elif subasta_selec.get_tipo() == 'Anonima':
                    subasta_anonima(subasta_selec)

            except ExceptionCampoVacio:
                pass


        tk.Button(subframe_oferta, text='Confirmar', font=('Arial', 9, 'bold'), bg=RESALTO, bd=0, command=confirmar_subasta).grid(row=1, column=0, columnspan=2, padx=15, pady=15)


    def actualizar_subasta(self):
        self.reiniciar_frame()

        subastas_desc = []
        for subasta in self.tienda_actual.get_subastas():
            if subasta.get_estado() == 'Activa' and subasta.get_tipo() == 'Descendente':
                subastas_desc.append(subasta)

        if len(subastas_desc) == 0:
            messagebox.showinfo('Subastas descendentes', 'No hay subastas descendentes activas')
            self.seleccion_accion()
            return

        subframe_actualizar = tk.Frame(self.framemain, bg=FONDO, bd=0)
        subframe_actualizar.grid(row=0, column=0, sticky='nswe')
        subframe_actualizar.columnconfigure((0, 1), weight=1, uniform='a')
        subframe_actualizar.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform='b')

        # seleccion subasta
        tk.Label(subframe_actualizar, text='Subasta', font=('Arial', 11, 'bold'), bg=FONDO).grid(row=0, column=0, padx=15, pady=15, sticky='e')
        values_subastas = []
        for subasta in subastas_desc:
            values_subastas.append('ID: ' + str(subasta.get_id()) + ' | Ultimo valor: ' + str(subasta.get_oferta_mayor()) + ' | Finaliza en: ' + subasta.get_fecha_fin().__str__())

        combobox_selec_subasta = ttk.Combobox(subframe_actualizar, values=values_subastas, state='readonly')
        combobox_selec_subasta.grid(row=0, column=1, padx=15, pady=15, ipadx=50, sticky='w')

        # boton confirmacion
        def selec_subasta():
            subasta_selec = None
            for subasta in subastas_desc:
                if combobox_selec_subasta.get().split(' | ')[0] == 'ID: ' + str(subasta.get_id()):
                    subasta_selec = subasta
                    break

            # entry para nuevo valor
            tk.Label(subframe_actualizar, text='Nuevo valor', font=('Arial', 11, 'bold'), bg=FONDO).grid(row=2, column=0, padx=15, pady=15, sticky='e')
            entry_nuevo_valor = tk.Entry(subframe_actualizar)
            entry_nuevo_valor.grid(row=2, column=1, padx=15, pady=15, sticky='w')

            # boton para confirmar
            def confirmar_actualizacion():
                try:
                    # Buscar campo vacio
                    if combobox_selec_subasta.get() == '' or entry_nuevo_valor.get() == '':
                        raise ExceptionCampoVacio([combobox_selec_subasta, entry_nuevo_valor], ['Subasta', 'Nuevo valor'])

                    # Comprobar reduccion de valor
                    if int(entry_nuevo_valor.get()) >= subasta_selec.get_oferta_mayor():
                        raise ExceptionLogica('El nuevo valor debe ser menor a la ultima oferta')

                    # Actualizar subasta
                    subasta_selec.set_oferta_mayor(int(entry_nuevo_valor.get()))
                    messagebox.showinfo('Subasta actualizada', 'Subasta actualizada con exito. Nuevo valor: ' + entry_nuevo_valor.get())

                    self.seleccion_accion()
                except ExceptionCampoVacio:
                    pass
                except ExceptionLogica:
                    pass

            tk.Button(subframe_actualizar, text='Confirmar decremento', font=('Arial', 9, 'bold'), bg=RESALTO, bd=0, command=confirmar_actualizacion).grid(row=3, column=0, columnspan=2, padx=15, pady=15)

        tk.Button(subframe_actualizar, text='Seleccionar', font=('Arial', 9, 'bold'), bg=RESALTO, bd=0, command=selec_subasta).grid(row=1, column=0, columnspan=1, padx=15, pady=15, sticky='e')
        tk.Button(subframe_actualizar, text='Volver', font=('Arial', 9, 'bold'), bg=POWER, bd=0, command=self.seleccion_accion).grid(row=1, column=1, columnspan=1, padx=15, pady=15, sticky='w')

    # metodo que comprueba que hayan subastas finalizadas, avisa mediante messageboxes y actualiza su estado segun corresponda
    def comprobar_subastas_finalizadas(self):
        for subasta in self.tienda_actual.get_subastas():
            if subasta.get_estado() == 'Activa' and int(subasta.get_fecha_fin().get_total_dias()) < int(self.fecha_actual.get_total_dias()):
                # Si no hubo ofertas mirando la lista de ofertas
                if subasta.get_ofertas() == []:
                    messagebox.showinfo('Subasta extendida', subasta.extender_subasta(self.fecha_actual))
                # Si hubo ofertas
                else:
                    if subasta.get_tipo() == 'Ascendente':
                        ganador = subasta.finalizar_subasta()
                        messagebox.showinfo('Subasta finalizada', 'La subasta ' + str(subasta.get_id()) + ' ha finalizado.\nEl ganador es ' + ganador.get_nombre() + ' con cedula ' + str(ganador.get_cedula()) + ' por una oferta de ' + str(subasta.get_oferta_mayor()))
                    elif subasta.get_tipo() == 'Anonima':
                        ganador = subasta.finalizar_subasta_anonima()
                        messagebox.showinfo('Subasta finalizada', 'La subasta ' + str(subasta.get_id()) + ' ha finalizado.\nEl ganador es ' + ganador.get_nombre() + ' con cedula ' + str(ganador.get_cedula()) + ' por una oferta de ' + str(subasta.get_oferta_mayor()))






    # metodo que limpia por completo el interior de el frame que reciba
    @staticmethod
    def limpiar_frame(frame):
        for widget in frame.winfo_children():
            widget.destroy()

    # metodo que limpiar el frame de la funcionalidad y reestablece sus filas y columnas para que tenga solo una celda
    def reiniciar_frame(self):
        self.limpiar_frame(self.framemain)
        self.framemain.rowconfigure(0, weight=1, uniform='a')
        self.framemain.columnconfigure(0, weight=1, uniform='a')

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
        super().__init__('Ingrese una fecha posterior a ' + str(fecha))

class ExceptionCantidadInvalida(ExceptionLogica):
    def __init__(self):
        super().__init__('Este local no posee suficientes unidades de este producto')

class ExceptionNoEncontrado(ExceptionLogica):
    def __init__(self, tipo):
        super().__init__(f'No se encontro ninguna instancia del tipo {tipo} con este valor')

# Grupo 2
class ExceptionCampos(ErrorAplicacion):
    def __init__(self, mensaje):
        super().__init__('Error en los campos:\n' + mensaje)

class ExceptionTipoInvalido(ExceptionCampos):
    def __init__(self, entries_val, criterios, tipos_esperados):
        super().__init__(self.identificar_tipo_invalido(entries_val, criterios, tipos_esperados))

    def identificar_tipo_invalido(self, entries_val, criterios, tipos_esperados):
        self.campos_invalidos = []
        self.mensaje = ''

        for entry in entries_val:
            if entry == '':  # Revisar si el campo esta vacio
                raise ExceptionCampoVacio(entries_val, criterios)

            elif tipos_esperados is not None:
                if tipos_esperados[entries_val.index(entry)] == 'str':  # Si el tipo esperado es str
                    if entry.get().isdigit():
                        self.campos_invalidos.append(criterios[entries_val.index(entry)])

                elif tipos_esperados[entries_val.index(entry)] == 'int':  # Si el tipo esperado es int
                    if not entry.get().isdigit():
                        self.campos_invalidos.append(criterios[entries_val.index(entry)])

        return('Campos con tipo invalidos: ' + ', '.join(self.campos_invalidos))

class ExceptionFormatoFecha(ExceptionCampos):
    def __init__(self):
        super().__init__('Error en el formato de la fecha. Recuerde que debe ser DD/MM/AAAA')

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