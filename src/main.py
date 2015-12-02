import os
import random
import numpy
import sys

def main():
	#testfile is the file name of the dataset in dir /cs170data in project file
	testfile = input("""Welcome to Zi Zhou Feature Seletion Algorithm
	Type in the name of the file to test: """)
	#algonum is the number for the algorithm used
	algonum = input("""Type the number of the algorithm you want to run.

	1) Forward Selection
	2) Backward Elimination
	3) Zi's Special Algorithm
	""")
	#make lists and normalize
	data = []
	readf(data, testfile)
	
	#print lists
	#for i in data:
	#	print(i)

	#normalize
	print("""Please wait while I normalize the numbers ...""")
	col = 0
	while col != len(data[1]):
		if col != 0:
			tmp = []
			for row in range(len(data)):
				tmp.append(data[row][col])
			tmp = normalize(tmp)
			for row in range(len(data)):
				data[row][col] = tmp[row]
		col += 1
	print("""Done""")
	
	#print lists
	#for i in data:
	#	print(i)
	
	print("""The data has 
	{} features (not including class attribute
	{} instances """.format(len(data[1]) - 1, len(data)))

	if algonum == "1":
		forward(data)
	elif algonum == "2":
		backward(data)
	elif algonum == "3":
		special(data)
	else:
		pass
#input list
#returns normalized list
def normalize(set):
	j = 0
	for i in set:
		set[j] = (set[j] - numpy.mean(set))/numpy.std(set)
		j += 1
	return set
	
#forward uses a forward search
#takes a list of data 
#prints step by step adding the best feature
def forward(data):
	#the one to print 
	theone = 0
	#the set to print 
	theset = []
	#size of the tree
	treesize = len(data[1]) - 1
	#to hold current features
	currSet = []
	#features starts at 1
	i = 1
	prevAcc = 0
	while i <=  treesize:
		#print level
		print("I am on the {}th level".format(i))
		#for best accuracy at this level 
		best = 0
		#for feature with best accuracy
		toAdd = 0
		j = 1
		while j <= treesize:
			#cannot add the same feature twice
			if j not in currSet:
				#get accuracy
				v = validation(data, currSet, j)
				print ("""checking set {} with feature {}. 
					Accuracy is {}%""".format(currSet, j, v*100))
				if v > best:
					best = v
					toAdd = j
			j += 1
		#set the one and the set
		print("""Feature set {} has best accuracy at {}""".format(toAdd, best))
		if prevAcc > best and i != 10:
			print("""Warning accuracy has decreased, continuing in case of local maxima""")
		prevAcc = best
		currSet.append(toAdd)
		if theone < best:
			theone = best
			theset.clear()
			theset += currSet
		i += 1
		print("""The set {} has the overall best accuracy at {}% so far.""".format(theset, theone * 100))
		print()

def backward(data): 
	#size of the tree
	treesize = len(data[1]) - 1
	#to hold removed features
	remSet = []
	
				
def special(data):
	pass
			
#input data list, the features already added and the new feature to test
#returns the accuracy of the data
def validation(data, currSet, j):
	correct = 0
	instances = len(data)
	
	#one point from data set
	#for every instance
	for row in range(len(data)):
		p1 = []
		#make data point
		for i in currSet:
			p1.append(data[row][i])
		p1.append(data[row][j])
		#test with all other data points
		mindist = sys.maxsize
		for row2 in range(len(data)):
			p2 = []
			if row2 != row:
				for i in currSet:
					p2.append(data[row2][i])
				p2.append(data[row2][j])
				if dist(p1, p2) < mindist:
					mindist = dist(p1, p2)
					classification = data[row2][0]
		if classification == data[row][0]:
			correct += 1
	return correct/instances
	
def dist(p1, p2):
	result = 0
	
	#print points
	#print()
	#print(p1)
	#print(p2)
	
	for i in range(len(p1)):
		result += (p2[i] - p1[i]) ** 2
	return result ** (.5)

#readf takes a list and a file name
#reads data from the file into the list
def readf(data, testfile):
	f = open(os.path.join("/home/loli/Documents/projects/dataSetSearch/cs170data", testfile))
	
	for line in f:
		i = line.split()
		data.append(list(map(float, i)))

	


main()
