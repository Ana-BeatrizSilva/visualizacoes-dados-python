import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.figure(figsize=(8, 6))
plt.plot(x, y, marker = 'o', linestyle = '-')

for xi, yi in zip(x, y):
     plt.annotate(f'({xi}, {yi})',
                 (xi, yi),
                 textcoords="offset points",
                 xytext=(0, 10),
                 ha='center')

plt.grid(True)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Gráfico de Linha Simples com Anotações')

plt.show()