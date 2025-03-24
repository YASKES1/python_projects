import numpy as np

# гіперболічний тангенс
def f(x):
    return 2/(1 + np.exp(-x)) - 1
# похідна
def df(x):
    return 0.5 * (1 + x) * (1 - x)

W1 = np.array([[-0.2, 0.3, -0.4], [0.1, -0.3, -0.4]])
W2 = np.array([0.2, 0.3])

def go_forward(inp):
    sum = np.dot(W1, inp)
    out = np.array([f(x) for x in sum])

    sum = np.dot(W2, out)
    y = f(sum)
    return (y, out)

def train(epoch):
     global W2, W1
     lmd = 0.01             # крок навчання
     N = 10000              # кількість ітерацій при навчанні
     count = len(epoch)
     for k in range(N):
         x = epoch[np.random.randint(0, count)]     # випадковий вибір вхідного сигналу із навчальної вибірки
         y, out = go_forward(x[0:3])                # прямий прохід по нейромережі і обчислення вихідних значень нейромережі
         e = y - x[-1]                              # помилка
         delta = e * df(y)                          # локальний градієнт
         W2[0] = W2[0] - lmd * delta * out[0]       # корекція ваги першого зв'язку
         W2[1] = W2[1] - lmd * delta * out[1]       # корекція ваги другого зв'язку

         delta2 = W2 * delta * df(out)              # вектор із 2-х величин локальних градієнтів

         # корекція зв'язків першого шару

         W1[0, :] = W1[0, :] - np.array(x[0:3]) * delta2[0] * lmd
         W1[1, :] = W1[1, :] - np.array(x[0:3]) * delta2[1] * lmd

epoch = [(-1, -1, -1, -1),
         (-1, -1, 1, -1),
         (-1, 1, -1, -1),
         (-1, 1, 1, -1),
         (-1, -1, 1, 1),
         (1, 1, -1, -1),
         (1, 1, 1, -1)
         ]

train(epoch)

for x in epoch:
    y, out = go_forward(x[0:3])
    print(f': {y} => {x[-1]}')