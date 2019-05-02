import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

"""
Tenemos archivos para cada probabilidad con 60k iteraciones, contando cantidad de elementos en cada etiqueta de cluster. Primero: contar cantidad de clusters de cada tamaño (n_s). Promediar n_s en las 60k iteraciones), para cada cluster size s. (Nota: s maximo es N*N). Obtenemos una tabla con los tamaños medios <n_s>, para distintas probabildiades.
"""

#Lado 64

datos_585 = np.loadtxt('datos/etiquetas_p0585_L64.txt', skiprows=1)
datos_59 = np.loadtxt('datos/etiquetas_p059_L64.txt', skiprows=1)
datos_595 = np.loadtxt('datos/etiquetas_p0595_L64.txt', skiprows=1)
datos_60 = np.loadtxt('datos/etiquetas_p060_L64.txt', skiprows=1)

#C0 - C(N*N/2-1) tamaño de cluster de cada número en orden 0 1 2 3...;  C(N*N/2) - C(N*N/2 + N/2-1) etiquetas cluster percolante. Para N = 64: es C0 a C7 y luego C8 a C11. Como en realidad nos importa a partir de la eitqueta 2, contamos C2 a C7.

N = 64
cluster_size_585 = datos_585[:,2:int(N*N/2-1)]
cluster_size_59 = datos_59[:,2:int(N*N/2-1)]
cluster_size_595 = datos_595[:,2:int(N*N/2-1)]
cluster_size_60 = datos_60[:,2:int(N*N/2-1)]


max_585 = int(np.amax(cluster_size_585))#obtengo el tamaño de cluster más grande
cuenta_585 = np.zeros(max_585+1)

#ahora este for me va a devolver cuántas veces aparece un cluster de tamaño i. Empieza contando desde cero.
for i in range(0,max_585+1):
    a_585 = np.count_nonzero(cluster_size_585 == i)
    cuenta_585[i] = a_585

max_59 = int(np.amax(cluster_size_59))#obtengo el tamaño de cluster más grande
cuenta_59 = np.zeros(max_59+1)

for i in range(0,max_59+1):
    a_59 = np.count_nonzero(cluster_size_59 == i)
    cuenta_59[i] = a_59


max_595 = int(np.amax(cluster_size_595))
cuenta_595 = np.zeros(max_595+1)

for i in range(0,max_595+1):
    a_595 = np.count_nonzero(cluster_size_595 == i)
    cuenta_595[i] = a_595


max_60 = int(np.amax(cluster_size_60))#obtengo el tamaño de cluster más grande
cuenta_60 = np.zeros(max_60+1)

for i in range(0,max_60+1):
    a_60 = np.count_nonzero(cluster_size_60 == i)
    cuenta_60[i] = a_60

Y_595 = cuenta_595[2:62]
Y_norm595 = Y_595/np.linalg.norm(Y_595)
X595 = np.log10(range(2,max_595+1))
slope595, intercept595, r_value595, p_value595, std_err595 = stats.linregress(X595[:60],np.log10(Y_norm595[:60]))
line595 = slope595*X595[:60]+intercept595

Y_585 = cuenta_585[2:62]
Y_norm585 = Y_585/np.linalg.norm(Y_585)
X585 = np.log10(range(2,max_585+1))
slope585, intercept585, r_value585, p_value585, std_err585 = stats.linregress(X585[:60],np.log10(Y_norm585[:60]))
line585 = slope585*X585[:60]+intercept585

Y_59 = cuenta_59[2:62]
Y_norm59 = Y_59/np.linalg.norm(Y_59)
X59 = np.log10(range(2,max_59+1))
slope59, intercept59, r_value59, p_value59, std_err59 = stats.linregress(X59[:60],np.log10(Y_norm59[:60]))
line59 = slope59*X59[:60]+intercept59

Y_60 = cuenta_60[2:62]
Y_norm60 = Y_60/np.linalg.norm(Y_60)
X60 = np.log10(range(2,max_60+1))
slope60, intercept60, r_value60, p_value60, std_err60 = stats.linregress(X60[:60],np.log10(Y_norm60[:60]))
line60 = slope60*X60[:60]+intercept60

plt.figure()
plt.scatter(X585[0:60], np.log10(Y_norm585), label='P = 0.585')
plt.scatter(X59[0:60], np.log10(Y_norm59), label='P = 0.590')
plt.scatter(X595[0:60], np.log10(Y_norm595), label='P = 0.595')
plt.scatter(X60[0:60], np.log10(Y_norm60), label='P = 0.600')
plt.plot(X585[0:60],line585, color='C1', label = r'$\tau$ ={0:1.3g}, b ={1:1.3g} '.format(slope585, intercept585))
plt.plot(X59[0:60],line59, color='C2', label = r'$\tau$ ={0:1.3g}, b ={1:1.3g} '.format(slope59, intercept59))
plt.plot(X595[:60],line595, color='C0', label = r'$\tau$ ={0:1.3g}, b ={1:1.3g} '.format(slope595, intercept595))
plt.plot(X60[0:60],line60, color='C3', label = r'$\tau$ ={0:1.3g}, b ={1:1.3g} '.format(slope60, intercept60))
plt.legend()
plt.title('Distribución de los clusters para una red con L=64 en escala logarítmica')
plt.xlabel(r'Tamaño de clusters $s$')
plt.ylabel(r'Densidad de clusters $n(s)$')

plt.show(block=False)

frac585 =0
for i in range(len(line585)):
    num = (np.log10(Y_norm585)[i] - line585[i])**2
    den = np.abs(line585[i])
    frac585 += num/den

frac59 =0
for i in range(len(line59)):
    num = (np.log10(Y_norm59)[i] - line59[i])**2
    den = np.abs(line59[i])
    frac59 += num/den

frac595 =0
for i in range(len(line595)):
    num = (np.log10(Y_norm595)[i] - line595[i])**2
    den = np.abs(line595[i])
    frac595 += num/den

frac60 =0
for i in range(len(line60)):
    num = (np.log10(Y_norm60)[i] - line60[i])**2
    den = np.abs(line60[i])
    frac60 += num/den


print('m_585 = {0}, b_585 = {1}, chi={2}'.format(slope585, intercept585,frac585))# stats.chisquare(np.log10(Y_norm585), line585)))
print('m_59 = {0}, b_59 = {1}, chi={2}'.format(slope59, intercept59, frac59))#stats.chisquare(np.log10(Y_norm59), line59)))
print('m_595 = {0}, b_595 = {1}, chi={2}'.format(slope595, intercept595, frac595))#stats.chisquare(np.log10(Y_norm595), line595)))
print('m_60 = {0}, b_60 = {1}, chi={2}'.format(slope60, intercept60, frac60))#stats.chisquare(np.log10(Y_norm60), line60)))
