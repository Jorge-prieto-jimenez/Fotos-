import sqlite3
import os

# Obtener la ruta de la base de datos
db_path = os.path.abspath(r'C:\DBSQLite\BaseDatos\DB_p.db')

# Conectarse a la base de datos
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Función para actualizar una foto
def update_photo(photo_id, new_data):
    cursor.execute("""
        UPDATE photos SET title = ?, url = ?, thumbnailUrl = ?
        WHERE id = ?
    """, (new_data['title'], new_data['url'], new_data['thumbnailUrl'], photo_id))
    conn.commit()

try:
    # Actualizar una foto
    photo_id = 2
    updated_data = {
        "title": "Nuevo título",
        "url": "https://example.com/nueva_url.jpg",
        "thumbnailUrl": "https://example.com/nuevo_thumbnail.jpg"
    }
    update_photo(photo_id, updated_data)
    print("Foto actualizada correctamente.")
except Exception as e:
    print("Error al actualizar la foto:", str(e))

# Cerrar la conexión
conn.close()