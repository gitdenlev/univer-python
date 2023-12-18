import matplotlib.pyplot as plt
import numpy as np

# Функції
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = x**0.15

# Фігура
fig = plt.figure()

# Панелі
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

# Графіки
ax1.plot(x, y1, color='black')
ax2.plot(x, y2, '--', color='black')
ax3.plot(x, y3, color='gray')

# Діапазони значень по осях
for ax in [ax1, ax2, ax3, ax4]:
    ax.set_xlim([0, 2*np.pi])
    ax.set_ylim([min(min(y1), min(y2), min(y3)), max(max(y1), max(y2), max(y3))])

# Текстові мітки
ax1.text(0.5, 1.05, '(а)', transform=ax1.transAxes, ha='center')
ax2.text(0.5, 1.05, '(б)', transform=ax2.transAxes, ha='center')
ax3.text(0.5, 1.05, '(в)', transform=ax3.transAxes, ha='center')
ax4.text(0.5, 1.05, '(г)', transform=ax4.transAxes, ha='center')

# Відображення малюнка
plt.show()
