#This is an Simple Neural Network program, trying to predict the diabetic based on smoking, Obesity Exercise
# Person    Smoking Obesity Exercise    Diabetics
# Person1    0	      1	       0	      1
# Person2	 0	      0	       1	      0
# Person3	 1	      0	       0	      0
# Person4	 1	      1	       0	      1
# Person5	 1	      1	       1	      1

import numpy as np  
#input Parameter
feature_set = np.array([[0,1,0],[0,0,1],[1,0,0],[1,1,0],[1,1,1]])  
#Output Results
labels = np.array([[1,0,0,1,1]])
labels = labels.reshape(5,1)  
# Other ways to Transpose is np.array([[1,0,0,1,1]]).T / labels = np.array([[1,0,0,1,1]]).transpose()
