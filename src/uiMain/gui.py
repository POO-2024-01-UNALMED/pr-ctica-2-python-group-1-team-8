import tkinter as tk

class GUI:
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
        # Botones TODO BORRAR
        self.boton3 = tk.Button(self.frame2, text="Boton 3", bg='black', fg='white', font=('Arial', 15, 'bold')).grid(row=0, column=0, sticky='nsew', padx=8, pady=8)

        # Subframe de imagenes
        self.subframe1 = tk.Frame(self.frame2, bg='white')
        self.subframe1.grid(row=1, column=0, sticky='nsew', padx=8, pady=8)
        self.subframe1.columnconfigure((0,1), weight=1, uniform='aaa')
        self.subframe1.rowconfigure((0,1), weight=1, uniform='bbb')

        self.imagen1 = tk.PhotoImage(file='images/images1.png')
        self.imagen_label1 = tk.Label(self.subframe1, image=self.imagen1).grid(row=0, column=0, sticky='nwse', padx=2, pady=2)
        self.imagen2 = tk.PhotoImage(file='images/images2.png')
        self.imagen2 = self.imagen2.subsample(6)
        self.imagen_label2 = tk.Label(self.subframe1, image=self.imagen2).grid(row=0, column=1, sticky='nwse', padx=2, pady=2)
        self.imagen3 = tk.PhotoImage(file='images/images3.png')
        self.imagen3 = self.imagen3.subsample(6)
        self.imagen_label3 = tk.Label(self.subframe1, image=self.imagen3).grid(row=1, column=0, sticky='nwse', padx=2, pady=2)
        self.imagen4 = tk.PhotoImage(file='images/images4.png')
        self.imagen4 = self.imagen4.subsample(9)
        self.imagen_label4 = tk.Label(self.subframe1, image=self.imagen4).grid(row=1, column=1, sticky='nwse', padx=2, pady=2)





        self.root.mainloop()