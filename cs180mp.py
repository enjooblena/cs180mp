'''
Open File
Reference for manipulating CSV file: http://docs.python.org/2/library/csv.html
Training set is 31 x 12084 matrix (first row is disregarded since they are headers)
Columns 1-30 are keypoints while column 31 is the image data
Each row represents a sample, each column represents a feature.
scikit-learn follows a (sample, feature) format so convert to that 
'''

#Pre-process CSV file for conversion
import csv
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
	print featureArray[0][59]

	'''
	Structure of featureArray
	[ [header1, data1_1, data1_2], [header2, data2_1, data2_2],..., [headern, datan_1, datan_2] ]
	'''

