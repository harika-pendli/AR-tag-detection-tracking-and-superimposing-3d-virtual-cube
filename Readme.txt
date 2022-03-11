This folder consists of three solution scripts, two utils scripts, one video and two images(testudo and AR tag reference image)

NOTE: code when running on my PC had issues when path is relative, so I put absolute path. I would recommend you to put the absolute
path too.
---------------------------------------------------------------------------------------------------------------------------------
To run 1a.py, change the path on line 10, that is the location of the 1tagvideo.mp4 and run it. 
1a.py detects the corners of the tag that is tag detection
---------------------------------------------------------------------------------------------------------------------------------
To run 1b.py, change the path on line 8, that is the location of the referecne tag image and run it.
1b.py decodes the tag and gives id and value of the tag.
---------------------------------------------------------------------------------------------------------------------------------
testudoncube.py gives the solution of part 2, 

To get the solution to 2a, that is testudo superimposition, comment the lines from 64 to 71
To get the solution to 2b, that is virtual cube superimposition, uncomment the above lines and comment the lines from 57 to 62.
---------------------------------------------------------------------------------------------------------------------------------
imageutils.py consists of the following functions:threshold, highpass, edgedetection, cornerdetection,extreme,decodetag and drawcube
mathutils.py consists of Homography,warpPerspective, and projectionMatrix
---------------------------------------------------------------------------------------------------------------------------------