import numpy as np

def initialize_parameters(input_size):
    bias = 0.1
    weights = np.random.randn(input_size)

    return weights, bias


def step_function(z):
    #funkcja
    return np.where(z > 0, 1, 0)


def predict(X, weights, bias):
    #funkcja
    predictions = []
    for x in X:
        z = np.dot(x, weights) + bias # suma ważona
        y_pred = step_function(z) # funkcja krokowa
        predictions.append(y_pred)
    return np.array(predictions)



def update_parameters(X, y, weights, bias, learning_rate=0.1):
    # Zaimplementuj tę funkcję
    for i in range(len(X)):
        x = X[i]
        y_true = y[i]
        y_pred = predict([x], weights, bias)[0]  # Zmień to (użyj funkcji predict)
        if y_pred != y_true:
            weights += learning_rate * (y_true - y_pred) * x # Zmień to (zastosuj regułę aktualizacji)
            bias += learning_rate * (y_true - y_pred)     # Zmień to (zastosuj regułę aktualizacji)
    return weights, bias


def train_perceptron(X, y, epochs=100, learning_rate=0.1):
    # Zaimplementuj tę funkcję
    input_size = X.shape[1]
    weights, bias = initialize_parameters(input_size)  # Zmień to (użyj initialize_parameters)
    for epoch in range(epochs):
        weights, bias = update_parameters(X,y,weights, learning_rate)  # Zmień to (użyj update_parameters)
    return weights, bias

# Przetestuj funkcję
X_train = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_train = np.array([0, 0, 0, 1])  # AND gate
weights_trained, bias_trained = train_perceptron(X_train, y_train)
print("Wytrenowane wagi:", weights_trained)
print("Wytrenowany bias:", bias_trained)