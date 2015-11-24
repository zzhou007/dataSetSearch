import os

def main():
	#make lists
	lists = []
	listl = []
	readf(lists, listl)
	#print lists
	for i in lists:
		print(i)
	#pick a list
	lsize = input("""What list do you want to search?
		(0) small
		(1) large
	""")

	if lsize == 0:
		data = lists
	else:
		data = listl
	search(data)
	

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

#search takes in one list
#searches through features to find the best matches
#prints the best match and percentage
def search(data):
	pass	


main()
