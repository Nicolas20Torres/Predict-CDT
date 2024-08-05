# Importacion recursos
import sqlite3
import pandas as pd
from config.parametros import RutaDataSet as RT

# Clase adminsitradora de tablas
class DatabaseManager:
    def __init__(self,db_path) -> None:
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
    
    def create_table(self,nombre_tabla,esquema_tabla):
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

# Creacion de las tablas
if __name__ == '__main__':
    db_conexionSQL = DatabaseManager(RT.DataBase)

    # Construcion de la tabla Qualitative
    esquema_qualitative =  """
            ID INTEGER PRIMARY KEY,
            Edad INTEGER,
            Tipo_Trabajo TEXT,
            Estado_Civil TEXT,
            Educacion TEXT,
            Contacto TEXT
    """
    db_conexionSQL.create_table('Qualitative',esquema_qualitative)

    # Construccion de la tabla Campaing
    esquema_campanas = """
            Id_tabla_campanas INTEGER PRIMARY KEY AUTOINCREMENT,
            ID INTEGER,
            mora TEXT,
            Vivienda TEXT,
            Consumo TEXT,
            Mes TEXT,
            Dia TEXT,
            Campana INTEGER,
            Dias_Ultima_Camp INTEGER, 
            No_Contactos INTEGER, 
            Resultado_Anterior TEXT, 
            emp_var_rate FLOAT,
            cons_price_idx FLOAT, 
            cons_conf_idx FLOAT, 
            euribor3m FLOAT, 
            nr_employed FLOAT, 
            y INTEGER,
            FOREIGN KEY (ID) REFERENCES Cualitative (ID) 
    """
    db_conexionSQL.create_table('Campanas',esquema_campanas)
