import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

#definição dos eixos
plt.plot(x, y, marker = 'o', linestyle = '-', label = 'Marcadores de Dados' )
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

#título do gráfico
plt.title('Gráfico de Linha Simples com Marcadores')

#mostrar visualização
plt.show()