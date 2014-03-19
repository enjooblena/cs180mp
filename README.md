cs180mp
=======

CS 180 MP: Machine Learning  project proposal: Facial Keypoint Detection.

Workflow:
=========
[] Pre-process csv files
[] Convert csv files to data sets
[] Produce mean keypoint locations from training set
[] Try out simple algorithm (mean keypoint positions, image not used)
[] Develop better algorithm
    [] Use image patches
        [] Convert R tutorial code to Python and implement
            [] Produce average patch for all keypoints
            [] Write code for finding best match
                [] Apply algo to all keypoints
            OR: (easier/faster route)
            [] produce average patch for at least one key point
            [] Find best match for average patch
            [] Apply average keypoint positions relative to found keypoint
        [] Improve results
    [] Search for other methods
