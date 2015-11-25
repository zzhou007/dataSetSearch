import os
import random

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
	#make lists
	data = []
	readf(data, testfile)

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
	
#forward uses a forward search
#takes a list of data 
#prints step by step adding the best feature
def forward(data):
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
					Accuracy is {}%""".format(currSet, j, v))
				if v > best:
					best = v
					toAdd = j
			j += 1
		print("""Feature set {} has best accuracy at {}""".format(toAdd, best))
		if prevAcc > best and i != 10:
			print("""Warning accuracy has decreased, continuing in case of local maxima""")
		prevAcc = best
		currSet.append(toAdd)
		i += 1
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
	#test algorithms
	return random.random()
		

#readf takes a list and a file name
#reads data from the file into the list
def readf(data, testfile):
	f = open(os.path.join("/home/loli/Documents/projects/dataSetSearch/cs170data", testfile))
	
	for line in f:
		i = line.split()
		data.append(list(map(float, i)))

	


main()
