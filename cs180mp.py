'''
Open File
Reference for manipulating CSV file: http://docs.python.org/2/library/csv.html
Training set is 31 x 12084 matrix (first row is disregarded since they are headers)
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
	
	print averageArray