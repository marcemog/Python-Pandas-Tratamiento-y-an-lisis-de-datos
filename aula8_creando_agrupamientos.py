# -*- coding: utf-8 -*-
"""Aula8 Creando agrupamientos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jSf4-npN9IhiguY52r6JaunkaRqkcT-V

#Reporte de Analisis VII

##Creando agrupamientos
"""

import pandas as pd

datos = pd.read_csv('alquiler_residencial.csv', sep=';')

datos.head(10)

#vamos a calcular las medianas para cada uno de los distritos

datos['Valor'].mean() #saca la media aritmetica de la columna Valor

#barrios = ['Ate','Barranco','Comas','Lince','El Agustino','San Luis','Callao']  #crea una lista de barrios o distritos que interesan y hace que el DataFrame solo muestre esos
#seleccion = datos['Distrito'].isin(barrios)
#datos = datos[seleccion]                                    ##se comentaron estas lineas para poder observar todos los barrios, si saco el # van a quedar solo los barrios de la lista

datos.head(10)

datos['Distrito'].drop_duplicates()

grupo_barrio = datos.groupby('Distrito')

type(grupo_barrio)

grupo_barrio.groups

for barrio,data in grupo_barrio:
  print(barrio)

for barrio,data in grupo_barrio:                              #imprime el nombre del barrio o distrito y su valor medio 
  print('{} -> {}'.format(barrio, data.Valor.mean()))

grupo_barrio['Valor'].mean().round(2)   #imprime el nombre del barrio o distrito y su valor medio

grupo_barrio[['Valor', 'Mantenimiento']].mean().round(2)   #imprime el nombre del barrio o distrito y su valor medio de valor y mantenimiento

"""##Estadisticas descriptivas"""

grupo_barrio['Valor'].describe().round(2)  #genera estadisticas descriptivas de la columna valor en grupo_barrio

grupo_barrio['Valor'].aggregate(['min','max'])  #genera un resumen de las columnas min y max que queriamos observar

grupo_barrio['Valor'].aggregate(['min','max']).rename(columns = {'min':'Minimo', 'max':'Maximo'})  #lo mismo de arriba pero cambiando los nombres de las columnas

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib.pyplot as plt
plt.rc('figure', figsize = (20,10))

fig = grupo_barrio['Valor'].mean().plot.bar(color = 'blue')
fig.set_ylabel('Valor del Alquiler')
fig.set_title('Valor medio del Alquiler por Distrito', {'fontsize': 22})

fig = grupo_barrio['Valor'].max().plot.bar(color = 'blue')
fig.set_ylabel('Valor del Alquiler')
fig.set_title('Valor maximo del Alquiler por Distrito', {'fontsize': 22})
