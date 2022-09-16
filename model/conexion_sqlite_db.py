import sqlite3


class ConexionDB:
    # contructor de la clase
    def __init__(self):
        # se conecta a la base de datos (archivo de sqlite), en caso que no exista, la crea.
        self.base_datos = '/database/peliculas.db'
        self.conexion = sqlite3.connect(self.base_datos)
        # Se crea un cursor para realizar operaciones sobre a base de datos
        self.cursor = self.conexion.cursor()

    def cerrar(self):
        # siempre que se abre una conexion, se debe cerrar al terminar las operaciones requeridas
        self.conexion.commit()
        self.conexion.close()

