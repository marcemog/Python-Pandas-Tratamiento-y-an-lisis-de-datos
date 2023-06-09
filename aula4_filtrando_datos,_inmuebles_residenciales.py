# -*- coding: utf-8 -*-
"""Aula4 Filtrando datos, inmuebles residenciales.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KgDfCPmpTaBgWPQCDvixsTOayuJ105iI

#Reporte de Analisis 3

##Inmuebles residenciales
"""

import pandas as pd

datos = pd.read_csv('alquiler.csv', sep=';')
datos.head(10)

list(datos['Tipo'].drop_duplicates())

residencial = ['Habitación',
 'Casa',
 'Departamento',
 'Casa en condominio',
 'Casa comercial',
 'Casa de villa']
residencial

datos.head(10)

seleccion = datos['Tipo'].isin(residencial)
seleccion

datos_residencial = datos[seleccion]
datos_residencial

list(datos_residencial['Tipo'].drop_duplicates())

datos_residencial.shape[0]

datos_residencial.index = range(datos_residencial.shape[0])
datos_residencial

"""##Exportando la base de datos"""

datos_residencial.to_csv('alquiler_residencial.csv', sep= ';')

datos_residencial2 = pd.read_csv('alquiler_residencial.csv', sep= ';')
datos_residencial2

datos_residencial.to_csv('alquiler_residencial.csv', sep= ';', index = False)

datos_residencial2 = pd.read_csv('alquiler_residencial.csv', sep= ';')
datos_residencial2

