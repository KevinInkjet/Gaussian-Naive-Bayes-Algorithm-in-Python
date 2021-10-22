import pandas as pd
import math
import numpy as np
from decimal import *
import statistics

datos = pd.read_csv("C:/Users/Owner/Documents/LCC/Machine Learning/Naive-bayes/Hipotiroidismo.csv")
#datos = pd.read_csv("C:/Users/Owner/Documents/LCC/Machine Learning/Naive-bayes/playsport.csv")

atributos = [feat for feat in datos]
atributos.remove("Class")

def valorReal(dataset, valor, item):
    #print("oK")
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

    #print(len(valores))
    #print(numeric)

    #Calcular la probabilidad del valor objetivo "positivo"
    subdatapositivo = datos[datos["Class"] == "positive"] #Subdata de sólo los valores donde la clase da positivo
    #print(len(subdatapositivo))

    #Calcular la probabilidad del valor objetivo "negativo"
    subdatanegativo = datos[datos["Class"] == "negative"] #Subdata de sólo los valores donde la clase da negativo
    #print(len(subdatanegativo))
    #print(len(datos))
    #print(np.unique(datos["Class"]))

    #Probabilidades condicionales
    cantidadpositivos = []
    cantidadnegativos = []
    positivelist = []
    negativelist = []
    i = 0
    k = 0
    for item in atributos:
        if numeric[i] == False:
            for clase in np.unique(datos["Class"]):
                print("Clase ", clase, " en ", item)
                #subdata1 = datos[datos["Class"] == clase]
                subdata1 = datos[datos[str(item)] == str(valores[i])]
                subdata = subdata1[subdata1["Class"] == clase] #La longitud de subdata guarda la cantidad de items donde el valor introducido es igual a positive/negative
                if clase == "negative":
                    cantidadnegativos.append(len(subdata))
                    negativelist.append(len(subdata)/len(subdatanegativo))
                else:
                    cantidadpositivos.append(len(subdata))
                    positivelist.append(len(subdata)/len(subdatapositivo))
                    i = i + 1
                #print(len(subdata))
            #print("Total en ese valor de item: ", len(subdata1)) #La longitud de subdata1 guarda la cantidad de datos donde el item es igual al valor introducido

        else: #Si el item tiene valores reales
            #print("Valor falso")
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
    #print(cantidadnegativos)
    #print(cantidadpositivos)

    #print("Subdatas positivos: ", len(subdatapositivo))
    #print("Subdatas negativos: ", len(subdatanegativo))

    probvalorobjetosi = len(subdatapositivo)/len(datos)
    probvalorobjetono = len(subdatanegativo)/len(datos)

    #print("Len datos: ", len(datos))

    #Probabilidad de positive
    #print("PROBABILIDAD POSITIVA")
    respos = probvalorobjetosi
    #print("respos: ", respos)
    i = 0
    longitud = len(atributos)
    #print(positivelist)
    for i in range (0, longitud):
        if positivelist[i] == 0.0:
            positivelist[i] = 1
        else:    
            respos = respos * positivelist[i]
    print("La probabilidad de que sea positivo es: ", respos) #!Importante

    #Probabilidad de negative
    resneg = probvalorobjetono
    i = 0
    longitud = len(atributos)
    for i in range (0, longitud):
        if negativelist[i] == 0.0:
            negativelist[i] = 1
        else:
            resneg = resneg * negativelist[i]
    print("La probabilidad de que sea negativo es: ", resneg) #!Importante

    if respos > resneg:
        print("Es más probable que sea positivo")
    else:
        print("Es más probable que sea negativo")

bayes(datos, atributos)