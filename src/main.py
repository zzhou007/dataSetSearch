import os

def main():
	testfile = input("""Welcome to Zi Zhou Feature Seletion Algorithm
	Type in the name of the file to test: """)
	algonum = input("""Type the number of the algorithm you want to run.

	1) Forward Selection
	2) Backward Elimination
	3) Zi's Special Algorithm
	""")
	#make lists
	data = []
	readf(data, testfile)

	#print lists
	for i in data:
		print(i)
	
	print("""The data has 
	{} features (not including class attribute
	{} instances """.format(len(data[1]) - 1, len(data)))
	search(data)
	

#readf takes a list and a file name
#reads data from the file into the list
def readf(data, testfile):
	f = open(os.path.join("/home/loli/Documents/projects/dataSetSearch/cs170data", testfile))
	
	for line in f:
		i = line.split()
		data.append(list(map(float, i)))

#search takes in one list
#searches through features to find the best matches
#prints the best match and percentage
def search(data):
	pass	


main()
