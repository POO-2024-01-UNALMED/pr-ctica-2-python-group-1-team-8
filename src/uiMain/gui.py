import tkinter as tk
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'libs', 'Pillow'))

from PIL import Image, ImageTk

class GUI:
    # Atributos de clase
    # estos atributos son con el fin de permitir la funcion de metodos en la clase
    num_imagen_integrante = 0
    saludo = 'Hola, bienvenido a Villajuegos. Aqui podras encontrar los mejores juegos para ti y tus amigos.'
    descripcion = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cr'


    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Villajuegos")

        self.root.geometry("700x700")
        self.root.configure(bg="white")

        # Configuracion de las filas y columnas
        # Columnas
        self.root.columnconfigure((0,1), weight=1, uniform='a')
        # Filas
        self.root.rowconfigure(1, weight=10, uniform='b')

        # FRAME 1
        self.frame = tk.Frame(self.root, bg='white', bd=3, relief='solid')
        self.frame.grid(row=1, column=0, sticky='nsew', padx=15, pady=20)
        # Columnas y filas de FRAME 1
        self.frame.columnconfigure(0, weight=1, uniform='aa')
        self.frame.rowconfigure(0, weight=4, uniform='bb')
        self.frame.rowconfigure(1, weight=7, uniform='bb')
        # ~~~~~~~
        # Elementos
        # Saludo
        self.texto_saludo = tk.Text(self.frame, fg='black', font=('Arial', 15, 'bold'), wrap='word', cursor='hand2')
        self.texto_saludo.insert(tk.END, self.__class__.saludo)
        self.texto_saludo.grid(row=0, column=0, sticky='nsew', padx=8, pady=8)
        self.texto_saludo.config(state=tk.DISABLED)

        # Imagenes del local

        self.canvas = tk.Canvas(self.frame, bg='white')
        self.canvas.grid(row=1, column=0, sticky='nsew', padx=8, pady=8)
        self.imagen = ImageTk.PhotoImage(Image.open('imagenes/tienda/tienda1.png'))
        self.imagen_id = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.imagen)

        # Botones TODO BORRAR
        #self.boton2 = tk.Button(self.frame, text="Boton 2", bg='black', fg='white', font=('Arial', 15, 'bold')).grid(row=1, column=0, sticky='nsew', padx=8, pady=8)

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # FRAME 2
        self.frame2 = tk.Frame(self.root, bg='white', bd=3, relief='solid')
        self.frame2.grid(row=1, column=1, sticky='nsew', padx=15, pady=20)
        # Columnas y filas de FRAME 1
        self.frame2.columnconfigure(0, weight=1, uniform='aa')
        self.frame2.rowconfigure(0, weight=4, uniform='bb')
        self.frame2.rowconfigure(1, weight=7, uniform='bb')
        # ~~~~~~
        # Elementos
        # Subframe de imagenes
        self.subframe1 = tk.Frame(self.frame2, bg='white')
        self.subframe1.grid(row=1, column=0, sticky='nsew', padx=8, pady=8)
        self.subframe1.columnconfigure((0,1), weight=1, uniform='aaa')
        self.subframe1.rowconfigure((0,1), weight=1, uniform='bbb')

        # Mostrar integrantes y hoja de vida y cambiar con click en esta
        self.cambiar_integrante() # Llamada inicial a la funcion

        # Menubar
        menubar = tk.Menu(self.root)
        iniciomenu = tk.Menu(menubar, tearoff=0)
        iniciomenu.add_command(label="Descripcion", command=lambda: self.alternar_saludo())
        iniciomenu.add_separator()
        iniciomenu.add_command(label="Salir", command=self.root.destroy)
        menubar.add_cascade(label="Inicio", menu=iniciomenu)

        self.root.config(menu=menubar)

        self.root.bind("<Configure>", self.resizer)
        self.root.mainloop()

    def resizer(self, event):
        #global imagen_og, imagen_resizeada, imagen_nueva
        # CANVAS 1 (izquierda)
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        self.imagen_og = Image.open('imagenes/tienda/tienda1.png')
        self.imagen_resizeada = self.imagen_og.resize((width, height))
        self.imagen_nueva = ImageTk.PhotoImage(self.imagen_resizeada)

        self.canvas.itemconfig(self.imagen_id, image=self.imagen_nueva)

        # CANVAS 2 (derecha)

        width2 = self.subframe1.winfo_width()
        height2 = self.subframe1.winfo_height()


    def cambiar_integrante(self):
        # Imagenes
        paths1 = ['imagenes/integrantes/villa/images1.png', 'imagenes/integrantes/villa/images2.png',
                  'imagenes/integrantes/villa/images3.png', 'imagenes/integrantes/villa/images4.png']
        paths2 = ['imagenes/integrantes/seba/images1.png', 'imagenes/integrantes/seba/images2.png',
                  'imagenes/integrantes/seba/images3.png', 'imagenes/integrantes/seba/images4.png']
        paths3 = ['imagenes/integrantes/andres/images1.png', 'imagenes/integrantes/andres/images2.png',
                  'imagenes/integrantes/andres/images3.png', 'imagenes/integrantes/andres/images4.png']

        paths = [paths1, paths2, paths3]

        p = self.__class__.num_imagen_integrante

        self.imagen1 = tk.PhotoImage(file=paths[p][0])
        tk.Label(self.subframe1, image=self.imagen1).grid(row=0, column=0, sticky='nwse',
                                                          padx=2, pady=2)
        self.image2 = tk.PhotoImage(file=paths[p][1])
        tk.Label(self.subframe1, image=self.image2).grid(row=0, column=1, sticky='nwse',
                                                          padx=2, pady=2)
        self.image3 = tk.PhotoImage(file=paths[p][2])
        tk.Label(self.subframe1, image=self.image3).grid(row=1, column=0, sticky='nwse',
                                                          padx=2, pady=2)
        self.image4 = tk.PhotoImage(file=paths[p][3])
        tk.Label(self.subframe1, image=self.image4).grid(row=1, column=1, sticky='nwse',
                                                          padx=2, pady=2)

        self.__class__.num_imagen_integrante += 1
        if self.__class__.num_imagen_integrante > 2:
            self.__class__.num_imagen_integrante = 0

        # Hoja de vida TODO: Quitar texto placeholder
        hv_villa = """villavillavillavillavillavillavillavillavillavillavilla"""
        hv_seba = """sebasebasebasebasebasebasebasebasebasebasebasebaseba"""
        hv_andres = """aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"""
        hojas_vida = [hv_villa, hv_seba, hv_andres]

        self.text = tk.Text(self.frame2, fg='black', font=('Arial', 9, 'bold'), wrap='word', cursor='hand2')
        self.text.grid(row=0, column=0, sticky='nsew', padx=8, pady=8)
        self.text.insert(tk.END, hojas_vida[p])
        self.text.bind("<Button-1>", lambda event: self.cambiar_integrante())


    def alternar_saludo(self):
        self.texto_saludo.config(state=tk.NORMAL)
        if self.texto_saludo.get(1.0, tk.END).strip() == self.__class__.saludo:
            self.texto_saludo.delete(1.0, tk.END)
            self.texto_saludo.insert(tk.END, self.__class__.descripcion)
        else:
            self.texto_saludo.delete(1.0, tk.END)
            self.texto_saludo.insert(tk.END, self.__class__.saludo)
        self.texto_saludo.config(state=tk.DISABLED)