import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

"""
Calcule la probabilidad de aparicion del cluster percolante F(p)dp cuando p∈[p,p+dp].
Estime pc(L) como el valor de p para el cual la red percola al menos la mitad de las veces.
Compare con el metodo anterior.

Estudie como se comporta la dispersion de los valores obtenidos en los puntos anteriores para pc, en funcion del tamano del sistema.
"""

datos_4 = np.loadtxt('proba_percola_lado_4.txt', skiprows=1)
datos_16 = np.loadtxt('proba_percola_lado_16.txt', skiprows=1)
datos_32 = np.loadtxt('proba_percola_lado_32.txt', skiprows=1)
datos_64 = np.loadtxt('proba_percola_lado_64.txt', skiprows=1)
datos_128 = np.loadtxt('proba_percola_lado_128.txt', skiprows=1)

proba_poblar_4 = datos_4[:,0]
proba_percolar_4 = np.mean(datos_4[:,1:], axis=1) #promedia sobre la cantidad de veces que percola el sistema, para cada probabilidad

proba_poblar_16 = datos_16[:,0]
proba_percolar_16 = np.mean(datos_16[:,1:], axis=1)

proba_poblar_32 = datos_32[:,0]
proba_percolar_32 = np.mean(datos_32[:,1:], axis=1)

proba_poblar_64 = datos_64[:,0]
proba_percolar_64 = np.mean(datos_64[:,1:], axis=1)

proba_poblar_128 = datos_128[:,0]
proba_percolar_128 = np.mean(datos_128[:,1:], axis=1)

slope, intercept, r_value, p_value, std_err = stats.linregress(proba_poblar_4[10:100],proba_percolar_4[10:100])
line = slope*proba_poblar_4+intercept
#la proba es 0.5 en donde line = 0.5
aparicion_percolante_4 = (0.5-intercept)/slope

slope, intercept, r_value, p_value, std_err = stats.linregress(proba_poblar_16[10:100],proba_percolar_16[10:100])
line = slope*proba_poblar_16+intercept
aparicion_percolante_16 = (0.5-intercept)/slope

slope, intercept, r_value, p_value, std_err = stats.linregress(proba_poblar_32[10:100],proba_percolar_32[10:100])
line = slope*proba_poblar_32+intercept
aparicion_percolante_32 = (0.5-intercept)/slope

slope, intercept, r_value, p_value, std_err = stats.linregress(proba_poblar_64[10:100],proba_percolar_64[10:100])
line = slope*proba_poblar_64+intercept
aparicion_percolante_64 = (0.5-intercept)/slope

slope, intercept, r_value, p_value, std_err = stats.linregress(proba_poblar_128[10:100],proba_percolar_128[10:100])
line = slope*proba_poblar_128+intercept
aparicion_percolante_128 = (0.5-intercept)/slope

print('El percolante aparece en: \n {} para L = 4 \n {} para L = 16 \n {} para L = 32 \n {} para L = 64 \n {} para L = 128 \n'.format(aparicion_percolante_4,aparicion_percolante_16,aparicion_percolante_32,aparicion_percolante_64,aparicion_percolante_128))

#ahora que tenemos p_c, queremos hallar la desviación.

def find_nearest(array,value):
    idx = (np.abs(array-value)).argmin() #argmin me da el valor del minimo en el array
    return array[idx]

indice = np.where(proba_percolar_4 == find_nearest(proba_percolar_4,aparicion_percolante_4))[0][0] #este es el índice de la proba de ocupación más cercana a la critica. Queremos hallar la stdev en este índice.
datos_4[indice, 1:]

# plt.plot(proba_poblar_4,proba_percolar_4, label='L = 4')
# plt.plot(proba_poblar_4,line)
# plt.plot(proba_poblar_16,proba_percolar_16, label='L = 16')
# plt.plot(proba_poblar_32,proba_percolar_32, label='L = 32')
# plt.plot(proba_poblar_64,proba_percolar_64, label='L = 64')
# plt.plot(proba_poblar_128,proba_percolar_128, label='L = 128')
# plt.legend()
# plt.grid()
# plt.xlim(0,1)
# plt.xlabel('Probabilidad de ocupación')
# plt.ylabel('Probabilidad de percolación')
#
# plt.show()
