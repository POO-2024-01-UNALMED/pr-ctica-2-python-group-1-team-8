import tkinter as tk

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Villajuegos")

        self.root.geometry("550x600")
        self.root.configure(bg="white")

        # Configuracion de las filas y columnas
        # Columnas
        self.root.columnconfigure((0,1), weight=1, uniform='a')
        # Filas
        self.root.rowconfigure(0, weight=1, uniform='b')
        self.root.rowconfigure(1, weight=10, uniform='b')

        self.label = tk.Label(self.root, text="hola", bg='white', fg='black', font=('Arial', 15, 'bold'))
        self.label.grid(row=0, column=0)

        # FRAME 1
        self.frame = tk.Frame(self.root, bg='white', bd=3, relief='solid')
        self.frame.grid(row=1, column=0, sticky='nsew', padx=15, pady=20)

        # Columnas y filas de FRAME 1
        self.frame.columnconfigure(0, weight=1, uniform='aa')
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=3)

        # Boton 1
        self.boton = tk.Button(self.frame, text="Boton 1", bg='black', fg='white', font=('Arial', 15, 'bold')).grid(row=0, column=0, sticky='nsew', padx=8, pady=8)
        self.boton2 = tk.Button(self.frame, text="Boton 2", bg='black', fg='white', font=('Arial', 15, 'bold')).grid(row=1, column=0, sticky='nsew', padx=8, pady=8)

        # FRAME 2
        self.frame2 = tk.Frame(self.root, bg='white', bd=3, relief='solid')
        self.frame2.grid(row=1, column=1, sticky='nsew', padx=15, pady=20)
        # Columnas y filas de FRAME 1
        self.frame2.columnconfigure(0, weight=1, uniform='aa')
        self.frame2.rowconfigure(0, weight=1)
        self.frame2.rowconfigure(1, weight=3)
        # Botones
        self.boton3 = tk.Button(self.frame2, text="Boton 3", bg='black', fg='white', font=('Arial', 15, 'bold')).grid(row=0, column=0, sticky='nsew', padx=8, pady=8)
        self.boton4 = tk.Button(self.frame2, text="Boton 4", bg='black', fg='white', font=('Arial', 15, 'bold')).grid(row=1, column=0, sticky='nsew', padx=8, pady=8)





        self.root.mainloop()