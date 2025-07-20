# нейросеть урок https://www.youtube.com/watch?v=VqChpNNYZ8Q&list=PLA0M1Bcd0w8yv0XGiF1wjerjSZVSrYbjh&index=2

# простая нейросеть определения симпатии девушки по параметрам
                          #есть квартира, слушает рок, красивый


import numpy as np

def act(x):
    return 0 if x < 0.5 else 1

def go(house, rock, attr):
    x = np.array([house, rock, attr])
    w11 = [0.3, 0.3, 0]  # веса первого нейрона
    w12 = [0.4, -0.5, 1]  # веса второго нейрона
    weight1 = np.array([w11, w12])  # матрица 2х3
    weight2 = np.array([-1, 1])     # вектор 1х2

    sum_hidden = np.dot(weight1, x) # сума на входах нейронов скрытого слоя
    # np.dot - скалярний добуток вектора
    print("сумма на нейронах скрытого слоя: " +str(sum_hidden))

    out_hidden = np.array([act(x) for x in sum_hidden])
    print("значение на выходах скрытого слоя: " + str(out_hidden))

    sum_end = np.dot(weight2, out_hidden)
    y = act(sum_end)

    return y

house = 1
rock = 0
attr = 1

res = go(house, rock, attr)
if res ==1:
    print("i like you")
else:
    print("bye")

