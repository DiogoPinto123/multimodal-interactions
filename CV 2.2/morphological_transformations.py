import cv2 as cv
import numpy as np

img = cv.imread('j.png',0)
kernel = np.ones((5,5),np.uint8)
cv.imshow('Original', img)

# erosion
erosion = cv.erode(img, kernel, iterations = 1)
cv.imshow('Erosion', erosion)

# dilation
dilation = cv.dilate(img, kernel, iterations = 1)
cv.imshow('Dilation', dilation)

# opening (erosion followed by dilation, good for removing noise)
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
cv.imshow('Opening', opening)

# closing (dilation followed by erosion, good for closing holes inside foreground objects)
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
cv.imshow('Closing', closing)

# gradient (difference between dilation and erosion of an image)
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
cv.imshow('Gradient', gradient)

# top hat (difference between input image and opening of the image)
tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)
cv.imshow('Top Hat', tophat)

cv.waitKey(0)
cv.destroyAllWindows()