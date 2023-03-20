import sqlite3

def conectar():
    conexion = sqlite3.connect("datos.db")
    cursor = conexion.cursor()
    return conexion, cursor

def crearTabla():
    conexion, cursor = conectar()
    sql="""
    CREATE TABLE IF NOT EXISTS alumnos(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        nombre VARCHAR(25) NOT NULL,
        nota INTEGER NOT NULL
    )
    """
    if(cursor.execute(sql)):
        print("Tabla Creada")
    else:
        print("No se pudo crear la tabla")
    conexion.close()
    
def insertar(datos):
    conexion, cursor=conectar()
    sql="""
        INSERT INTO alumnos(nombre,nota) VALUES(?,?)
    """
    if(cursor.execute(sql, datos)):
        print("Datos guardados")
    else:
        print("No se puedieron guardar los datos")
    conexion.commit()
    conexion.close()

def consultar():
    conexion, cursor = conectar()
    sql =  """SELECT id, nombre, nota from alumnos"""
    cursor.execute(sql)
    for fila in cursor:
        print("ID = ", fila[0])
        print("Nombre = ", fila[1])
        print("Nota = ", fila[2], "\n")
    conexion.close()
    
def modificar(id, nota):
    conexion, cursor= conectar()
    id= str(id)
    nota= str(nota)
    sql="UPDATE alumnos SET nota="+nota+" WHERE id="+id
    cursor.execute(sql)
    cursor.close()
    conexion.commit()
    conexion.close()
    print("Se ha modificado el registro.\n")
    
def borrar(id):
   conexion, cursor = conectar()
   id = str(id)
   sql="DELETE from alumnos WHERE id="+id
   cursor.execute(sql)
   cursor.close()
   conexion.commit()
   conexion.close()
   print("Se ha borrado el registro.\n") 

if __name__=="__main__":
    #crearTabla()
    #for i in range(3):
     #   nombre=input("Dime el nombre del alumno: ")
      #  nota=input("Dime la nota que saco el alumno: ")
       # datos = nombre, nota
        #insertar(datos)
    consultar()
    #borrar(3)
    modificar(1,7)
    consultar()