"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re


def ingest_data():
    
    dic={'cluster':[], 'cantidad_de_palabras_clave':[], 'porcentaje_de_palabras_clave':[], 'principales_palabras_clave':[]}
    columns = ['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave']

    with open('clusters_report.txt') as report:
        filas = report.readlines()
    # No me sirven las 4 primeras filas del txt
        filas = filas[4:]
        concatenar=""

        for fila in filas:    

            fila= fila.split()

            #Si la fila esta vacía significa que se haya la siguiente fila    
            if fila == []:
                #Se separa cada uno de los patrones
                aux=re.findall(r"(\s+\d+,\d %)|(\s*\d+)|(\s*([\w+\s]|[/$&+:,;=?@#|'<>^*()%!-])*)",concatenar)

                #Se tomada cada una de las columnas
                for i in range(0,4):
                    #Se concatenas los valores dado a que contiene valor ''
                    valor="".join(aux[i][:-1])
                    #Si es el porcentaje se elimina los caracteres especiales y se cambia el punto por decimal
                    if i == 2:
                        valor= valor.replace(",",".").replace(" %","")
                    #Si es el texto largo, se elimina el espacio inicial y se organizan las comas para queden palabra, palabra
                    elif i == 3:
                        valor= re.sub("^\s","",valor)
                        valor= re.sub(r"([\w?'<>^*()%!-])(,)(\w)",r"\1\2 \3",valor)
                    #Se añade el valor al diccionario 
                    dic[columns[i]].append(valor)
                #Se reinicia la fila
                concatenar=""
            else:
                #Se concatenan todos los valores de las filas
                concatenar+= " "+" ".join(fila)

    df=pd.DataFrame(dic)
    #Se pasan a valores numericos
    df["cluster"]=pd.to_numeric(df["cluster"])
    df["cantidad_de_palabras_clave"]=pd.to_numeric(df["cantidad_de_palabras_clave"])
    df["porcentaje_de_palabras_clave"]= pd.to_numeric(df['porcentaje_de_palabras_clave'])
    return df
