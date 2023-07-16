import sqlite3
import os

# Obtener la ruta de la base de datos
db_path = os.path.abspath(r'C:\DBSQLite\BaseDatos\DB_p.db')

# Conectarse a la base de datos
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Función para crear una foto
def create_photo(photo):
    cursor.execute("INSERT INTO photos (albumId, id, title, url, thumbnailUrl) VALUES (?, ?, ?, ?, ?)",
                   (photo['albumId'], photo['id'], photo['title'], photo['url'], photo['thumbnailUrl']))
    conn.commit()


# Crear una foto
try:
    # CRUD: Crear una foto
    new_photo = {
        "albumId": 1,
        "id": 4,
        "title": "Nueva foto",
        "url": "https://example.com/nueva_foto.jpg",
        "thumbnailUrl": "https://example.com/nueva_foto_thumbnail.jpg"
    }
    create_photo(new_photo)
    print("Foto creada correctamente.")
except Exception as e:
    print("Error al crear la foto:", str(e))


# Cerrar la conexión
conn.close()