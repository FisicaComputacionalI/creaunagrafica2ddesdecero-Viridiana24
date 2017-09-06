import numpy as np
import pylab as plt
X=[0,1,2,3,4,5,6]
Y=[0,8,8.5,9,8.7,8.7,9.4]
plt.plot(X,Y)
plt.title("HISTORIA ACADEMICA")
plt.xlabel("Semestres")
plt.ylabel("Promedio Obtenido")
plt.grid(True)
plt.axis('tight')
plt.plot(X, Y, color="PURPLE", linewidth=2.0, linestyle="-",label="Promedios")
plt.plot(label="promedios")
plt.legend()
plt.savefig('graph.png')
plt.show()
