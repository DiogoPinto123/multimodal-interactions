import cv2 as cv
import numpy as np

image = cv.imread('test.jpg')

bilateral_filter = cv.bilateralFilter(src=image, d=9, sigmaColor=75, sigmaSpace=75)

cv.imshow('Original', image)
cv.imshow('Bilateral Filtering', bilateral_filter)
 
cv.waitKey(0)
cv.imwrite('bilateral_filtering.jpg', bilateral_filter)
cv.destroyAllWindows()