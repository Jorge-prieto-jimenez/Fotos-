import sqlite3
import os

# Obtener la ruta de la base de datos
db_path = os.path.abspath('C:\DBSQLite\BaseDatos\DB_p.db')

# Conectarse a la base de datos
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Datos álbumes
albums_data = [
    {"id": 2, "title": "dbjskbJKNJKN"},

]

# Insertar los álbumes en la tabla
for album in albums_data:
    cursor.execute("INSERT INTO albums (id, title) VALUES (?, ?)",
                   (album['id'], album['title']))




# Datos fotos
photos_data = [
    {
        "albumId": 1,
        "id": 2,
        "title": "accusamus beatae ad facilis cum similique qui sunt",
        "url": "https://via.placeholder.com/600/92c952",
        "thumbnailUrl": "https://via.placeholder.com/150/92c952"
    },

]

# Insertar las fotos en la tabla
for photo in photos_data:
    cursor.execute("INSERT INTO photos (albumId, id, title, url, thumbnailUrl) VALUES (?, ?, ?, ?, ?)",
                   (photo['albumId'], photo['id'], photo['title'], photo['url'], photo['thumbnailUrl']))

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()