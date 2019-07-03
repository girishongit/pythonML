import numpy as np  
input = np.linspace(-10, 10, 100)

def sigmoid(x):  
    return 1/(1+np.exp(-x))

from matplotlib import pyplot as plt  
import pylab
plt.plot(input, sigmoid(input), "r")  

plt.show()
#print (sigmoid(input))
