import cv2
import numpy as np
"""
basic document scanner:
1. Detect
2. Use edges to find the counter of the peice of paper
3. Apply a perspective transform to obtain the to-down view
"""

# PART 1
#Load image
#convert image to grayscale to simplify edge detection and other operations
#Use algorithim to identify sharp changes in intesity, whcih typically correspond to edges of the doc

#PART 2
#Locate contours(the outlines of the object), find all the coutnours of the image
#Use geometry to isolat the quadrilateral that represents the document

#PART 3
#Rearange the detected points so they correspond to the conrer of the paper
#Map these points to a rectangle to "Flatten" the doc into a clean top-down view
