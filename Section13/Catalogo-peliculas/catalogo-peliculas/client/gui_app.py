import tkinter as tk

def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width = 300, height = 300)

    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Inicio' ,menu = menu_inicio)

    menu_inicio.add_command(label='Crear Registro en DB')
    menu_inicio.add_command(label='Eliminar Registro en DB')
    menu_inicio.add_command(label='Salir', command=root.destroy)

    barra_menu.add_cascade(label='Consultas')
    barra_menu.add_cascade(label='Configuracion')
    barra_menu.add_cascade(label='Ayuda')
class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width= 1920, height= 1080)
        self.root = root
        self.pack()
        self.config(bg = 'green')

        self.campos_pelicula()
        self.desabilitar_campos()

    def campos_pelicula(self):
        self.label_nombre = tk.Label(self, text='Nombre: ')
        self.label_nombre.config(font = ('Arial', 12, 'bold'))
        self.label_nombre.grid(row=0, column=0, padx = 10, pady = 10)

        self.label_duracion = tk.Label(self, text='Duracion: ')
        self.label_duracion.config(font = ('Arial', 12, 'bold'))
        self.label_duracion.grid(row=1, column=0, padx = 10, pady = 10)

        self.label_genero = tk.Label(self, text='Genero: ')
        self.label_genero.config(font = ('Arial', 12, 'bold'))
        self.label_genero.grid(row=2, column=0, padx = 10, pady = 10)

        #entry
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.config(width=50, font = ('Arial', 12))
        self.entry_nombre.grid(row=0, column=1, padx = 10, pady = 10, columnspan=2)
        
        self.entry_duracion = tk.Entry(self)
        self.entry_duracion.config(width=50, font = ('Arial', 12))
        self.entry_duracion.grid(row=1, column=1, padx = 10, pady = 10, columnspan=2)
        
        self.entry_genero = tk.Entry(self)
        self.entry_genero.config(width=50, font = ('Arial', 12))
        self.entry_genero.grid(row=2, column=1, padx = 10, pady = 10, columnspan=2)

        #botones
        self.boton_nuevo = tk.Button(self, text='Nuevo', command = self.habilitar_campos)
        self.boton_nuevo.config(font = ('Arial', 12, 'bold'), width = 20, fg = '#DAD5D6', bg = '#158645', cursor = 'hand2', activebackground = '#35bd6f')
        self.boton_nuevo.grid(row=4, column=0, padx = 10, pady = 10)
        
        self.boton_guardar = tk.Button(self, text='Guardar')
        self.boton_guardar.config(font = ('Arial', 12, 'bold'), width = 20, fg = '#DAD5D6', bg = '#1658A2', cursor = 'hand2', activebackground = '#3586df')
        self.boton_guardar.grid(row=4, column=1, padx = 10, pady = 10)

        self.buton_cancelar = tk.Button(self, text='Cancelar', command = self.desabilitar_campos)
        self.buton_cancelar.config(font = ('Arial', 12, 'bold'), width = 20, fg = '#DAD5D6', bg = '#bd152e', cursor = 'hand2', activebackground = '#e15370')
        self.buton_cancelar.grid(row=4, column=2, padx = 10, pady = 10)

    def habilitar_campos(self):
        self.entry_nombre.config(state = 'normal')
        self.entry_duracion.config(state = 'normal')
        self.entry_genero.config(state = 'normal')

        self.boton_guardar.config(state = 'normal')
        self.buton_cancelar.config(state = 'normal')

    def desabilitar_campos(self):
        self.entry_nombre.config(state = 'disabled')
        self.entry_duracion.config(state = 'disabled')
        self.entry_genero.config(state = 'disabled')

        self.boton_guardar.config(state = 'disabled')
        self.buton_cancelar.config(state = 'disabled')