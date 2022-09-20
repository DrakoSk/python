import MySQLdb.connections
dbconexion = {'host': 'localhost',
              'user':'root',
              'password':'',
              'database':'asistencia1'}
conexion = MySQLdb.connect(**dbconexion)
cursor = conexion.cursor()
sql = "Select * from alumno2"
cursor.execute(sql)
res = cursor.fetchall()
print(res)
