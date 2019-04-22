import numpy as np
from scipy.stats import norm
from matplotlib.mlab import normpdf
import matplotlib.pyplot as plt


datos = np.loadtxt('proba_lado.txt', skiprows=1) #la primera columna es el tamaño de la red

proba_4 = datos[0,1:]
proba_16 = datos[1,1:]
proba_32 = datos[2,1:]
proba_64 = datos[3,1:]
proba_128 = datos[4,1:]


lado = np.array([4,16,32,64,128])
probabilidades_criticas = np.array([np.mean(proba_4),np.mean(proba_16), np.mean(proba_32), np.mean(proba_64), np.mean(proba_128)])

print('los valores medios son: \n p_4 = {0:1.4g} \n p_16 = {1:1.4g} \n p_32 = {2:1.4g} \n p_64 = {3:1.4g} \n p_128 = {4:1.4g}'.format(np.mean(proba_4),np.mean(proba_16),np.mean(proba_32),np.mean(proba_64),np.mean(proba_128)))

plt.figure()
plt.axhline(y = 0.5927, color='red', linestyle='--')
plt.scatter(lado, probabilidades_criticas)
plt.ylabel(r'$P_c$')
plt.xlabel('Tamaño de la red')
plt.title(r'$P_c$ en función del tamaño de la red según el método de bisección')


plt.figure()
ax1 = plt.subplot(511)
n, bins, patches = plt.hist(proba_4, 50, normed = True, alpha=0.5)
(mu_4, sigma_4) = norm.fit(proba_4)
y = normpdf(bins, mu_4, sigma_4)
plt.plot(bins, y)
plt.setp(ax1.get_xticklabels(), visible=False)
ax1.set_title('Histograma de la probabilidad para distintos tamaños de red')
ax1.set_ylabel('L = 4')

ax2 = plt.subplot(512, sharex=ax1)
n, bins, patches = plt.hist(proba_16, 50, normed = True, alpha=0.5)
(mu_16, sigma_16) = norm.fit(proba_16)
y = normpdf(bins, mu_16, sigma_16)
plt.plot(bins, y)
plt.setp(ax2.get_xticklabels(), visible=False)
ax2.set_ylabel('L = 16')

ax3 = plt.subplot(513, sharex=ax1)
n, bins, patches = plt.hist(proba_32, 50, normed = True, alpha=0.5)
(mu_32, sigma_32) = norm.fit(proba_32)
y = normpdf(bins, mu_32, sigma_32)
plt.plot(bins, y)
plt.setp(ax3.get_xticklabels(), visible=False)
ax3.set_ylabel('L = 32')

ax4 = plt.subplot(514, sharex=ax1)
n, bins, patches = plt.hist(proba_64, 50, normed = True, alpha=0.5)
(mu_64, sigma_64) = norm.fit(proba_64)
y = normpdf(bins, mu_64, sigma_64)
plt.plot(bins, y)
plt.setp(ax4.get_xticklabels(), visible=False)
ax4.set_ylabel('L = 64')

ax5 = plt.subplot(515, sharex=ax1)
n, bins, patches = plt.hist(proba_128, 50, normed = True, alpha=0.5)
(mu_128, sigma_128) = norm.fit(proba_128)
y = normpdf(bins, mu_128, sigma_128)
plt.plot(bins, y)
ax5.set_ylabel('L = 128')

plt.xlabel('Probabilidad')

sigma = np.array([sigma_4,sigma_16, sigma_32, sigma_64, sigma_128])

plt.figure()
plt.scatter(lado, sigma)
plt.ylabel('Dispersión')
plt.xlabel('Tamaño de la red')
plt.grid()
plt.title(r'Dispersión de $P_c$ en función del tamaño de la red')





plt.show()
