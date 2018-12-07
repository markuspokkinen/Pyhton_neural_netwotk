from NeuralNetwork import NeuralNetwork
import numpy as np


data = np.array([[1,1,0],[1,0,1],[0,0,0],[1,1,1],[1,0,0]])
result = np.array([[1],[1],[0],[1],[1]])

weight1 = np.random.uniform(-1,1,[3,15])
weight2 = np.random.uniform(-1,1,[15,1])

nn = NeuralNetwork(weight1,weight2,data,result)
nn.new_result(data)