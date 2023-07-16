import sqlite3
import os

# Obtener la ruta de la base de datos
db_path = os.path.abspath(r'C:\DBSQLite\BaseDatos\DB_p.db')

# Conectarse a la base de datos
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Función para leer una foto
def read_photo(photo_id):
    cursor.execute("""
        SELECT * FROM photos WHERE id = ?
    """, (photo_id,))
    return cursor.fetchone()

try:
    # Leer una foto
    photo_id = 1001
    photo_data = read_photo(photo_id)
    if photo_data:
        print("Datos de la foto:", photo_data)
    else:
        print("No se encontró ninguna foto con el ID", photo_id)
except Exception as e:
    print("Error al leer la foto:", str(e))

# Cerrar la conexión
conn.close()