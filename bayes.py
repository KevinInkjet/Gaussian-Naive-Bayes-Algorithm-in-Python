import pandas as pd
import math
import numpy as np
from decimal import *
import statistics

datos = pd.read_csv("C:/Users/Owner/Documents/LCC/Machine Learning/Naive-bayes/playsport.csv") #Write here the path of the dataset

atributos = [feat for feat in datos]
atributos.remove("Class")

def valorReal(dataset, valor, item):
    newdataset = []
    for object in dataset[item]:
        if object == '?':
            object = 1
        newdataset.append(float(object))
    mean = statistics.mean(newdataset)
    var = np.var(newdataset)
    res = (1/( math.sqrt((2* math.pi * var)) ))*(math.e)**(-( ((float(valor)-mean)**2) /(2*var)))
    #res = 10
    return res

def bayes(datos, atributos):
    valores = []
    numeric = []
    #i = 0
    for item in atributos:
        bandera = True
        print("Give me the value of ", item)
        uniq = np.unique(datos[item])
        if (uniq[0].isnumeric() == False):
            try:
                Decimal(uniq[0])
            except InvalidOperation:
                print("Values: ", uniq)
                bandera = False
        numeric.append(bandera)
        dato = input("Ingresa: ")
        valores.append(dato)

    subdatapositivo = datos[datos["Class"] == "positive"]

    subdatanegativo = datos[datos["Class"] == "negative"] 

    #Conditional probabilities
    cantidadpositivos = []
    cantidadnegativos = []
    positivelist = []
    negativelist = []
    i = 0
    k = 0
    for item in atributos:
        if numeric[i] == False:
            for clase in np.unique(datos["Class"]):
                subdata1 = datos[datos[str(item)] == str(valores[i])]
                subdata = subdata1[subdata1["Class"] == clase] 
                if clase == "negative":
                    cantidadnegativos.append(len(subdata))
                    negativelist.append(len(subdata)/len(subdatanegativo))
                else:
                    cantidadpositivos.append(len(subdata))
                    positivelist.append(len(subdata)/len(subdatapositivo))
                    i = i + 1

        else: 
            for clase in np.unique(datos["Class"]):
                if clase == "negative":
                    entrega = valorReal(datos[datos["Class"] == "negative"], valores[i], item)
                    cantidadnegativos.append(entrega)
                    negativelist.append(entrega)
                else:
                    entrega = valorReal(datos[datos["Class"] == "positive"], valores[i], item)
                    cantidadpositivos.append(entrega)
                    positivelist.append(entrega)
                    i = i + 1

    probvalorobjetosi = len(subdatapositivo)/len(datos)
    probvalorobjetono = len(subdatanegativo)/len(datos)

    respos = probvalorobjetosi
    i = 0
    longitud = len(atributos)
    for i in range (0, longitud):
        if positivelist[i] == 0.0:
            positivelist[i] = 1
        else:    
            respos = respos * positivelist[i]
    print("The probability of being positive is: ", respos) 

    resneg = probvalorobjetono
    i = 0
    longitud = len(atributos)
    for i in range (0, longitud):
        if negativelist[i] == 0.0:
            negativelist[i] = 1
        else:
            resneg = resneg * negativelist[i]
    print("The probability of being negative is: ", resneg)

    if respos > resneg:
        print("More likely to be positive")
    else:
        print("More likely to be negative")

bayes(datos, atributos)
