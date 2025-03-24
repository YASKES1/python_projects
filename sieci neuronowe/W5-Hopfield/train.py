# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 08:40:49 2018

@author: user
"""
import imageio
import numpy as np
np.random.seed(1)
from matplotlib import pyplot as plt
import skimage.data
from skimage.color import rgb2gray
from skimage.filters import threshold_mean
from skimage.transform import resize
from skimage import io
import network


# Utils
# Function that introduces noise into the image, the greater the corruption level the greater the disturbance
def get_corrupted_input_noise(input, corruption_level):
    corrupted = np.copy(input)
    inv = np.random.binomial(n=1, p=corruption_level, size=len(input))
    for i, v in enumerate(input):
        if inv[i]:
            corrupted[i] = -1 * v
    return corrupted


# Function that obscures a certain part of the image from the upper left corner, corruption level is between 0-1 and indicates the
# the size of the obstructing square (as % of the image width)
def get_corrupted_input_cover(input, corruption_level):
    corrupted = np.copy(input)
    corrupted = np.reshape(corrupted, (128, 128))
    toNum = int(128*corruption_level)
    for i in range(toNum):
        for j in range(toNum):
            corrupted[i][j] = -1
    corrupted = corrupted.flatten()
    return corrupted

def corrupt_custom(input, corruption_level):
    corrupted = np.copy(input)
    corrupted = np.reshape(corrupted, (128, 128))
    square = int(128 * corruption_level)
    num_squares = np.random.randint(2,6)
    if square > 128:
        square = 128
    for _ in range(num_squares):
        start_x = np.random.randint(1, 128 - square)
        start_y = np.random.randint(1, 128 - square)
        for i in range(start_x, start_y + square):
            for j in range(start_x, start_y + square):
                corrupted[i][j] = -1
    corrupted = corrupted.flatten()
    return corrupted


def reshape(data):# Auxiliary function

    dim = int(np.sqrt(len(data)))
    data = np.reshape(data, (dim, dim))
    return data


# A function that draws the effects of Hopfield networks
def plot(data, test, predicted, figsize=(5, 6)):
    data = [reshape(d) for d in data]
    test = [reshape(d) for d in test]
    predicted = [reshape(d) for d in predicted]

    fig, axarr = plt.subplots(len(data), 3, figsize=figsize)
    for i in range(len(data)):
        if i==0:
            axarr[i, 0].set_title('Train data')
            axarr[i, 1].set_title("Input data")
            axarr[i, 2].set_title('Output data')

        axarr[i, 0].imshow(data[i])
        axarr[i, 0].axis('off')
        axarr[i, 1].imshow(test[i])
        axarr[i, 1].axis('off')
        axarr[i, 2].imshow(predicted[i])
        axarr[i, 2].axis('off')

    plt.tight_layout()
    plt.savefig("result.png")
    plt.show()


# Image processing - scaling to 128x128 pixels, converting the image from color to binary. This is done
# by finding the average value in the image and assigning 1 as there is a pixel value larger and -1 as smaller
# than the average value. Flatten saves the image as a vector of length 128*128
def preprocessing(img, w=128, h=128):
    # Resize image
    img = resize(img, (w, h), mode='reflect')

    # Thresholding
    thresh = threshold_mean(img)
    binary = img > thresh
    shift = 2*(binary*1)-1 # Boolian to int

    # Reshape
    flatten = np.reshape(shift, (w*h))
    return flatten


def main():
    # Load data
    camera = skimage.data.camera()
    astronaut = rgb2gray(skimage.data.astronaut())
    horse = skimage.data.horse()
    coffee = rgb2gray(skimage.data.rocket())

    # Load image from file, example
    pkin = rgb2gray(io.imread("imgs/pkin.jpg"))
    tower = rgb2gray(io.imread("imgs/tower.jpg"))
    statue = rgb2gray(io.imread("imgs/statue.jpg"))
    flower = rgb2gray(io.imread("imgs/flower.jpg"))
    mouse = rgb2gray(io.imread("imgs/mouse.jpg"))
    # Marge data
    #data = [camera, astronaut, horse, pkin]
    data = [tower, flower, mouse, statue]

    # Preprocessing
    print("Start to data preprocessing...")
    data = [preprocessing(d) for d in data]

    # Create Hopfield Network Model
    model = network.HopfieldNetwork()
    model.train_weights(data)

    # Generate testset
    test = [corrupt_custom(d, 0.12) for d in data]

    predicted = model.predict(test, threshold=0, asyn=False)
    print("Show prediction results...")
    plot(data, test, predicted)
    print("Show network weights matrix...")
    #model.plot_weights()


if __name__ == '__main__':
    main()
