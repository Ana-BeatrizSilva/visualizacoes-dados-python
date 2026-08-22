import matplotlib.pyplot as plt
import numpy as np

barWidth = 0.25

fig = plt.subplots(figsize=(12, 9))

Lucro = [12, 20, 25, 1, 10, 6]
Receita = [30, 15, 8, 14, 45, 5]
Despesas = [2, 24, 18, 20, 32, 14]

br1 = np.arange(len(Lucro))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]

plt.bar(br1, Lucro, color='r', width=barWidth,
        edgecolor='grey', label='Lucro')
plt.bar(br2, Receita, color='g', width=barWidth,
        edgecolor='grey', label='Receita')
plt.bar(br3, Despesas, color='b', width=barWidth,
        edgecolor='grey', label='Despesas')

plt.xlabel('Períodos Anuais', fontweight='bold', fontsize=15)
plt.ylabel('Valores', fontweight='bold', fontsize=13)

plt.xticks(
    [r + barWidth for r in range(len(Lucro))],
    ['2021', '2022', '2023', '2024', '2025', '2026']
)

plt.legend()
plt.show()