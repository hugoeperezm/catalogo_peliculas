# este archivo crea los objetos de la base de datos: tablas
# Por encontrarse en el mismo paquete, puede usarse el punto (.conexion_sqlite_db)
import sqlite3
from .conexion_sqlite_db import ConexionDB #, sql_tabla_peliculas
# from .conexion_mysql_db import ConexionDB, sql_tabla_peliculas
from tkinter import messagebox


def crear_tabla():
    # conexion = ConexionDB()  --la llamada a la conexion se controla con el try
    titulo = 'Crear Tabla'
    sql = ConexionDB.sql
    # sql = '''
    #         CREATE TABLE peliculas(
    #             id_pelicula INTEGER NOT NULL,
    #             nombre VARCHAR(100),
    #             duracion VARCHAR(10),
    #             genero VARCHAR(100),
    #             PRIMARY KEY(id_pelicula AUTOINCREMENT)
    #         )
    #         '''
    try:
        conexion = ConexionDB()
        conexion.cursor.execute(sql)
        conexion.cerrar()
        mensaje = f'Se creó la tabla en la base de datos "{ConexionDB.database_path}".'
        messagebox.showwarning(titulo, mensaje)
    except sqlite3.OperationalError as err:
        mensaje = f'No se ha podido abrir la base de datos "{ConexionDB.database_path}".' \
                  f'\n\nDescripcion del error : {err}'
        messagebox.showwarning(titulo, mensaje)
    except sqlite3.ProgrammingError as err:
        mensaje = f'La tabla ya está creada.' \
                  f'\n\nDescripcion del error : {err}'
        messagebox.showwarning(titulo, mensaje)
    except BaseException as err:
        mensaje = f'Se ha presentado un error desconocido.' \
                  f'\n\nDescripcion del error : {err}'
        messagebox.showwarning(titulo, mensaje)


def borrar_tabla():
    # conexion = ConexionDB()

    titulo = 'Borrar Tabla'
    sql = 'DROP TABLE peliculas'
    try:
        conexion = ConexionDB()
        conexion.cursor.execute(sql)
        conexion.cerrar()
        mensaje = 'Se borró la tabla con éxito'
        messagebox.showwarning(titulo, mensaje)
    except sqlite3.OperationalError as err:
        mensaje = f'No se ha podido abrir la base de datos.' \
                  f'\n\nDescripcion del error : {err}'
        messagebox.showwarning(titulo, mensaje)
    except sqlite3.ProgrammingError as err:
        mensaje = f'No hay tablas para borrar.' \
                  f'\n\nDescripcion del error : {err}'
        messagebox.showwarning(titulo, mensaje)
    except BaseException as err:
        mensaje = f'Se ha presentado un error desconocido.' \
                  f'\n\nDescripcion del error : {err}'
        messagebox.showwarning(titulo, mensaje)


class Pelicula:
    def __init__(self, nombre, duracion, genero):
        self.id_pelicula = None
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero

    def __str__(self):
        return f'Pelicula[{self.nombre}, {self.duracion}, {self.genero}]'

def guardar(pelicula):
    conexion = ConexionDB()

    titulo = 'Conexion al Registro'
    mensaje = 'La tabla peliculas no está creada en la base de datos'

    sql = f"""INSERT INTO peliculas (nombre, duracion, genero)
                VALUES('{pelicula.nombre}', '{pelicula.duracion}', '{pelicula.genero}')"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        messagebox.showerror(titulo, mensaje)

