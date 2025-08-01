# reuters dataset


import keras
from keras import layers, models
from keras.models import Sequential
from keras.datasets import reuters
from keras import optimizers, losses, metrics
import numpy as np


(train_data, train_labels), (test_data, test_labels) = reuters.load_data(num_words=10000)

len(train_data)
len(test_data)

#decode into text
word_index = reuters.get_word_index()
reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])
decoded_newswire =  ' '.join([reverse_word_index.get(i - 3, '?') for i in
                              train_data[0]])
# индексы смещены на 3 потому что 0,1,2 зарезервированы для слов padding, start of sequence, unknown

# кодирование данных

def vectorize_sequence(sequences, dimension=10000):
  results = np.zeros((len(sequences), dimension))
  for i, sequnce in enumerate(sequences):
    results[i, sequnce] = 1
  return results

x_train = vectorize_sequence(train_data)
x_test = vectorize_sequence(test_data)

#one-hot encoding кодирование категорий
def to_one_hot(labels, dimension=46):
  results = np.zeros((len(labels), dimension))
  for i, label in enumerate(labels):
    results[i, label] = 1
  return results

one_hot_train_labels = to_one_hot(train_labels)
one_hot_test_labels = to_one_hot(test_labels)

model = models.Sequential()
model.add(layers.Dense(64, activation='relu', input_shape=(10000,)))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(46, activation='softmax'))

# скть завершается слоем с размером 46, для каждого выхода сеть выводит 46-мерный вектор. 
#каждый элемент этого вектора отдельный выходной клас

#последний слой софтмакс будет выводить распредиление вероятностей по 46 разным класам где сумма 46 элементов всегда равна 1


# функция потери определяет расстояние между распределениями вероятностей на выходе сети и истинным распределением меток
#минимизируя расстояние между этими двуся распределениями мы учим сеть выводить резултат максимально близкий к истинным значениям

model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

#проверка решений
#создание проверочного набора

x_val = x_train[:1000]
partial_x_train = x_train[1000:]

y_val = one_hot_train_labels[:1000]
pratial_y_train = one_hot_train_labels[1000:]


#model training

history = model.fit(partial_x_train,
                    pratial_y_train,
                    epochs=20,
                    batch_size=512,
                    validation_data=(x_val, y_val))
import matplotlib.pyplot as plt

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(1, len(loss) +1 )

plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.show()

plt.clf()
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Loss')  





