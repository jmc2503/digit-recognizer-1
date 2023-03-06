import ipywidgets
import numpy as np
import matplotlib.pyplot as plt

#This script is inspired by Sebastian Lague's Youtube Neural Network Tutorial

#Weights of neural network for first output
w1_1, w2_1 = 0.0, 0.0

#Weights of neural network for second output
w1_2, w2_2 = 0.0, 0.0

#Bias
b1, b2 = 0.0, 0.0

def classify(input1, input2):
    output1 = w1_1 * input1 + w2_1 * input2 + b1
    output2 = w1_2 * input1 + w2_2 * input2 + b2

    return output1 > output2


def visualize(graphX, graphY):
    predictedClass = classify(graphX, graphY)

    #Graphing functionality
    if(predictedClass):
        pass
    else:
        pass

def plot_fct(w=1):
    x = np.random.uniform(0, 5, size=100)
    y = w * np.random.normal(size=100)

    for i in range(x.size):
        if y[i] > 0:
            plt.scatter(x[i], y[i], color= 'red')
        else:
            plt.scatter(x[i], y[i], color ='blue')
    


#add slider functionality
plt.show()
    







