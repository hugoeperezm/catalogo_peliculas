import sqlite3


class ConexionDB:
    database_path = 'database/peliculas.db'
    sql = '''
                CREATE TABLE peliculas(
                    id_pelicula INTEGER NOT NULL,
                    nombre VARCHAR(100),
                    duracion VARCHAR(10),
                    genero VARCHAR(100),
                    PRIMARY KEY(id_pelicula AUTOINCREMENT)
                )
                '''

    # contructor de la clase
    def __init__(self):
        # se conecta a la base de datos (archivo de sqlite), en caso que no exista, la crea.
        self.base_datos = ConexionDB.database_path
        self.conexion = sqlite3.connect(self.base_datos)
        # Se crea un cursor para realizar operaciones sobre a base de datos
        self.cursor = self.conexion.cursor()

    def cerrar(self):
        # siempre que se abre una conexion, se debe cerrar al terminar las operaciones requeridas
        self.conexion.commit()
        self.conexion.close()


