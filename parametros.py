"""
-------------------------------------------------------
PARAMETROS DEL MODELOS
Autor: @Nicolas Torres
Contacto: 3213107305
-------------------------------------------------------
"""

import os
class RutaDataSet:
    # Archivos Originales
    Campaing = os.path.join('Archivos','campaign_inf.csv')
    Qualitative = os.path.join('Archivos','qualitative.csv')
    db_split = os.path.join('Archivos','db_split.csv')
    SampleSubmission = os.path.join('Archivos','sampleSubmission.csv')
    DataBase = os.path.join('database','BaseDatosSQL.db')
    # Matrices de trabajo
    X = os.path.join('Archivos','X_CDT')
    y = os.path.join('Archivos','y_CDT')
    e = os.path.join('Archivos','Etiqueta_cliente')
    # Archivos de salida
    RegresionLogistica = os.path.join('Archivos','Submission(Regresion_Logistica).csv')
    ArbolDecision = os.path.join('Archivos','Submission(Arboles_Decision).csv')
    RedNeuronal = os.path.join('Archivos','Submission(Red_Neuronal).csv')

    