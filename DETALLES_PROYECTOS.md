# Predict-CDT
EL proyecto constan de varios pasos dentro de los cuales es encuenta llevar los archivos planos en formato csv descargados de Kaggle y generar una base de datos usado SQLLite3 de pandas usando la clase ```DataBAseManager´´´
Se crear la clases que generan las tablas y la estructura de las mismas
```python
# Importacion recursos
import sqlite3
import pandas as pd
from config.parametros import RutaDataSet as RT

# Clase adminsitradora de tablas
class DatabaseManager:
    def __init__(self, db_path) -> None:
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
    
    def create_table(self, nombre_tabla, esquema_tabla):
        """Crea una tabla en la base de datos si la tabla no existe"""
        try:
            self.cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS {nombre_tabla} (
                    {esquema_tabla}
                )
            """)
            print(f'Tabla {nombre_tabla} creada o ya existe')
        except sqlite3.Error as e:
            print(f'Error al crear la tabla {nombre_tabla}: {e}')

    def Cerrar_coneccion(self):
        if self.conn:
            self.conn.close()
            print('Conexion a las base de datos cerrada')
