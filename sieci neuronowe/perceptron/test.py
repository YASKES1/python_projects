import numpy as np

def initialize_parameters(input_size):
    bias = np.array([1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1])
    weights = np.array([0.5, 0, 1])

    # implementacja funkcji
    dot_product = np.dot(bias[1],weights[1])

    return weights, bias, dot_product

bias = np.array([[1, 0, 0],
                [1, 0, 1],
                [1, 1, 0],
                [1, 1, 1]])
weights = np.array([0.5, 0, 1])
d = ([0, 0, 0, 1])
learn_const = 1


y = iloczyn = np.dot(bias[0],weights[0])
suma = sum(iloczyn)
print("Wagi: ", weights)
print("Bias: ", bias)
print("iloczyn: ", iloczyn)
print(suma)


if suma > 0:
    g = 1
else:
    g = 0
print(g)
parametr = d[0] - g

w_k = weights[0] + learn_const * parametr * bias[0][0]
print(w_k)

for i in weights:
    w_k = weights + learn_const * parametr * bias[0][0]
    print(w_k)


