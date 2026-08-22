import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = x * 5

x1 = [2, 4, 6, 8, 10]
y1 = [3, 6, 9, 12, 15]

plt.plot(x, y, label = 'y = x * 5')
plt.plot(x1, y1, '-.', label = 'Segunda Linha')

plt.xlabel('Dados do Eixo X')
plt.ylabel('Dados do Eixo Y')
plt.title('Múltiplos Gráficos de Linha no mesmo Eixo')
plt.legend()

plt.show()