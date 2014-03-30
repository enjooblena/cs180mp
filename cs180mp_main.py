'''
Main file. Used for actual keypoint location.
'''

import cs180functions as fun

def main():
	averageArray = fun.getPickle("averageArray.p")
	averagePatches = fun.getPickle("averagePatches.p")

	fileName = raw_input("Please enter filename of .csv holding image data: ")
	imageGraph = fun.loadFile(fileName)
	print "Loaded file with " + str(len(imageGraph)) + " images."

	running = 1
	search_size = 3
	while(running == 1):
		imageIndex = input("Please enter index to search for keypoints (input -1 to exit, -2 to change search size): ")
		if imageIndex == -1:
			exit()
		elif imageIndex == -2:
			search_size = input("Please enter new search size: ")
		else:
			keypoints = fun.getAllPoints(imageGraph[imageIndex], averagePatches, averageArray, 30, search_size)
			fun.displayResult(keypoints, imageGraph[imageIndex])

main()