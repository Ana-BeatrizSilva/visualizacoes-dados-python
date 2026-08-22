import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
y_seno = np.sin(x)
y_cosseno = np.cos(x)

plt.plot(x, y_seno, label="seno (x)")
plt.plot(x, y_cosseno, label="cosseno (x)")
plt.xlabel("Valores de X")
plt.ylabel("Valor Função")
plt.title("Funções Trigonométricas")
plt.legend()
plt.show()