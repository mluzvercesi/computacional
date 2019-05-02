import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

"""
Primero, armamos la tabla de n(s). Una vez que la tenemos, buscamos qué probabilidad maximiza n(s) para cada s, y la llamamos p_max.

Para armar la tabla, hace muchos loops:
el primero (en s y en l), me devuelve mil tablas n_s, una para cada medición con la misma probabilidad.
El siguiente, en j, barre en todo el archivo. El if se asegura de elegir la primera probabilidad diferente, de modo tal que los 1000 j siguientes sean todos correspondientes a la misma probabilidad.

z = s^sigma * epsilon, donde sigma=36/91 sale de la tabla, epsilon es (pmax-pc)

"""

datos = np.loadtxt('ej4.txt', skiprows=1)
#C0 la proba; C1 - C(N*N/2) tamaño de cluster de cada número en orden 0 1 2 3...;  C(N*N/2+1) - C(N*N/2+1 + N/2) etiquetas cluster percolante.

N = 64
pc =  0.5919
probabilidad = datos[:,0]
cluster_size = datos[:,3:int(N*N/2)]

col = int(len(probabilidad)/1000)
ns_total = np.zeros((15,col))
for j in range(len(probabilidad)): #loop en todo el archivo
    if probabilidad[j] != probabilidad[j-1]: #que lo haga sólo en los casos en los cuales la proba es la misma
        n_s = np.zeros((15, 1000))
        for l in range(1000):
            for s in range(15):
                n = np.count_nonzero(cluster_size[j+l, :] == s) #j va a ser 0, 1000, 2000, etc (porque es el que me deja el if). Luego, le suma los l.
                n_s[s,l] = n
            #esto ahora me devolvería un array de 15x1000, donde cada columna corresponde a una nueva medicion.
        ns_medio = np.mean(n_s, axis=1) #ahora, promedia sobre las mil mediciones.
    ns_total[:, int(j/1000)] = ns_medio #me devuelve un array 2D de 15x100 donde cada columna corresponde a una probabilidad. Esta es la tabla que dibujamos siempre (si bien la dibujamos en general traspuesta, con las probabilidades como filas y los s como columnas)

proba = np.linspace(0,1, 101)
idx_max = np.zeros(15)
ns_max = np.zeros(15)
p_max = np.zeros(15)

#referencia:
# s = ns_total[j,:]
# p = ns_total[:,j]

for s in range(2,15): #s fijo: las filas (axis 0) fijas
    idx_max[s] = np.where(ns_total[s, :] == max(ns_total[s,:]))[0][0]
    ns_max[s] = ns_total[s, int(idx_max[s])]
    p_max[s] = proba[int(idx_max[s])]
# print(idx_max, ns_max, p_max)

epsilon = np.abs(p_max - pc)
sigma = 36/91
tau = 1.7


for s in range(2,15):
    ns_pc = s**-tau
    z = s**sigma * (proba[1:]-pc)
    fz = ns_total[s,:]/ns_pc
    plt.plot(z, fz, label='{}'.format(s))

plt.xlabel('z')
plt.ylabel('f(z)')
plt.title(r'Función de scaling para distintos $s$')
plt.legend()
plt.show()
# for x in range(15):
#     fz[:,x] = ns_total[:,x]/ns_pc
# for x in range(15):
#     plt.plot(z, fz[:,x], label='{}'.format(size))


#ej 5
"""
Ej 5: primero, grafico la proba y la densidad. nos da bien.
Una vez que tenemos esta forma, usamos p_max que calculamos antes.
Graficamos entonces en escala loglog epsilon vs s, la pendiente de la recta será el sigma.
La variable ajuste_teo es para comparar cuán bien ajusta el valor teórico.
"""

Y = np.log10(epsilon[2:])
X = np.log10(size[2:])
slope, intercept, r_value, p_value, std_err = stats.linregress(X, Y)
line = slope*X + intercept
ajuste_teo = -sigma * X - 0.319

plt.figure()
for s in range(2,15):
    plt.plot(proba[1:], ns_total[s,:]/np.linalg.norm(ns_total, axis=0), label='s = {}'.format(s))
    plt.xlabel(r'Probabilidad de ocupación $p$')
    plt.ylabel(r'Densidad de clusters $n_s$')
    plt.title(r'Densidad de clusters en función de la probabilidad de ocupación $n_s(p)$ para distintos tamaños $s$')
    plt.legend()

plt.figure()
plt.scatter(np.log10(size[2:]), np.log10(epsilon[2:]))
plt.plot(X, line, c='r', label=r'$\sigma$ = {0:1.3g}, b = {1:1.3g}'.format(slope, intercept))
# plt.plot(X, ajuste_teo)
plt.xlabel(r'Tamaño de clusters $s$')
plt.ylabel(r'$\epsilon = |p_{max} - p_c|$')
plt.title(r'$\epsilon(s)$ en escala logarítmica')
plt.legend()
plt.show(block=False)
