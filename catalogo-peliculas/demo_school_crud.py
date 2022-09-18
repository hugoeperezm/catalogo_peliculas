#Importar la libreria mysql.connector
import mysql.connector
import datetime

#Hacer una función donde se va conectar la base de datos
def conectar():
    try:
        cnn = mysql.connector.connect(host='localhost', user='root',
                                      password = 'Narly2016', database='colegio')
        #print('Conexión Exitosa')
    except:
        print('No hubo conexión')
    return cnn

def consultar_alumnos():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM alumnos')
    datos_alu = cursor.fetchall()
    cursor.close()
    conexion.close()
    return datos_alu

def insertar_alumnos(ID, nombres, apellidos, grado, grupo, fecha_ingreso, edad):
    conexion = conectar()
    cursor = conexion.cursor()
    alumnos = '''INSERT INTO alumnos (ID, nombres, apellidos, grado, grupo, fecha_ingreso, edad)
                values ({}, '{}', '{}', '{}', '{}', '{}', {})'''.format(ID, nombres, apellidos, grado, grupo, fecha_ingreso, edad)
    cursor.execute(alumnos)
    filas = cursor.rowcount
    conexion.commit()
    cursor.close()
    return filas

def actualizar_alumonos(ID, nombres, apellidos, grado, grupo, fecha_ingreso, edad):
    conexion = conectar()
    cursor = conexion.cursor()
    oferentes = '''UPDATE alumnos SET nombres='{}', apellidos='{}', grado={}, grupo='{}',
                fecha_ingreso='{}', edad={} 
                WHERE ID={}'''.format(nombres, apellidos, grado, grupo, fecha_ingreso, edad, ID)
    cursor.execute(oferentes)
    filas = cursor.rowcount
    conexion.commit()
    cursor.close()
    return filas

def eliminar_alumnos(ID):
    conexion = conectar()
    cursor = conexion.cursor()
    oferentes = 'DELETE FROM alumnos WHERE ID = {}'.format(ID)
    cursor.execute(oferentes)
    filas = cursor.rowcount
    conexion.commit()
    cursor.close()
    return filas

print('***************')
print('*TABLA ALUMNOS*')
print('1. CONSULTAR\n2. INSERTAR \n3. ACTUALIZAR\n4. ELIMINAR\n5. VOLVER')

opcion = int(input('Ingrese un número del 1 al 5, 5 Salir\n'))
while opcion != 5:
    if opcion == 1:
        alumnos = consultar_alumnos()
        print(alumnos)
    elif opcion == 2:
        ID = int(input('Ingrese el ID: '))
        nom = input('Ingrese los nombres del alumno: ')
        ape = input('Ingrese los apellidos del alumno: ')
        gra = input('Ingrese el grado del alumno: ')
        gru = input('Ingrese el grupo del alumno: ')
        dia = int(input('Ingrese el día: '))
        mes = int(input('Ingrese el mes: '))
        año = int(input('Ingrese el año: '))
        f_ing = datetime.datetime(año, mes, dia)
        ed = int(input('Ingrese la edad: '))
        insertar_alumnos(ID, nom, ape, gra, gru, f_ing, ed)
    elif opcion == 3:
        ID = int(input('Ingrese el ID: '))
        nom = input('Ingrese los nombres del alumno: ')
        ape = input('Ingrese los apellidos del alumno: ')
        gra = input('Ingrese el grado del alumno: ')
        gru = input('Ingrese el grupo del alumno: ')
        dia = int(input('Ingrese el día: '))
        mes = int(input('Ingrese el mes: '))
        año = int(input('Ingrese el año: '))
        f_ing = datetime.datetime(año, mes, dia)
        ed = int(input('Ingrese la edad: '))
        actualizar_alumonos(ID, nom, ape, gra, gru, f_ing, ed)
    elif opcion == 4:
        codigo = int(input('Ingrese el codigo del estudiante: '))
        eliminar_alumnos(codigo)
    elif opcion == 5:
        import EJERCICIO_FP_COLEGIO
        EJERCICIO_FP_COLEGIO
    else:
        print('Opción no válida')
    opcion = int(input('Ingrese un número del 1 al 5:'))