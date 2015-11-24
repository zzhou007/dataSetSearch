import os

def main():
	lists = []
	listl = []
	readf(lists, listl)
	for i in lists:
		print(i)

#readf takes two lists 
#read in csfile large and cs file small into two lists
def readf(lists, listl):
	fl = open(os.path.join("/home/loli/Documents/projects/dataSetSearch/cs170data", "cs_170_large73.txt"))
	fs = open(os.path.join("/home/loli/Documents/projects/dataSetSearch/cs170data", "cs_170_small73.txt"))
	
	for line in fs:
		i = fs.readline().split()
		lists.append(list(map(float, i)))
	for line in fl:
		i = fl.readline().split()
		listl.append(list(map(float, i)))


main()
