import sqlite3
import os

# Obtener la ruta de la base de datos
db_path = os.path.abspath(r'C:\DBSQLite\BaseDatos\DB_p.db')

# Conectarse a la base de datos
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Función para eliminar una foto
def delete_photo(photo_id):
    cursor.execute("DELETE FROM photos WHERE id = ?", (photo_id,))
    conn.commit()

try:
    #Eliminar una foto
    photo_id = 4
    delete_photo(photo_id)
    print("Foto eliminada correctamente.")
except Exception as e:
    print("Error al eliminar la foto:", str(e))

# Cerrar la conexión
conn.close()