CS180 Final Project
=======

CS 180 MP: Machine Learning Project Proposal: [Facial Keypoint Detection](http://www.kaggle.com/c/facial-keypoints-detection) Using Python and [Scikit-Learn](http://scikit-learn.org/stable/).

Workflow:
=========
+ [ ] Pre-process csv files
+ [ ] Convert csv files to data sets
+ [ ] Produce mean keypoint locations from training set
+ [ ] Try out simple algorithm (mean keypoint positions, image not used)
+ [ ] Develop better algorithm
    + [ ] Use image patches
        + [ ] Convert R tutorial code to Python and implement
            + [ ] Produce average patch for all keypoints
            + [ ] Write code for finding best match
                + [ ] Apply algo to all keypoints
            + _OR: (easier/faster route)_
            + [ ] produce average patch for at least one key point
            + [ ] Find best match for average patch
            + [ ] Apply average keypoint positions relative to found keypoint
        + [ ] Improve results
    + [ ] Search for other methods

References:
==========
http://www.kaggle.com/c/facial-keypoints-detection/details/getting-started-with-r
