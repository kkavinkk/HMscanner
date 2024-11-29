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

#load image
image = cv2.imread('TestImage.jpg')
#gray scale image
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#blur to reduce noise
blurred_image = cv2.GaussianBlur(grayscale_image, (5, 5), 0)
#edge detection
edges = cv2.Canny(blurred_image, 30, 120)

#PART 2
#Locate contours(the outlines of the object), find all the coutnours of the image
#Use geometry to isolat the quadrilateral that represents the document

#find contours
contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

#Only keep the largest contours
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:5]

document_contour = None

#use a loop to find a quadrilateral
for contour in contours:
    perimeter = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)

    if len(approx) == 4:
        document_contour = approx
        break

#PART 3
#Rearange the detected points so they correspond to the conrer of the paper
#Map these points to a rectangle to "Flatten" the doc into a clean top-down view

#PART 4
#view result
#if document_contour is not None:
  
cv2.drawContours(image, [document_contour], -1, (0, 255, 0), 3)
cv2.namedWindow('Document Detected', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Document Detected', 800, 1100)
cv2.imshow('Document Detected', image)
cv2.waitKey(0)

cv2.destroyAllWindows()
"""
NOT DETECTING EDGES PROPERLY
"""

