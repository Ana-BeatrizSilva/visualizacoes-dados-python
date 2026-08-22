import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = x * 3.5

#definição dos eixos
plt.plot(x, y)
plt.xlabel ('Eixo X')
plt.ylabel('Eixo Y')

#título do gráfico
plt.title('Gráfico de Linha Simple s com Rótulos')

#mostrar visualização do gráfico
plt.show()