import cv2 as cv
import numpy as np

image = cv.imread('test.jpg')

kernel1 = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])

sharp_img = cv.filter2D(src=image, ddepth=-1, kernel=kernel1)

cv.imshow('Original', image)
cv.imshow('Sharpened', sharp_img)
     
cv.waitKey()
cv.imwrite('sharp_image.jpg', sharp_img)
cv.destroyAllWindows()