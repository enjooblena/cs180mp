import math
import pylab as pl
from matplotlib.pylab import *
import cPickle as pickle
from sklearn.feature_extraction import image

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
	for index in range(0, len(imageGraph)):
		print "Getting image patch at index " + str(index)
		temp = getPatch(float(featureArray[featureNumber][1 + index]), float(featureArray[featureNumber+1][1 + index]), imageGraph[index])
		if len(temp) != 1:
			patchArray.append(temp)
		else:
			print "Skipped image patch at index " + str(index)

	averagePatch = zeros((96, 96))

	#Gets actual average patch
	temp_x = 0
	temp_y = 0
	counter = 0
	for image in patchArray:
		for row in image:
			print "Entering row " + str(counter)
			for column in row:
				averagePatch[temp_x][temp_y] += column / len(patchArray)
				temp_x += 1
			temp_y += 1
		temp_x = 0
		temp_y = 0
		count += 1

	print averagePatch
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