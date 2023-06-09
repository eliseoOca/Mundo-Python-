import sqlite3

def conectar():
    conexion= sqlite3.connect("miBD.db")
    cursor = conexion.cursor()
    return conexion,cursor
def crearTabla():
    conexion,cursor=conectar()
    sql="""
        CREATE TABLE IF NOT EXISTS agenda(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nombre VARCHAR(20) NOT NULL,
            telefono VARCHAR(14) NOT NULL
        )
    """
    if(cursor.execute(sql)):
        print("Tabla creada")
    else:
        print("No se pudo crear la tabla ")
    conexion.close()
    
def insertar(datos):
    conexion, cursor=conectar()
    sql="""
        INSERT INTO agenda(nombre,telefono) VALUES (?,?)    
    """
    if(cursor.execute(sql, datos)):
        print("datos guardados")
    else:
        print("No se pudieron guardar los datos")
    conexion.commit()
    conexion.close()

def consultar():
    conexion, cursor=conectar()
    cursor.execute("SELECT id,nombre,telefono from agenda")
    for fila in cursor:
        print("ID = ",fila[0])
        print("Nombre = ",fila[1])
        print("Telefono = ",fila[2])
    conexion.close()
    
def modificar(id, telefono):
    conexion, cursor = conectar()
    sql= "UPDATE agenda SET TELEFONO="+telefono+" where ID="+id
    cursor.execute(sql)
    cursor.close()
    conexion.commit()
    conexion.close()
    
def borrar(id):
    conexion, cursor=conectar()
    sql = "DELETE from agenda where ID="+id
    cursor.execute(sql)
    cursor.close()
    conexion.commit()
    conexion.close()

crearTabla()
#datos=("Eliseo","12345678")
#insertar(datos)
#datos=("Rosario","123456789")
#insertar(datos)
#datos=("Bautista","1234567890")
#insertar(datos)
#consultar()
#datos=("Bautista","1234567890")
#insertar(datos)
#consultar()
#modificar("4", "123123")
#consultar()
borrar("3")
consultar()