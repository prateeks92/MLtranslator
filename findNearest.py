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
