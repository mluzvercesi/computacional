
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
path = os.getcwd()
import copy


# ## Gamma matching
# Para redes de lado 6 y 128


N = 6 #hacer lo mismo para 128
filename = "\\ns_lado{:d}.txt".format(N)
df = pd.read_csv(path+filename,header=None,sep='\t',skiprows=1)

p_c = 0.5927
p = df.iloc[:,0].values
n_s = df.iloc[:,1:].values
s = np.array([i for i in range(df.values.shape[1]-1)])

m2 = np.zeros(len(p))
for i in range(len(m2)):
    m2[i] = np.nansum(n_s[i,:]*s**2)

plt.plot(p,m2)



N = 32 #hacer lo mismo para 128
filename = "\\ns_lado{:d}.txt".format(N)
df = pd.read_csv(path+filename,header=None,sep='\t',skiprows=1)

p_c = 0.5927
p = df.iloc[:,0].values
n_s = df.iloc[:,1:].values
s = np.array([i for i in range(df.values.shape[1]-1)])

m2 = np.zeros(len(p))
for i in range(len(m2)):
    m2[i] = np.nansum(n_s[i,:]*s**2)

plt.plot(p,m2)
plt.xlabel('p')
plt.ylabel('$m^2$')


---------------------------------------


# Obtengo un gamma para cada par de puntos consecutivos (de p-p_c)
# Falta separar en prob > p_c y prob < p_c, y se obtienen dos curvas gammas: gamma+ y gamma-
gamma = np.zeros(len(probs))
for i in range(len(probs)):
    coeffs = np.polyfit(np.log(abs(probs[i:i+1]-p_c)),np.log(m2[i:i+1]),1)
    gamma[i] = coeffs[0] #aca estan las dos curvas, faltaria separar en menos y mas


#hasta probs[25], probs[26] es la critica
gamma_mas = gamma[27:]
gamma_menos = gamma[1:26]
probs_mas = abs(probs[27:]-p_c)
probs_menos = abs(probs[1:26]-p_c)

plt.figure(figsize=([16,5]))
plt.subplot(1,2,1)
plt.plot(probs,m2,'.')
plt.xlabel('p')
plt.ylabel('$m_2$')
plt.subplot(1,2,2)
plt.plot(probs_mas,gamma_mas,'.r',label='$\gamma_+$')
plt.plot(probs_menos,gamma_menos,'.b',label='$\gamma_-$')
plt.xlabel('$|p-p_c|$')
plt.ylabel('$\gamma$')

