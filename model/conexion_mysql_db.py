# Importar la libreria mysql.connector
import pymysql


class ConexionDB:
    sql = '''
                CREATE TABLE peliculas(
                    id_pelicula INTEGER AUTO_INCREMENT NOT NULL,
                    nombre VARCHAR(100),
                    duracion VARCHAR(10),
                    genero VARCHAR(100),
                    PRIMARY KEY(id_pelicula)
                )
                '''

    # contructor de la clase
    def __init__(self):
        # se conecta a la base de datos (archivo de sqlite), en caso que no exista, la crea.
        try:
            self.conexion = pymysql.connect(host='localhost',
                                            user='root',
                                            password='Training2017*',
                                            db='peliculadb')
            # Se crea un cursor para realizar operaciones sobre a base de datos
            self.cursor = self.conexion.cursor()
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            # print("Ocurrió un error al conectar: ", e)
            pass

    def cerrar(self):
        # siempre que se abre una conexion, se debe cerrar al terminar las operaciones requeridas
        self.conexion.commit()
        self.conexion.close()

    def crear_basedatos(self):
        pass

