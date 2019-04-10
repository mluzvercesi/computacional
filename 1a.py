import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from matplotlib.mlab import normpdf



proba = {}

for L in [4, 16, 32, 64]:#, 128]:
    proba[L] = np.loadtxt('proba_lado_{}.txt'.format(L))
    plt.figure()
    plt.plot()
    n, bins, patches = plt.hist(proba[L], 50, normed = True, alpha=0.5)
    (mu, sigma) = norm.fit(proba[L])
    y = normpdf(bins, mu, sigma)
    plt.plot(bins, y)
    plt.title('Histograma de la probabilidad para redes con L = {}'.format(L))
    plt.xlabel('Probabilidad')
    plt.ylabel('Cuentas')

    print('La probabilidad para una red de lado L = {0:1.4g} es P = {1:1.4g} +- {2:1.4g}'.format(L, mu, sigma))

plt.show()
