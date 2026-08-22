import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = x * 2

plt.plot(x, y)
plt.title('Primeiro Gráfico de Linha')

plt.figure()
x1 = [2, 4, 6, 8, 10]
y1 = [3, 5, 7, 9, 11]

plt.plot(x1, y1, '-.')
plt.title('Segundo Gráfico de Linha')
plt.show()