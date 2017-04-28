import numpy as np
import random
import math
import re
import sys
import mpmath
import pandas as pd
from mpmath import mp
from mpmath import mpf

def find_nearest(array,value):
	idx = (np.abs(array-value)).argmin()
	return array[idx]


dictio = dict()

spanishToWordMap = "spanishToWordMap.txt"
keyArray=np.empty(0,)

with open(spanishToWordMap, "r") as file:
	for line in file:
		line = line.strip().split(',')
		dictio[line[1]] = line[0]
		keyArray=np.append(keyArray,line[1])

print keyArray

#array = np.random.random(10)

# [ 0.21069679  0.61290182  0.63425412  0.84635244  0.91599191  0.00213826
#   0.17104965  0.56874386  0.57319379  0.28719469]

#value = 0.5

#print(find_nearest(array, value))