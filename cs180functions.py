import math
import csv
import pylab as pl
from matplotlib.pylab import *
import cPickle as pickle
from sklearn.feature_extraction import image

def importFeatureArray():
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
					else:
						featureArray[index].append(-1)	#does not exist for this index
					index += 1
		return featureArray

def getCoor(x, y, patch_size = 21, x_total = 96, y_total = 96):
		x1 = math.floor(x - patch_size/2)
		y1 = math.floor(y - patch_size/2)
		if (x1 < 0) or (y1 < 0):
			return -1
		else:
			return (x_total-patch_size+1) * y1 + x1

def getPickle(fileName):
	return pickle.load(open(fileName, "rb"))

def getPatch(x, y, currentImage):
	if getCoor(x, y) < 0:
		return [-1] #not eligible for averaging
	else:
		patches = image.extract_patches_2d(currentImage, (21, 21))	#gets 21x21 patches
		return patches[int(getCoor(x, y))]

def getAveragePatch(featureArray, featureNumber, imageGraph):
	patchArray = []

	#gets patches of all images
	averagePatch = zeros((21, 21))
	counter = 0

	for index in range(0, len(imageGraph)):
		if (index >= 1000) and (index % 1000 == 0):
			print "Getting image patch at index " + str(index)
		if(featureArray[featureNumber][1 + index] != -1) and (getCoor(float(featureArray[featureNumber][1 + index]), float(featureArray[featureNumber + 1][1 + index])) < 5776):
			temp = getPatch(float(featureArray[featureNumber][1 + index]), float(featureArray[featureNumber+1][1 + index]), imageGraph[index])
		else:
			temp = [-1]
		if len(temp) != 1:
			counter += 1
			temp_x = 0
			temp_y = 0
			for row in temp:
				for column in row:
					averagePatch[temp_x][temp_y] += column
					temp_x += 1
				temp_y += 1
				temp_x = 0
			temp_y = 0
			#patchArray.append(temp)
		else:
			print "Skipped image patch at index " + str(index)
	'''
	for row in averagePatch:
		for column in row:
			averagePatch[temp_x][temp_y] = (averagePatch[temp_x][temp_y] / counter)
			temp_x += 1
		temp_y += 1
		temp_x = 0
	temp_y = 0
	'''

	'''
	#Gets actual average patch
	temp_x = 0
	temp_y = 0
	for image in patchArray:
		#print "Entering image " + str(counter)
		for row in image:
			for column in row:
				averagePatch[temp_x][temp_y] += column / len(patchArray)
				temp_x += 1
			temp_y += 1
			temp_x = 0
		temp_y = 0
	'''

	#print averagePatch
	return averagePatch

	def getBestMatch(imagePatches, averagePatches, featureNumber):
		#compute score
		bestPatch = 0
		for i in imagePatches:
			if score(i, averagePatch[featureNumber]) < bestPatch:
				bestPatch = i
		return bestPatch

	'''
	Get Pickles
	get averagePatch for features
	pickle averagePatch

	'''

	'''
	rotate averagePatch result by -90
	>>> from scipy import ndimage
	>>> rotate_lena = ndimage.rotate(lena, 45)
	http://www.tp.umu.se/~nylen/pylect/advanced/image_processing/index.html
	'''

	'''
	to generate all average patches
	averagePatches = []
	for index in range(0, 30, 2): #(even indexes are x, odd are y)
		temp = getAveragePatch(featureArray, index, imageGraph)
		temp = ndimage.rotate(temp, -90)	#rotates image to proper orientation
		averagePatch.append(temp)

	averagePatch of feature_n is at math.floor(n/2)
	'''

	'''
	patch searching
	average keypoint of feature is center
	compute for 

	create search_size*2 + 1 * search_size*2 + 1 array of possibilities
	center = getCoor(avg_x, avg_y)

	searchMatrix = createSearchMatrix(x, y, search_size)

	createSearchMatrix(x, y, search_size):
		x1 = x - search_size	#leftmost
		y1 = y - search_size	#topmost
		tempMatrix = []

		for y_index in range(y1, y + search_size):
			for x_index in range(x1, x + search_size):
				tempMatrix.append([x_index, y_index])

		return tempMatrix

		#tempMatrix structure:
		[ [x_index1, y_index1]...[x_indexn, y_indexn] ]

	'''