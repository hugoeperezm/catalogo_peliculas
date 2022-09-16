# este archivo crea los objetos de la base de datos: tablas
# Por encontrarse en el mismo paquete, puede usarse el punto (.conexion_sqlite_db)

from .conexion_mysql_db import ConexionDB
from tkinter import messagebox


def crear_tabla():
    conexion = ConexionDB()
    titulo = 'Crear Tabla'
    sql = '''
    CREATE TABLE peliculas(
        id_pelicula INTEGER AUTO_INCREMENT NOT NULL,
        nombre VARCHAR(100),
        duracion VARCHAR(10),
        genero VARCHAR(100),
        PRIMARY KEY(id_pelicula)
    )
    '''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        mensaje = 'Se creó la tabla en la base de datos'
        messagebox.showwarning(titulo, mensaje)
    except:
        mensaje = 'La tabla ya está creada'
        messagebox.showwarning(titulo, mensaje)


def borrar_tabla():
    conexion = ConexionDB()

    titulo = 'Borrar Tabla'
    sql = 'DROP TABLE peliculas'
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        mensaje = 'Se borró la tabla con éxito'
        messagebox.showwarning(titulo, mensaje)
    except:
        mensaje = 'No hay tabla para borrar'
        messagebox.showwarning(titulo, mensaje)


def crear_basedatos():
    pass


