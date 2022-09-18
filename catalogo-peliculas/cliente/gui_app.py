# Este archivo será la interfaz de usuario la aplicacion
# 1. Se importa el modulo tkinter
# 2. Se define la clase Frame
# 3. Se crear la barra de mnú con las diferentes menus y opciones
# 4. Se crea los labels (3) los Entry (3) y los botones (3)
# 5. Se aplica funcionalidad de habilitar y deshabilitar de acuerdo a las reglas
# 6. Se Crear un TreeView para mostrar los datos como una tabla de datos
# 7. Crear paquete model y database para crear tabla y eliminar tabla.
#    Crear comando adicionar registro a la bd y eliminar registro a la bd en las opciones del menu
# 8. Crear


import tkinter as tk
from tkinter import ttk
from model.pelicula_dao import crear_tabla, borrar_tabla
from model.pelicula_dao import Pelicula, guardar


def barra_menu(root):
    # La funcion barra_menu diseña y crear toda la barra de menús recibiendo el parametro root

    # crea la barra de menues y le da una configuracion
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu, width=300, height=300)

    # Define el primer menú y quita el lineado que le aparece, con tearoff=0
    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Archivo', menu=menu_inicio)

    # Se adiciona cada comando o cada opcion del menu Archivo
    menu_inicio.add_command(label='Crear registro en DB', command=crear_tabla)
    menu_inicio.add_command(label='Eliminar registro en DB', command=borrar_tabla)
    menu_inicio.add_command(label='Salir', command=root.destroy)

    barra_menu.add_cascade(label='Consultas')
    barra_menu.add_cascade(label='Herramientas')
    barra_menu.add_cascade(label='Ayuda')


