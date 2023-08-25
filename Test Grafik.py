from cProfile import label
from cmath import log, log10
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace (-3, 3, 100)
y1 = np.power (x, 2)
y2 = x
y3 = np.power (x, 3)
y4 = np.power (x, 0)
y5 = np.power (2, x)

plt.plot (x, y1, "r", label="y = x^2")
plt.plot (x, y2, "b", label="y = x")
plt.plot (x, y3, "g", label="y = x^3")
plt.plot (x, y4, "black", label="y = 1")
plt.plot (x, y5 , "purple", label="y = 2^x")

plt.ylim(-3, 3)

plt.grid ()
plt.title("Grafik Fungsi")

plt.legend(loc="best")

plt.show ()