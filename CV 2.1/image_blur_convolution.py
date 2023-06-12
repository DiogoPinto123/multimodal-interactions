import cv2 as cv
import numpy as np

image = cv.imread('test.jpg')

kernel1 = np.ones((5, 5), np.float32) / 25
img = cv.filter2D(src=image, ddepth=-1, kernel=kernel1)

cv.imshow('Original', image)
cv.imshow('Kernel Blur', img)

cv.waitKey()
cv.imwrite('blur_kernel.jpg', img)
cv.destroyAllWindows()