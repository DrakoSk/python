import MySQLdb
bd = MySQLdb.Connect("localhost","root","","prueba_db")
cursor = bd.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("Version de base de datos: %s " %data)
sql="INSERT INTO EMPLEADO(NOMBRE, APELLIDO,EDAD,SEXO,SALARIO) VALUES('jhon','Ñunez', 22, 'M',3000)"
try:
    cursor.execute(sql)
    bd.commit()
except:
    bd.rollback()
bd.close()
