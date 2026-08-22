import numpy as np
import matplotlib.pyplot as plt

N = 5

vendas_online = (20, 35, 30, 35, 27)
vendas_loja = (25, 32, 34, 20, 25)
erro_online = (2, 3, 4, 1, 2)
erro_loja = (3, 5, 2, 3, 3)

equipes = np.arange(N)

largura = 0.35
fig = plt.subplots(figsize=(10, 7))

p1 = plt.bar(
    equipes,
    vendas_online,
    largura,
    yerr=erro_online
)
p2 = plt.bar(
    equipes,
    vendas_loja,
    largura,
    bottom=vendas_online,
    yerr=erro_loja
)

plt.ylabel('Quantidade de vendas')
plt.title('Vendas por equipe')

plt.xticks(
    equipes,
    ('Equipe 1', 'Equipe 2', 'Equipe 3', 'Equipe 4', 'Equipe 5')
)
plt.yticks(np.arange(0, 81, 10))

plt.legend(
    (p1[0], p2[0]),
    ('Vendas online', 'Vendas na loja')
)
plt.show()