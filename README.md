CS180 Final Project
=======

CS 180 MP: Machine Learning Project Proposal: [Facial Keypoint Detection](http://www.kaggle.com/c/facial-keypoints-detection) Using Python and [Scikit-Learn](http://scikit-learn.org/stable/).

About:
======

Program (cs180mp_main) takes in a pre-formatted CSV file (test.csv) containing image datas. Program will identify keypoints using previously crunched data (performed by cs180mp and cs180functions beforehand) loaded via averageArray.p and averagePatches.p.

Upon running program, user will be asked to input the name of the CSV file. Using the included files, the file name would be "test.csv". After loading, the program will notify the user of the number of images loaded after which they will be asked for the index of the image on which they want to apply the algorithm. _(Note: user should only input index within 0 to number of images - 1)_ 

The user can also opt to input -1 to exit the program or -2 to change the search size. The search size determines the size of the area to be searched. The algorithm moves by a value of the search size in all directions with the computed average coordinates for the current keypoint as the center. [Pearson Correlation](http://en.wikipedia.org/wiki/Pearson_product-moment_correlation_coefficient) is then computed for all patches with the highest scoring patch returned as the _"best match"_.

After computing, program will then display a window containing the processed image along with unlmabeled blue points for the keypoints. The program also prints the coordinates of the keypoints.

**Important!** - scikit-learn, numpy, and matplotlib are absolutely required to run the program properly. Please click on [this link](http://scikit-learn.org/stable/install.html) for installation instructions.

*TLDR: To run the program, run cs180mp_main.py and when prompted for the csv file, input "test.csv".*

Workflow:
=========
+ [x] Pre-process csv files
+ [x] Convert csv files to data sets
+ [x] Produce mean keypoint locations from training set
+ [x] Try out simple algorithm (mean keypoint positions, image not used)
+ [-] Develop better algorithm
    + [x] Use image patches
        + [x] Convert R tutorial code to Python and implement
            + [x] Produce average patch for all keypoints
            + [x] Write code for finding best match
                + [x] Apply algo to all keypoints
            + ~~_OR: (easier/faster route)_~~
            + ~~[x] produce average patch for at least one key point~~
            + ~~[ ] Find best match for average patch~~
            + ~~[ ] Apply average keypoint positions relative to found keypoint~~
        + [ ] Improve results
    + [ ] Search for other methods

Other Things To Do:
===================
+ [x] Learn how to [pickle/serialize objects](https://wiki.python.org/moin/UsingPickle). Apply to data sets and trained classifier for faster iteration.

References:
==========
http://www.kaggle.com/c/facial-keypoints-detection/details/getting-started-with-r
https://wiki.python.org/moin/UsingPickle
http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.extract_patches_2d.html
http://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html
http://matplotlib.org/examples/pylab_examples/matshow.html
http://docs.scipy.org/doc/scipy-0.13.0/reference/generated/scipy.stats.pearsonr.html
