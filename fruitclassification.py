import ipywidgets
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

#This script is inspired by Sebastian Lague's Youtube Neural Network Tutorial

#Weights of neural network for first output
w1_1, w2_1 = 0.0, 0.0

#Weights of neural network for second output
w1_2, w2_2 = 0.0, 0.0

#Bias
b1, b2 = 0.0, 0.0

def classify(input1, input2):
    output1 = w1_1_slider.val * input1 + w2_1_slider.val * input2 + b1_slider.val
    output2 = w1_2_slider.val * input1 + w2_2_slider.val * input2 + b2_slider.val

    return output1 > output2


def visualize(graphX, graphY):
    predictedClass = classify(graphX, graphY)

    #Graphing functionality
    if(predictedClass):
        axs.scatter(graphX, graphY, facecolor='blue', alpha=0.5)
    else:
        axs.scatter(graphX,  graphY, facecolor='red', alpha = 0.5)

def plot_fct():
    x = np.random.uniform(0, 5, size=100)
    y = np.random.uniform(0, 5, size=100)

    for i in range(x.size):
        if y[i] > -0.5*x[i] + 2:
            axs.scatter(x[i], y[i], color= 'red')
        else:
            axs.scatter(x[i], y[i], color ='blue')
    
def update_graph(indx):
    for x in np.arange(0.0,5.0,0.1):
        for y in np.arange(0.0,5.0,0.1):
            visualize(x,y)



fig, axs = plt.subplots()
plot_fct()
plt.subplots_adjust(bottom = 0.35)

w1_1_axes = plt.axes([0.1, 0.25, 0.8, 0.05], facecolor='gray')
w1_1_slider = Slider(w1_1_axes, "W1_1", valmin=-1, valmax=1, valinit=0, valstep = 0.1)

w2_1_axes = plt.axes([0.1, 0.2, 0.8, 0.05], facecolor='gray')
w2_1_slider = Slider(w2_1_axes, "W2_1", valmin=-1, valmax=1, valinit=0, valstep = 0.1)

w1_2_axes = plt.axes([0.1, 0.15, 0.8, 0.05], facecolor='gray')
w1_2_slider = Slider(w1_2_axes, "W1_2", valmin=-1, valmax=1, valinit=0, valstep = 0.1)

w2_2_axes = plt.axes([0.1, 0.1, 0.8, 0.05], facecolor='gray')
w2_2_slider = Slider(w2_2_axes, "W2_2", valmin=-1, valmax=1, valinit=0, valstep = 0.1)

b1_axes = plt.axes([0.1, 0.05, 0.8, 0.05], facecolor='gray')
b1_slider = Slider(b1_axes, "B1", valmin=-1, valmax=1, valinit=0, valstep = 0.1)

b2_axes = plt.axes([0.1, 0, 0.8, 0.05], facecolor='gray')
b2_slider = Slider(b2_axes, "B2", valmin=-1, valmax=1, valinit=0, valstep = 0.1)

w1_1_slider.on_changed(update_graph)







plt.show()
    







