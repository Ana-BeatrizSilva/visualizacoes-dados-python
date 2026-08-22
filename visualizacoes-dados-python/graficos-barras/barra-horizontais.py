import matplotlib.pyplot as plt

atletas = ['John', 'Paulo', 'Mathew', 'Sam']
pontuacoes = [120, 230, 340, 250]

plt.barh(atletas, pontuacoes, height = 0.3)

plt.title('Pontuações dos Atletas')
plt.xlabel('Pontuações')
plt.ylabel('Atletas')

plt.show()