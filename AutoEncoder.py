import numpy as np
import pandas as pd
import random
pd.set_option('precision', 12)

def formMatrix(file):
	data = pd.read_csv(file,  sep = ',')
	df = pd.DataFrame(data = data, dtype = float)
	return df

def sigmoid(x):
	return 1/(1 + np.exp(-x))
	
def encoderTrain(x):
	w1 = np.zeros((x.shape[1], x.shape[1] - 4)) + 0.119945801707
	w2 = np.zeros((x.shape[1] - 3, x.shape[1] - 1)) + 0.368386302287
	lr = 0.42
	epoch = 10
	for k in range(epoch):
		for i in range(x.shape[0]):
			h = sigmoid(np.dot(x[i, :], w1))
			h = np.append(h, 1)
			o = sigmoid(np.dot(h, w2))
			summ1 = (x[i, :x.shape[1]-1] - o) * o * (1 - o)
			for j in range(x.shape[1] - 4):
				summ2 = np.sum(summ1 * w2[j, :]) * h[j] * (1 - h[j])
				w1[:, j] += np.transpose(lr * (summ2 * x[i,:]))
			for j in range(x.shape[1] - 3):
				w2[j, :] += lr * (summ1 * h[j])
				
		#if (k%100 == 0):
		print(str(w2[0,0]) + "	" + str(w1[0,0]))
	return w1, w2
	
def main():
	df = formMatrix('english_Encoder_matrix.txt')
	cols = df.shape[1]
	rows = df.shape[0]
	xtrain = df.iloc[0:rows, 0:cols]
	xtrain = np.array(xtrain.values)
	one = np.ones((xtrain.shape[0], 1))
	xtrain = np.c_[xtrain, one]
	weight_lvl1_36, weight_lvl2_36 = encoderTrain(xtrain)
	#xtemp = sigmoid(np.dot(xtrain, weight_lvl1_36))
	#xtemp = np.c_[xtemp, one]	
	#weight_lvl1_31, weight_lvl2_31 = encoderTrain(xtemp)
	#xfinal = sigmoid(np.dot(xtemp, weight_lvl1_31))
	print(xtrain[10,:])
	xtemp1 = sigmoid(np.dot(xtrain[10,:], weight_lvl1_36))
	xtemp1 = np.append(xtemp1, 1)
	xfinal1 = sigmoid(np.dot(xtemp1, weight_lvl2_36))
	print(xfinal1)
	#np.savetxt("EncodedWords.csv", xfinal, delimiter = ",")
	np.savetxt("Weight_lvl1_36.csv", weight_lvl1_36, delimiter = ",")
	np.savetxt("Weight_lvl2_36.csv", weight_lvl2_36, delimiter = ",")
	#np.savetxt("Weight_lvl1_31.csv", weight_lvl1_31, delimiter = ",")
	#np.savetxt("Weight_lvl2_31.csv", weight_lvl2_31, delimiter = ",")
		
if __name__ == "__main__": main()
