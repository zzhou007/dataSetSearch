from __future__ import division
from __future__ import absolute_import
import os
import random
import numpy
import sys
from io import open
from itertools import imap

def main():
	#testfile is the file name of the dataset in dir /cs170data in project file
	testfile = raw_input(u"""Welcome to Zi Zhou Feature Seletion Algorithm
	Type in the name of the file to test: """)
	#algonum is the number for the algorithm used
	algonum = raw_input(u"""Type the number of the algorithm you want to run.

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
	print u"""Please wait while I normalize the numbers ..."""
	col = 0
	while col != len(data[1]):
		if col != 0:
			tmp = []
			for row in xrange(len(data)):
				tmp.append(data[row][col])
			tmp = normalize(tmp)
			for row in xrange(len(data)):
				data[row][col] = tmp[row]
		col += 1
	print u"""Done"""
	
	#print lists
	#for i in data:
	#	print(i)
	
	print u"""The data has 
	{} features (not including class attribute
	{} instances """.format(len(data[1]) - 1, len(data))

	if algonum == u"1":
		forward(data)
	elif algonum == u"2":
		backward(data)
	elif algonum == u"3":
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
		print u"I am on the {}th level".format(i)
		#for best accuracy at this level 
		best = 0
		#for feature with best accuracy
		toAdd = 0
		j = 1
		while j <= treesize:
			#cannot add the same feature twice
			if j not in currSet:
				#get accuracy
				tmpSet = []
				tmpSet += currSet
				tmpSet.append(j)
				v = validation(data, tmpSet)
				print u"""checking set {} with feature {}. 
					Accuracy is {}%""".format(currSet, j, v*100)
				if v > best:
					best = v
					toAdd = j
			j += 1
		#set the one and the set
		print u"""Feature set {} has best accuracy at {}""".format(toAdd, best)
		if prevAcc > best and i != 10:
			print u"""Warning accuracy has decreased, continuing in case of local maxima"""
		prevAcc = best
		currSet.append(toAdd)
		if theone < best:
			theone = best
			theset = []
			theset += currSet
		i += 1
		print u"""The set {} has the overall best accuracy at {}% so far.""".format(theset, theone * 100)
		print

def backward(data):
	#the one to print 
	theone = 0
	#the set to print 
	theset = []
	#size of the tree
	treesize = len(data[1]) - 1
	#to hold current features
	k = 1
	#current set of features 
	currSet = []
	while k <= len(data[1]) - 1:
		currSet.append(k)
		k += 1
	#features starts at 1
	i = treesize
	prevAcc = 0
	while i >  1:
		#print level
		print u"I am on the {}th level".format(i)
		#for best accuracy at this level 
		best = 0
		#for feature with best accuracy
		toRem = 0
		j = treesize
		while j >= 1:
			#cannot add the same feature twice
			if j in currSet:
				#get accuracy
				tmpSet = []
				tmpSet += currSet
				tmpSet.pop(tmpSet.index(j))
				v = validation(data, tmpSet)
				print u"""checking set {} removing feature {}. 
					Accuracy is {}%""".format(currSet, j, v*100)
				if v > best:
					best = v
					toRem= j
			j -= 1
		#set the one and the set
		print u"""Removing feature {} has best accuracy at {}""".format(toRem, best)
		if prevAcc > best and i != 10:
			print u"""Warning accuracy has decreased, continuing in case of local maxima"""
		prevAcc = best
		currSet.pop(currSet.index(toRem))
		if theone < best:
			theone = best
			theset = []
			theset += currSet
		i -= 1
		print u"""The set {} has the overall best accuracy at {}% so far.""".format(theset, theone * 100)
		print
		

				
def special(data):
	pass
			
#input data list, the features already added and the new feature to test
#returns the accuracy of the data
def validation(data, currSet):
	correct = 0
	instances = len(data)
	
	#one point from data set
	#for every instance
	for row in xrange(len(data)):
		p1 = []
		#make data point
		for i in currSet:
			p1.append(data[row][i])
		#test with all other data points
		mindist = sys.maxsize
		for row2 in xrange(len(data)):
			p2 = []
			if row2 != row:
				for i in currSet:
					p2.append(data[row2][i])
				if dist(p1, p2) < mindist:
					mindist = dist(p1, p2)
					classification = data[row2][0]
		if classification == data[row][0]:
			correct += 1
	return correct/instances

#returns distance between point 1 and point 2
def dist(p1, p2):
	result = 0
	
	#print points
	#print()
	#print(p1)
	#print(p2)
	
	for i in xrange(len(p1)):
		result += (p2[i] - p1[i]) ** 2
	return result ** (.5)

#readf takes a list and a file name
#reads data from the file into the list
def readf(data, testfile):
	f = open(os.path.join(u"/home/loli/Documents/projects/dataSetSearch/cs170data", testfile))
	
	for line in f:
		i = line.split()
		data.append(list(imap(float, i)))

	


main()
