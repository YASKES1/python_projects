import time
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x*x - 5 * x + 5

def df(x):
    return 2 * x - 5


N = 20      # КІЛЬКІСТЬ ІТЕРАЦІЙ
xx = 0      # початкове значення
lmd = 0.3   # крок збіжності

x_plt = np.arange(0, 5.0, 0.1)
f_plt = [f(x) for x in x_plt]

plt.ion()  # включення інтерактивного режима відображення графіки
fig, ax = plt.subplots()    # створення вікра і осей графіка
ax.grid(True)   # відображення сітки на графіку

ax.plot(x_plt, f_plt)           #відображення параболи
point = ax.scatter(xx, f(xx), c="red")

mn=100

for i in range(N):
    lmd = 1 / min(i+1, mn)
    xx = xx - lmd*np.sign(df(xx))  # формула градієнтного спуску

    point.set_offsets([xx, f(xx)])

    fig.canvas.draw()
    fig.canvas.flush_events()
    time.sleep(0.02)

plt.ioff()
print(xx)
ax.scatter(xx, f(xx), c="blue")
plt.show()
