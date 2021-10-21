import pandas as pd
import numpy as np
from decimal import *

datos = pd.read_csv("C:/Users/Owner/Documents/LCC/Machine Learning/Naive bayes/Hipotiroidismo.csv")
atributos = [feat for feat in datos]
atributos.remove("Class")

def bayes(datos, atributos):
    '''
    print("programa")
    print(datos)
    subdata = datos[datos["Class"] == "negative"] #Subdata de todos los datos donde la Class sea negativa
    print(subdata["age"]) #Imprime sólo los datos de la variable age del conjunto de datos
    print(subdata["age"][0]) #Imprime el primer valor de la variable age del conjunto de datos
    '''
    valores = []
    numeric = []
    #i = 0
    for item in atributos:
        bandera = True
        print("Dame el valor de ", item)
        uniq = np.unique(datos[item])
        if (uniq[0].isnumeric() == False):
            try:
                Decimal(uniq[0])
            except InvalidOperation:
                print("Valores: ", uniq)
                #print("Es decimal o número")
                bandera = False
        numeric.append(bandera)
        dato = input("Ingresa: ")
        valores.append(dato)
        #i = i + 1

    print(len(valores))
    print(numeric)


bayes(datos, atributos)