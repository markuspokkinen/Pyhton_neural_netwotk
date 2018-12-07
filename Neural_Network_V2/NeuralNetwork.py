import numpy
import pandas as pd

class NeuralNetwork(object):
    
    weight1 = None
    weight2 = None
    data = None
    result = None
    hiddenlist = None

    def __init__(self,weight1,weight2,data,result):
        self.weights = weightlist
        self.data = data
        self.hiddenlist = [0]*len(weightlist)
        self.result = result

    def logisticActivationFuntion(self,value):
        return 1.0/(1.0+numpy.exp(-value))

    def randomWeight(size):
        return numpy.random.uniform(-1,1,size)

    def train(self,rounds):
        for i in range(rounds):
            for weightIndex in range(len(self.weights)):
                if(weightIndex == 0):
                    self.hiddenlist[0] = self.logisticActivationFuntion(numpy.dot(self.data,self.weights[0])+1)

                else:
                    self.hiddenlist[weightIndex] = self.logisticActivationFuntion(numpy.dot(self.hiddenlist[weightIndex-1],self.weights[weightIndex])+1)

            calcVal = self.logisticActivationFuntion(numpy.dot(hidden1,self.weight2)+1)
            if(i == 1):
                print(calcVal)

            resultError = self.result - calcVal
 
            result_delta = resultError*(calcVal*(1-calcVal))

            l1_error = result_delta.dot(self.weight2.T)

            # in what direction is the target l1?
            # were we really sure? if so, don't change too much.
            l1_delta = l1_error *(hidden1*(1-hidden1))

 
            self.weight2 += hidden1.T.dot(result_delta)
            self.weight1 += self.data.T.dot(l1_delta)
            if(i == rounds-1):
                print(calcVal)
                

    def new_result(self,setdata):
        hidden1 = self.logisticActivationFuntion(numpy.dot(setdata,self.weights[weightIndex])+1)
       
        print(self.hiddenlist[0])
        print("1 ")
        print(self.hiddenlist[1])
        print("last ")
        print(self.hiddenlist[-1])
        print(" ")
        print(self.weights[-1])
        print(" ")
        calcVal = self.logisticActivationFuntion(numpy.dot(self.hiddenlist[-1],self.weights[-1])+1)      
        print(calcVal)