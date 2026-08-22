import matplotlib.pyplot as plt

frutas = ['Maçãs', 'Laranjas', 'Uvas', 'Bananas']
total_vendas = [500, 350, 420, 450]

plt.bar(frutas, total_vendas, color='forestgreen')
plt.title('Vendas de Frutas')
plt.xlabel('Frutas')
plt.ylabel('Total de Vendas')

plt.show()