'''
Open File
Reference for manipulating CSV file: http://docs.python.org/2/library/csv.html
Training set is 31 x 7k+ matrix (first row is disregarded since they are headers)
Columns 1-30 are keypoints while column 31 is the image data
Each row represents a sample, each column represents a feature.
scikit-learn follows a (sample, feature) format so convert to that 
'''

'''
Training Part of Program
Deals with pre-processing of data, conversion to a format for use with scikit-learn and training.
'''

#Pre-process CSV file for conversion
import csv
import math
import pylab as pl
from matplotlib.pylab import *
import cPickle as pickle

with open('training.csv', 'rb') as csvfile:
	preprocessReader = csv.reader(csvfile, delimiter = ',', quotechar = '|')
	counter = 1
	testCounter = 5
	headerTitle = []
	featureArray = []
	for row in preprocessReader:
		#row[30] is image data
		#print row[30]

		if counter == 1: #row being read is header
			for header in row:
				featureArray.append([header])
			counter -= 1
		else:	#row being read is data
			index = 0
			for item in row:
				if (item != "") & (item != " "):
					featureArray[index].append(item)
				index += 1

		''' Limits number of data read to testCounter - 1
		testCounter -= 1
		print featureArray[5]
		print "\nNEXT ROW\n"
		if testCounter == 0:
			break
		'''
	#print featureArray[0][2]
	#print featureArray[0][59]

	'''
	Structure of featureArray
	[ [header1, data1_1, data1_2], [header2, data2_1, data2_2],..., [headern, datan_1, datan_2] ]
	'''

	'''
	Computation of Keypoint average position
	'''

	averageArray = []
	for feature in featureArray[:-1]: #does not include image features
		tempAverage = 0
		for data in feature[1:]:	#disregards header
			tempAverage +=  float(data)/float(len(feature)-1)
		averageArray.append(tempAverage)
		#print feature[0]
	
	#print averageArray


	'''
	Conversion of Vector to Image
	+ Use split to separate " "
	+ Use scikit-learn
	+ Use this format:
	[[  0.   0.   5. ...,   0.   0.   0.]
 	 [  0.   0.   0. ...,  10.   0.   0.]
	 [  0.   0.   0. ...,  16.   9.   0.]
	 ...,
	 [  0.   0.   1. ...,   6.   0.   0.]
	 [  0.   0.   2. ...,  12.   0.   0.]
	 [  0.   0.  10. ...,  12.   1.   0.]]

	http://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html
	http://matplotlib.org/examples/pylab_examples/matshow.html
	http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.extract_patches_2d.html#sklearn.feature_extraction.image.extract_patches_2d

	use reshape((x,y)) to transform vector to 2 dimensional array
	e.g:
		>>> from sklearn.feature_extraction import image
		>>> one_image = np.arange(16).reshape((4, 4))

	Pictures are 96x96 matrix
	'''

	print "Entering value splitting"

	pl.gray()
	testGraph = []
	for n in featureArray[-1][1:]:
		testGraph.append(n.split(" "))	#fetches first data from image set
		#if len(testGraph)
	#imageGraph = zeros((96, 96))	#creates 96x96 array of 0s
	
	#'''
	imageGraph = []

	print len(testGraph)			#Use this one
	print len(featureArray[-1])		#Incorrect because header is still added

	for i in range(0, len(testGraph)):	#creates a n x 96 x 96 array where n is the number of images
		imageGraph.append(zeros((96,96)))

	#'''

	print "Entering array population\n"

	pixelCounter = 0
	for n in range(0, len(testGraph)):
	#for n in range(0, 2):
		for i in range(0,96):			#populates array with value from image
			for j in range(0,96):
				imageGraph[n][i,j] = testGraph[n][pixelCounter]
				pixelCounter += 1
		pixelCounter = 0
	#IMAGE IS FLIPPED HORIZONTALLY

	#'''

	print "Entering image flipping\n"

	#FLIPS IMAGE
	for n in range(0, len(testGraph)):
	#for n in range(0, 2):
		for i in range(0,96):
			for j in range(0,48):
				tempPixel = imageGraph[n][i, 95-j]	#right side pixel
				imageGraph[n][i,95-j] = imageGraph[n][i, j]
				imageGraph[n][i,j] = tempPixel
	#'''

	#print testGraph.shape()


	#print len(featureArray[-1])

	#Pickle current data - UNTESTED CODE
	pickle.dump(averageArray, open("averageArray.p", "wb"))
	pickle.dump(featureArray, open("featureArray.p", "wb"))
	pickle.dump(imageGraph, open("imageGraph.p", "wb"))


	#shows image on screen
	pl.matshow(imageGraph[1])
	pl.show()

	'''
	Generating and using Image Patches
	References:
	http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.extract_patches_2d.html

	'''