import random
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt


INPUT_DIM = 4
OUT_DIM = 3
H_DIM = 10

def relu(t):
    return np.maximum(t, 0)

def relu_deriv(t):
    return (t >=0).astype(float)

def softmax(t):
    out = np.exp(t)
    return out / np.sum(out)

def softmax_batch(t):
    out = np.exp(t)
    return out / np.sum(out, axis=1, keepdims=True)

def sparse_cross_entropy_batch(z,y):
    return -np.log(np.array([z[j, y[j]] for j in range(len(y))]))

def sparse_cross_entropy(z,y):
    return -np.log(z[0, y])

def to_full(y, num_classes):
    y_full = np.zeros((1, num_classes))
    y_full[0, y] = 1
    return y_full

def to_full_batch(y, num_classes):
    y_full = np.zeros((len(y), num_classes))
    for j, yj in enumerate(y):
        y_full[j, yj] = 1
    return y_full

iris = datasets.load_iris()
dataset = [(iris.data[i][None, ...], iris.target[i])
           for i in range(len(iris.target))]



W1 = np.random.randn(INPUT_DIM, H_DIM)
b1 = np.random.randn(1, H_DIM)
W2 = np.random.randn(H_DIM, OUT_DIM)
b2 = np.random.randn(1, OUT_DIM)

W1 = (W1 - 0.5) * 2 * np.sqrt(1/INPUT_DIM)
b1 = (b1 - 0.5) * 2 * np.sqrt(1/INPUT_DIM)
W2 = (W2 - 0.5) * 2 * np.sqrt(1/H_DIM)
b2 = (b2 - 0.5) * 2 * np.sqrt(1/H_DIM)

#learning rate ALpha

Alpha = 0.0002
Epochs = 400
loss_err=[]
BATCH_SIZE = 50

for ep in range(Epochs):
    random.shuffle(dataset)
    for i in range(len(dataset) // BATCH_SIZE):

        batch_x, batch_y = zip(*dataset[i*BATCH_SIZE : i*BATCH_SIZE+BATCH_SIZE])
        x = np.concatenate(batch_x, axis=0)
        y = np.array(batch_y)


        # Forward
        t1 = x @ W1 + b1
        h1 = relu(t1)
        t2 = h1 @ W2 + b2
        z = softmax_batch(t2)

        E = np.sum(sparse_cross_entropy_batch(z, y))

        # backward

        y_full = to_full_batch(y, OUT_DIM)

        dE_dt2 = z - y_full
        dE_dW2 = h1.T @ dE_dt2
        dE_db2 = np.sum( dE_dt2, axis=0, keepdims=True)
        dE_dh1 =  dE_dt2 @W2.T
        dE_dt1 = dE_dh1 * relu_deriv(t1)
        dE_dW1 = x.T @ dE_dt1
        dE_db1 = np.sum( dE_dt1, axis=0, keepdims=True)
        #update

        W1 = W1 - Alpha * dE_dW1
        b1 = b1 - Alpha * dE_db1
        W2 = W2 - Alpha * dE_dW2
        b2 = b2 - Alpha * dE_db2

        loss_err.append(E)



def predict(x):
    t1 = x @ W1 + b1
    h1 = relu(t1)
    t2 = h1 @ W2 + b2
    z = softmax(t2)
    return z

def accuracy():
    correct = 0
    for x, y in dataset:
        z = predict(x)
        y_pred = np.argmax(z)
        if y_pred == y:
            correct += 1
    acc = correct / len(dataset)
    return acc

accuracy = accuracy()
print("Accuracy: ", accuracy)

plt.plot(loss_err)
plt.show()
