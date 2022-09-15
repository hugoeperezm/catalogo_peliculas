# Este archivo será la interfaz de usuario la aplicacion
# 1. Se importa el modulo tkinter
# 2. Se define la clase Frame
# 3. Se crear la barra de mnú con las diferentes menus y opciones

import tkinter as tk


def barra_menu(root):
    # La funcion barra_menu diseña y crear toda la barra de menús recibiendo el parametro root

    # crea la barra de menues y le da una configuracion
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu, width=300, height=300)

    # Define el primer menú y quita el lineado que le aparece, con tearoff=0
    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Archivo', menu=menu_inicio)

    # Se adiciona cada comando o cada opcion del menu Archivo
    menu_inicio.add_command(label='Crear registro en DB')
    menu_inicio.add_command(label='Eliminar registro en DB')
    menu_inicio.add_command(label='Salir', command=root.destroy)

    barra_menu.add_cascade(label='Consultas')
    barra_menu.add_cascade(label='Herramientas')
    barra_menu.add_cascade(label='Ayuda')


class Frame(tk.Frame):
    # Esta clase espera un frame none y se define el self
    # y el root que recibe desde el modulo principal
    def __init__(self, root = None):
        # Heredar el constructor de la clase padre y recibe la raiz y la configuracion
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()
        # self.config(bg='green')
        # self.label_nombre = None
        self.campos_pelicula()

    def campos_pelicula(self):
        # Labels de cada campo donde muestra los campos
        self.label_nombre = tk.Label(self, text='Nombre: ')
        self.label_nombre.config(font=('Arial', 12, 'bold'))
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)

        self.label_duración = tk.Label(self, text='Duración: ')
        self.label_duración.config(font=('Arial', 12, 'bold'))
        self.label_duración.grid(row=1, column=0, padx=10, pady=10)

        self.label_genero = tk.Label(self, text='Género: ')
        self.label_genero.config(font=('Arial', 12, 'bold'))
        self.label_genero.grid(row=2, column=0, padx=10, pady=10)

        # Entrys de cada campo
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.config(width=50, state='disable', font=('Arial', 12))
        # Los entrys están ocupando una sola columna en el grid. Para que ocupe dos columnas,
        # se agrega la propiedad: columnspan=2
        # self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10, columnspan=2)


        self.entry_duracion = tk.Entry(self)
        self.entry_duracion.config(width=50, state='disable', font=('Arial', 12))
        self.entry_duracion.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

        self.entry_genero = tk.Entry(self)
        self.entry_genero.config(width=50, state='disable', font=('Arial', 12))
        self.entry_genero.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

        # Botones de Nuevo registro, ...
        # en la pagina https://htmlcolorcodes.com/es se puede obtener los codigos de los colores
        self.boton_nuevo = tk.Button(self, text="Nuevo")
        self.boton_nuevo.config(width=20, font=('Arial', 12, 'bold'),
                                fg='#DAD5D6', bg='#158645',
                                cursor='hand2', activebackground='#35BD6F')
        self.boton_nuevo.grid(row=4, column=0, padx=10, pady=10)

        self.boton_guardar = tk.Button(self, text="Guardar")
        self.boton_guardar.config(width=20, font=('Arial', 12, 'bold'),
                                fg='#DAD5D6', bg='#1658A2',
                                cursor='hand2', activebackground='#3586DF')
        self.boton_guardar.grid(row=4, column=1, padx=10, pady=10)

        self.boton_cancelar = tk.Button(self, text="Cancelar")
        self.boton_cancelar.config(width=20, font=('Arial', 12, 'bold'),
                                fg='#DAD5D6', bg='#BD152E',
                                cursor='hand2', activebackground='#E15370')
        self.boton_cancelar.grid(row=4, column=2, padx=10, pady=10)

