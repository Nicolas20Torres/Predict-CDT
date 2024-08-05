# Importacion de recursos
from config.parametros import RutaDataSet as RT
import pandas as pd
import sqlite3

# Generar Conexion a la base de datos
conn = sqlite3.connect(RT.DataBase)
cursor = conn.cursor()
# Lectura de archivos planos
df_campanas = pd.read_csv(RT.Campaing,encoding='utf-8',sep=',')
df_qualitative = pd.read_csv(RT.Qualitative,encoding='utf-8',sep=',')

# Conexion a base de datos SQL
df_qualitative.to_sql('Qualitative',conn,if_exists='replace',index=False)
df_campanas.to_sql('Campanas',conn,if_exists='replace',index=False)