class Frame(tk.Frame):
    # Esta clase espera un frame none y se define el self
    # y el root que recibe desde el modulo principal
    def __init__(self, root=None):
        # Heredar el constructor de la clase padre y recibe la raiz y la configuracion
        super().__init__(root, width=480, height=320)
        self.tabla = None
        self.label_genero = None
        self.label_duracion = None
        self.label_nombre = None
        self.root = root
        self.pack()
        # self.config(bg='green')
        # self.label_nombre = None
        self.campos_pelicula()
        self.deshabilitar_campos()
        self.tabla_peliculas()

    def campos_pelicula(self):
        # Labels de cada campo donde muestra los campos
        self.label_nombre = tk.Label(self, text='Nombre: ')
        self.label_nombre.config(font=('Arial', 12, 'bold'))
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)

        self.label_duracion = tk.Label(self, text='Duración: ')
        self.label_duracion.config(font=('Arial', 12, 'bold'))
        self.label_duracion.grid(row=1, column=0, padx=10, pady=10)

        self.label_genero = tk.Label(self, text='Género: ')
        self.label_genero.config(font=('Arial', 12, 'bold'))
        self.label_genero.grid(row=2, column=0, padx=10, pady=10)

        # Entrys de cada campo
        # Ahora se va a agregar una var tk.StringVar() y el config textvariable
        # para poder borrar el contenido de un Entry
        self.mi_nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable=self.mi_nombre)
        self.entry_nombre.config(width=50, font=('Arial', 12))
        # Los entrys están ocupando una sola columna en el grid. Para que ocupe dos columnas,
        # se agrega la propiedad: columnspan=2
        # self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

        # En este punto se quita las config state='disabled', porque se va a manejar con dos funciones
        # deshabilitar_campos() y habilitar_campos()
        self.mi_duracion = tk.StringVar()
        self.entry_duracion = tk.Entry(self, textvariable=self.mi_duracion)
        self.entry_duracion.config(width=50, font=('Arial', 12))
        self.entry_duracion.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

        self.mi_genero = tk.StringVar()
        self.entry_genero = tk.Entry(self, textvariable=self.mi_genero)
        self.entry_genero.config(width=50, font=('Arial', 12))
        self.entry_genero.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

        # Botones de Nuevo registro, ...
        # en la pagina https://htmlcolorcodes.com/es se puede obtener los codigos de los colores
        self.boton_nuevo = tk.Button(self, text="Nuevo", command=self.habilitar_campos)
        self.boton_nuevo.config(width=20, font=('Arial', 12, 'bold'),
                                fg='#DAD5D6', bg='#158645',
                                cursor='hand2', activebackground='#35BD6F')
        self.boton_nuevo.grid(row=3, column=0, padx=10, pady=10)

        self.boton_guardar = tk.Button(self, text="Guardar", command=self.guardar_datos)
        self.boton_guardar.config(width=20, font=('Arial', 12, 'bold'),
                                fg='#DAD5D6', bg='#1658A2',
                                cursor='hand2', activebackground='#3586DF')
        self.boton_guardar.grid(row=3, column=1, padx=10, pady=10)

        self.boton_cancelar = tk.Button(self, text="Cancelar", command=self.deshabilitar_campos)
        self.boton_cancelar.config(width=20, font=('Arial', 12, 'bold'),
                                fg='#DAD5D6', bg='#BD152E',
                                cursor='hand2', activebackground='#E15370')
        self.boton_cancelar.grid(row=3, column=2, padx=10, pady=10)

    def habilitar_campos(self):
        # En segundo lugarse va a enviar un valor vacio a los entry
        self.mi_nombre.set('')
        self.mi_duracion.set('')
        self.mi_genero.set('')

        # En primer lugar se va a habilitar la config de los botones
        self.entry_nombre.config(state='normal')
        self.entry_duracion.config(state='normal')
        self.entry_genero.config(state='normal')

        self.boton_guardar.config(state='normal')
        self.boton_cancelar.config(state='normal')

    def deshabilitar_campos(self):
        # En segundo lugarse va a enviar un valor vacio a los entry
        self.mi_nombre.set('')
        self.mi_duracion.set('')
        self.mi_genero.set('')

        # En primer lugar se va a deshabilitar la config de los botones
        self.entry_nombre.config(state='disabled')
        self.entry_duracion.config(state='disabled')
        self.entry_genero.config(state='disabled')

        self.boton_guardar.config(state='disabled')
        self.boton_cancelar.config(state='disabled')

    def guardar_datos(self):

        pelicula = Pelicula(
            self.mi_nombre.get(),
            self.mi_duracion.get(),
            self.mi_genero.get()
        )

        guardar(pelicula)

        # Se deshabilitan los campos
        self.deshabilitar_campos()

    def tabla_peliculas(self):
        '''En este nuevo paso, se crea una tabla tipo TreeView de ttk, con 4 columnas.
        Para ello, se debe importar la libreria ttk de TKinter
        y corregir la posicion de los botones a la fila 3'''

        self.tabla = ttk.Treeview(self,
                                  column=('Nombre', 'Duracion', 'Genero'))
        self.tabla.grid(row=4, column=0, columnspan=4)

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='NOMBRE')
        self.tabla.heading('#2', text='DURACION')
        self.tabla.heading('#3', text='GENERO')

        # INSERTAR A LA TABLA UN VALOR DUMMY
        # A la raiz se le envia vacio
        # Al indice se le envía 0
        # Al texto se le envía el ID con valor 1
        # y se envia los valores de la columna en una tupla
        self.tabla.insert('', 0, text='1',
                          values=('Los Vengadores', '2.35', 'Accion'))

        self.tabla.insert('', 1, text='2',
                          values=('Juego de Tronos', '2.15', 'Ciencia Ficcion'))

        # Se crean los botones finales para controlar la data de la tabla (TreeView)
        # en la pagina https://htmlcolorcodes.com/es se puede obtener los codigos de los colores
        self.boton_editar = tk.Button(self, text="Editar")
        self.boton_editar.config(width=20, font=('Arial', 12, 'bold'),
                                fg='#DAD5D6', bg='#158645',
                                cursor='hand2', activebackground='#35BD6F')
        self.boton_editar.grid(row=5, column=0, padx=10, pady=10)

        self.boton_eliminar = tk.Button(self, text="Eliminar")
        self.boton_eliminar.config(width=20, font=('Arial', 12, 'bold'),
                                   fg='#DAD5D6', bg='#BD152E',
                                   cursor='hand2', activebackground='#E15370')
        self.boton_eliminar.grid(row=5, column=1, padx=10, pady=10)