import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = x * 2
y1 = [3, 5, 7, 9, 11]

plt.plot(x, y, label='y = 2x')
plt.plot(x, y1, '-.', label='y1')
plt.fill_between(x, y, y1, color='green', alpha=0.4)

plt.xlabel("Dados Eixo X")
plt.ylabel("dados Eixo X")
plt.title("Preenchimento de Área entre Duas Linhas")
plt.legend()
plt.show()