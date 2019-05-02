
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
path = os.getcwd()
import copy as copy


# ----Gamma matching----
# Para redes de lado 6 y 128


N = 128 #hacer lo mismo para 128
cant_prob = 1
str_start = "etiquetas_cluster_size_lado{:d}".format(N)
s = np.asarray([i for i in range(1,16)]) #tamaño de clusters del 1 al 15
n_s = np.zeros([len(s),cant_prob]) #cantidad de clusters de cada tamaño del 1 al 15
probs = np.zeros(cant_prob)
m2 = np.zeros(cant_prob) #momento de orden 2
p_c = 0.5927

for m in range(cant_prob):
    N_S = np.zeros([10000,len(s)])
    l = 0 # contador de probabilidades
    for filename in os.listdir(path):
        if filename.startswith(str_start):
            df = pd.read_csv(filename,header=None,sep='\t',skiprows=1)

            probs[m] = float(filename.split("_")[-1].replace("p","").replace(".txt",""))
            # probabilidad sacada del nombre del archivo

            nfilas = df.values.shape[0]
            ncols = df.values.shape[1]
            nclusters = int(N*N/2) # De col 0 a L*L/2 son tamaños de cluster (contamos ceros)

            # me quedo con cluster size para cada etiqueta de cluster
            clusters = df.iloc[:,1:nclusters] #a partir de 1 para que no considere los 0s que son sitios vacios
            clusters = clusters.values
            for j in range(nfilas):
                for i in range(len(s)):
                    N_S[j,i] = (clusters[j,:]==s[i]).sum() # devuelve la cantidad de clusters de tamaño s para cada iteracion
            l = l+1

    for k in range(len(s)):
        n_s[k,m] = np.mean(N_S[:,k])

    m2[m] = sum(n_s[:,m]*s**2)



#hace falta hacer esto? para no contar 0s
N_S_nan = copy.deepcopy(N_S)
N_S_nan[N_S_nan == 0] = np.nan
n_s_nan = np.zeros(len(s))
for k in range(len(s)):
    n_s_nan[k] = np.nanmean(N_S_nan[:,k])


# Obtengo un gamma para cada par de puntos consecutivos (de p-p_c)
# Falta separar en prob > p_c y prob < p_c, y se obtienen dos curvas gammas: gamma+ y gamma-
gamma = np.zeros(len(probs))
for i in range(len(probs)):
    coeffs = np.polyfit(np.log(abs(probs[i:i+1]-p_c)),np.log(m2[i:i+1]),1)
    gamma[i] = coeffs[0] #aca estan las dos curvas, faltaria separar en menos y mas
