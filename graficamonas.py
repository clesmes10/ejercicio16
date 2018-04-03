import numpy as np
import matplotlib.pyplot as plt

datosalbum = np.loadtxt("resalbum.txt")

nlaminas= datosalbum[:,0]
nrepetidas = datosalbum[:,1]
ntiempo = np.linspace(0, 159, 160) 


plt.plot(ntiempo, nlaminas, "c")
plt.plot(ntiempo, nrepetidas, "b")
plt.savefig("graficamona.pdf")
