import tkinter as tk

class GUI:
    # Atributos de clase
    # estos atributos son con el fin de permitir la funcion de metodos en la clase
    num_imagen_integrante = 0


    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Villajuegos")

        self.root.geometry("700x700")
        self.root.configure(bg="white")

        # Configuracion de las filas y columnas
        # Columnas
        self.root.columnconfigure((0,1), weight=1, uniform='a')
        # Filas
        self.root.rowconfigure(0, weight=1, uniform='b')
        self.root.rowconfigure(1, weight=10, uniform='b')

        # ROOT
        self.label = tk.Label(self.root, text="hola", bg='white', fg='black', font=('Arial', 15, 'bold'))
        self.label.grid(row=0, column=0)

        # FRAME 1
        self.frame = tk.Frame(self.root, bg='white', bd=3, relief='solid')
        self.frame.grid(row=1, column=0, sticky='nsew', padx=15, pady=20)
        # Columnas y filas de FRAME 1
        self.frame.columnconfigure(0, weight=1, uniform='aa')
        self.frame.rowconfigure(0, weight=4, uniform='bb')
        self.frame.rowconfigure(1, weight=7, uniform='bb')
        # ~~~~~~~
        # Elementos

        # Botones TODO BORRAR
        self.boton = tk.Button(self.frame, text="Boton 1", bg='black', fg='white', font=('Arial', 15, 'bold')).grid(row=0, column=0, sticky='nsew', padx=8, pady=8)
        self.boton2 = tk.Button(self.frame, text="Boton 2", bg='black', fg='white', font=('Arial', 15, 'bold')).grid(row=1, column=0, sticky='nsew', padx=8, pady=8)

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
        def cambiar_integrante():
            # Imagenes
            paths1 = ['imagenes/integrantes/villa/images1.png', 'imagenes/integrantes/villa/images2.png', 'imagenes/integrantes/villa/images3.png', 'imagenes/integrantes/villa/images4.png']
            paths2 = ['imagenes/integrantes/seba/images1.png', 'imagenes/integrantes/seba/images2.png', 'imagenes/integrantes/seba/images3.png', 'imagenes/integrantes/seba/images4.png']
            paths3 = ['imagenes/integrantes/andres/images1.png', 'imagenes/integrantes/andres/images2.png', 'imagenes/integrantes/andres/images3.png', 'imagenes/integrantes/andres/images4.png']

            paths = [paths1, paths2, paths3]

            p = self.__class__.num_imagen_integrante

            self.imagen1 = tk.PhotoImage(file=paths[p][0])
            self.imagen1 = self.imagen1.subsample(4)
            tk.Label(self.subframe1, image=self.imagen1).grid(row=0, column=0, sticky='nwse',
                                                              padx=2, pady=2)
            self.imagen2 = tk.PhotoImage(file=paths[p][1])
            self.imagen2 = self.imagen2.subsample(4)
            tk.Label(self.subframe1, image=self.imagen2).grid(row=0, column=1, sticky='nwse',
                                                              padx=2, pady=2)
            self.imagen3 = tk.PhotoImage(file=paths[p][2])
            self.imagen3 = self.imagen3.subsample(4)
            tk.Label(self.subframe1, image=self.imagen3).grid(row=1, column=0, sticky='nwse',
                                                              padx=2, pady=2)
            self.imagen4 = tk.PhotoImage(file=paths[p][3])
            self.imagen4 = self.imagen4.subsample(4)
            tk.Label(self.subframe1, image=self.imagen4).grid(row=1, column=1, sticky='nwse',
                                                              padx=2, pady=2)

            self.__class__.num_imagen_integrante += 1
            if self.__class__.num_imagen_integrante > 2:
                self.__class__.num_imagen_integrante = 0

            # Hoja de vida TODO: Quitar texto placeholder
            hv_villa = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras aliquet, ex ac malesuada fringilla, tortor ante facilisis felis, a feugiat velit velit ac leo. Fusce in faucibus tellus. Proin quis enim eu diam faucibus tincidunt. Nulla efficitur maximus sapien. Curabitur faucibus eget arcu nec dictum. Mauris nec lacus auctor nunc ultrices egestas id at erat. Sed magna libero, accumsan eu ante ut, sagittis fermentum mauris. Nam tellus nibh, scelerisque quis posuere eget, condimentum sit amet sapien. Curabitur non luctus elit, sit amet semper magna. Pellentesque vel diam urna. Proin congue id lectus in venenatis. Sed eget vehicula urna, nec vehicula odio. Aliquam quis molestie purus. Ut non orci vitae ipsum facilisis congue ultricies non metus. """
            hv_seba = """𓀔𓀇𓀅𓀋𓀡𓀡𓀕𓀠𓀧𓀨𓀣𓀷𓀷𓀿𓀿𓁀𓁶𓁰𓁴𓁿𓂀𓁾𓁵𓁯𓂞𓂤𓂗𓃃𓂾𓂺𓂹𓃞𓃙𓃖𓃓𓃕𓃓𓃜𓃘𓃙𓃟𓃛𓃞𓂺𓃂𓂿𓂺𓃃𓃂𓂛𓂏𓅱𓅥𓅩𓅦𓅹𓅸𓅳𓅩𓅪𓄭𓄫𓄮𓄬𓄗𓄑𓄌𓃦𓃧𓃨𓃤𓃟𓃓𓃅𓃁𓂽𓃂𓂊𓁾𓂀𓁽𓁼𓁠𓁛𓁟𓁦𓁜𓁭𓁡𓀔𓀇𓀅𓀋𓀡𓀡𓀕𓀠𓀧𓀨𓀣𓀷𓀷𓀿𓀿𓁀𓁶𓁰𓁴𓁿𓂀𓁾𓁵𓁯𓂞𓂤𓂗𓃃𓂾𓂺𓂹𓃞𓃙𓃖𓃓𓃕𓃓𓃜𓃘𓃙𓃟𓃛𓃞𓂺𓃂𓂿𓂺𓃃𓃂𓂛𓂏𓅱𓅥𓅩𓅦𓅹𓅸𓅳𓅩𓅪𓄭𓄫𓄮𓄬𓄗𓄑𓄌𓃦𓃧𓃨𓃤𓃟𓃓𓃅𓃁𓂽𓃂𓂊𓁾𓂀𓁽𓁼𓁠𓁛𓁟𓁦𓁜𓁭𓁡𓀔𓀇𓀅𓀋𓀡𓀡𓀕𓀠𓀧𓀨𓀣𓀷𓀷𓀿𓀿𓁀𓁶𓁰𓁴𓁿𓂀𓁾𓁵𓁯𓂞𓂤𓂗𓃃𓂾𓂺𓂹𓃞𓃙𓃖𓃓𓃕𓃓𓃜𓃘𓃙𓃟𓃛𓃞𓂺𓃂𓂿𓂺𓃃𓃂𓂛𓂏𓅱𓅥"""
            hv_andres = """Creo en Dios Padre, Todopoderoso, Creador del cielo y de la tierra. Y en Jesucristo, su único Hijo, Nuestro Señor, que fue concebido por obra y gracia del Espíritu Santo, nació de Santa María Virgen, padeció bajo el poder de Poncio Pilato, fue crucificado, muerto y sepultado, descendió a los infiernos, al tercer día resucitó entre los muertos, subió a los cielos y está sentado a la derecha de Dios Padre, Todopoderoso."""
            hojas_vida = [hv_villa, hv_seba, hv_andres]

            # self.boton3 = (tk.Button(self.frame2, bg='black', command=cambiar_integrante, fg='white',font=('Arial', 15, 'bold'))
            #                 .grid(row=0, column=0, sticky='nsew', padx=8, pady=8))
            self.text = tk.Text(self.frame2, fg='black', font=('Arial', 9, 'bold'), wrap='word', cursor='hand2')
            self.text.grid(row=0, column=0, sticky='nsew', padx=8, pady=8)
            self.text.insert(tk.END, hojas_vida[p])
            self.text.bind("<Button-1>", lambda event: cambiar_integrante())
        cambiar_integrante() # Llamada inicial a la funcion

        self.root.mainloop()