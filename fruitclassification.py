#This script is inspired by Sebastian Lague's Youtube Nerual Network Tutorial


#Weights of neural network for first output
weight1_1, weight2_1 = 0.0, 0.0

#Weights of neural network for second output
weight1_2, weight2_2 = 0.0, 0.0

#Bias
bias1, bias2 = 0.0, 0.0

def classify(input1, input2):
    output1 = weight1_1 * input1 + weight2_1 * input2 + bias1
    output2 = weight1_2 * input1 + weight2_2 * input2 + bias2

    return output1 > output2


def visualize(graphX, graphY):
    predictedClass = classify(graphX, graphY)

    #Graphing functionality
    if(predictedClass):
        pass
    else:
        pass






