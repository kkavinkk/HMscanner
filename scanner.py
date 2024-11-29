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
image = cv2.imread('TestImage.jpg')

"""
OPENS ORIGINAL IMAGE55
cv2.namedWindow('Original', cv2.WINDOW_NORMAL)  # Allow manual resizing
cv2.resizeWindow('Original', 800, 1100)  
cv2.imshow('Original', image)
cv2.waitKey(0)
"""

grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.namedWindow('Grayscale', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Grayscale', 800, 1100)
cv2.imshow('Grayscale', grayscale_image)
cv2.waitKey(0)

cv2.destroyAllWindows()



#PART 2
#Locate contours(the outlines of the object), find all the coutnours of the image
#Use geometry to isolat the quadrilateral that represents the document

#PART 3
#Rearange the detected points so they correspond to the conrer of the paper
#Map these points to a rectangle to "Flatten" the doc into a clean top-down view
