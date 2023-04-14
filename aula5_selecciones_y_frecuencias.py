# -*- coding: utf-8 -*-
"""Aula5 Selecciones y frecuencias.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fiZaYI3pWQAfCIvMYZoylWMYgaww8dfO

#Reporte de Analisis IV

##Selecciones y frecuencias
"""

import pandas as pd

datos = pd.read_csv('alquiler_residencial.csv', sep=';')
datos.head(10)

#seleccione solamente los inmuebles clasificados como 'Departamento'

seleccion = datos['Tipo'] == 'Departamento'
n1 = datos[seleccion]
n1

n1.shape[0] #Frecuencia de veces que se repite alguna de las condiciones

#seleccione los inmuebles clasificados con tipos 'Casa', 'Casa en condominio' y 'Casa de villa'

seleccion = (datos['Tipo'] == 'Casa') | (datos['Tipo'] == 'Casa en condominio') | (datos['Tipo'] == 'Casa de villa')
n2 = datos[seleccion]
n2

n2.shape[0]  #Frecuencia de veces que se repite alguna de las condiciones

#selecciones los inmuebles con area entre 60 y 100 metros cuadrados, incluyendo los limites

seleccion = (datos['Area']>=60) & (datos['Area']<=100)
n3 = datos[seleccion]
n3

n3.shape[0]  #Frecuencia de veces que se repite alguna de las condiciones

#seleccione los inmuebles que tengan por lo menos 4 cuartos y alquiler menor que $2.000,00

seleccion = (datos['Cuartos']>=4) & (datos['Valor']<2000)
n4 = datos[seleccion]
n4

n4.shape[0]  #Frecuencia de veces que se repite alguna de las condiciones

print('Número de inmuebles clasificados como Departamento -> {}'.format(n1.shape[0]))
print('Número de inmuebles clasificados con tipos Casa, Casa en condominio y Casa de villa -> {}'.format(n2.shape[0]))
print('Número de inmuebles con area entre 60 y 100 metros cuadrados, incluyendo los limites  -> {}'.format(n3.shape[0]))
print('Número de inmuebles que tengan por lo menos 4 cuartos y alquiler menor que $2.000,00 -> {}'.format(n4.shape[0]))

