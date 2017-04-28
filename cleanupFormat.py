import numpy
import random
import math
import re
import pandas as pd
import numpy as np

setAvgLen = 29

#cLang = "spanish"
cLang = "english"

#oLang = "english"
oLang = "spanish"

l="en"
#l="sp"

def concatLongNum(line):
	grouping = len(line)/setAvgLen
	nl=[]
	z=0
	ind=0
	while((z<len(line)) and ind<setAvgLen):
		x = line[z:(z+grouping)]
		tsum=0
		for wn in x:
			tsum = tsum+int(wn)
		tsum=tsum/grouping
		nl=nl+[tsum]
		ind=ind+1
		z=z+grouping
	return nl


def concatLongSent(line):
	grouping = len(line)/setAvgLen
	nl=[]
	z=0
	ind=0
	while((z<len(line)) and ind<setAvgLen):
		x = line[z:(z+grouping)]
		tsum=""
		for wn in x:
			tsum = tsum+wn
		nl=nl+[tsum]
		ind=ind+1
		z=z+grouping
	return nl


def allToAvgLen():
	#numberWriter = open(cLang+'_nums_avgLen.txt', 'w')
	wordWriter = open(cLang+'_toEncoderavgLen.txt', 'w')

	spRead = open(oLang+'.txt', 'r')

	wordNumbers = cLang+"_nums.txt"

	originalF = cLang+".txt"

	nonsenseNum = ["111111"]
	nonsenseWord = ["oo"]


	#words
	with open(originalF, 'r') as file:
		i = 0
		for line in file:
			spLine = spRead.readline().split()
			line = line.split()
			modline = line
			print len(modline)
			i+=1

			if(len(line)>setAvgLen or len(spLine)>setAvgLen or len(line)<26 or len(spLine)<26):
				continue

			while(len(modline)<setAvgLen):
				modline = modline + nonsenseWord
		
			else:
				fin = modline

			toWrite = ""

			for z in range(0,len(fin)):
				toWrite = toWrite + str(fin[z]) + " "

			wordWriter.write(toWrite[0:len(toWrite)-1] + "\n")
			print str(i) + "  :  " + str(len(fin))
	wordWriter.close()


def createDict():
	dictio = dict()


	avgLenSentences = cLang+"_toEncoderavgLen.txt"

	#writer = open(cLang+"_num_matrix.txt", "w")

	#wordsNumMap = open(cLang+"_EwordNumberMap.txt", "w")
	writer = open("spanishToWordMap.txt",'w')
	wordsNumMap = open("SpanishMapKeys.csv", "r")
	#numbersAvgLen = cLang+"_nums_avgLen.txt"

	with open(avgLenSentences, "r") as file:
		for line in file:
			line = line.split()
			en=wordsNumMap.readline().split(',')

			for z in range(0,len(en)):
				encode="0."+en[z].split('.')[1].split('e')[0]
				if(not(line[z] in dictio)):
					dictio[line[z]] = encode
					print line[z]

	for key in dictio:
		writer.write(str(key) + "," + str(dictio[key]) + "\n")

	writer.close()


def matrixify():
	file=l+"_EncodedWords.csv"
	
	writer = open(l+"_inputMatrix.csv",'w')
	
	if(l=="en"):
		with open(file, "r") as file:
			for line in file:
				line = line.strip().split(',')
				line=line+line[0:2]

				for i in range(0,len(line)-2):
					row = str(line[i])+","+str(line[i+1])+","+str(line[i+2])
					writer.write(str(row)+"\n")
		writer.close()

	if(l=="sp"):
		with open(file, "r") as file:
			for line in file:
				line = line.strip().split(',')

				for i in range(0,len(line)):
					row = str(line[i])
					writer.write(str(row)+"\n")
	writer.close()


def mergeMatrix():
	english="en_inputMatrix.csv"
	spanish="sp_inputMatrix.csv"

	sp=open(spanish,'r')

	out = open("inputMatrix.csv",'w')
	i=0

	with open(english,'r') as en:
		for enline in en:
			enline=enline.strip()

			spline=sp.readline().strip()

			enline=enline+","+spline
			out.write(enline+"\n")
			i+=1
			print i
	out.close()

def wordsToNum():

	langFile =  cLang+"_toEncoderavgLen.txt"

	writer = open(cLang+"_toEncoderNums.txt", "w")

	dictio = dict()

	with open(cLang+"_EwordNumberMap.txt", "r") as file:
		for line in file:
			line = line.split(',')
			dictio[line[0]] = line[1].strip()
			print dictio[line[0]]



	with open(langFile, "r") as file:
		for line in file:
			numSent=""
			line = line.split()

			for i in range(0,len(line)):
				x = dictio[line[i]]
				numSent = numSent+str(x)+" "

			writer.write(numSent+"\n")

	writer.close()
	#writer = open('eng.txt', 'w')

allToAvgLen()
wordsToNum()
createDict()
matrixify()
mergeMatrix()