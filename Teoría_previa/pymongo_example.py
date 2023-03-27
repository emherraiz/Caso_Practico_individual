from pymongo import MongoClient

# Conectar a la db, host y puerto
conn = MongoClient(host='localhost', port=1234)

# Obtener base de datos
db = conn.local

# Insertar datos en coleccion alumnos
db.alumnos.insert_one({"nombre": "Alberto", "edad": 30})
db.alumnos.insert_one({"nombre": "Fran", "edad": 25})

# Insertar datos en colección asignaturas
db.asignaturas.insert_one({"asignatura": "IA", "temas": ["Tema1", "Tema2"]})
db.asignaturas.insert_one({"asignatura": "Github", "temas": ["Tema1", "Tema2", "Prácticas"]})

# Operaciones con "find"
print(db.alumnos.find())

# Todos los datos de las colecciones
for data in db.alumnos.find():
	print(data)

for data in db.asignaturas.find():
	print(data)

# Todos los datos en base a condiciones
for data in db.alumnos.find({"name": "Alberto"}):
	print(data)

for data in db.alumnos.find({"edad": {"$gt" : 27}}):
	print(data)

for data in db.alumnos.find({"edad": {"$lt" : 27}}):
	print(data)

for data in db.alumnos.find({"edad": {"$gte" : 25}}):
	print(data)

# Eliminar coleccion de datos
db.asignaturas.drop()

# Eliminar datos en base a condiciones
db.alumnos.delete_many({"edad": {"$gt" : 27}})
