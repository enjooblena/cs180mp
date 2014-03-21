CS180 Final Project
=======

CS 180 MP: Machine Learning Project Proposal: [Facial Keypoint Detection](http://www.kaggle.com/c/facial-keypoints-detection) Using Python and [Scikit-Learn](http://scikit-learn.org/stable/).

Workflow:
=========
+ [x] Pre-process csv files
+ [x] Convert csv files to data sets
+ [x] Produce mean keypoint locations from training set
+ [x] Try out simple algorithm (mean keypoint positions, image not used)
+ [-] Develop better algorithm
    + [-] Use image patches
        + [-] Convert R tutorial code to Python and implement
            + [-] Produce average patch for all keypoints
            + [ ] Write code for finding best match
                + [ ] Apply algo to all keypoints
            + _OR: (easier/faster route)_
            + [x] produce average patch for at least one key point
            + [ ] Find best match for average patch
            + [ ] Apply average keypoint positions relative to found keypoint
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