import cv2 as cv
import numpy as np

image = cv.imread('test.jpg')
cv.imshow('Original', image)

# Identity
kernel1 = np.array([[0, 0, 0],
                    [0, 1, 0],
                    [0, 0, 0]])

identity_image = cv.filter2D(src=image, ddepth=-1, kernel=kernel1)

cv.imshow('Identity', identity_image)
cv.imwrite('identity.jpg', identity_image)

# Blurring
kernel2 = np.ones((5, 5), np.float32) / 25
blurred_image = cv.filter2D(src=image, ddepth=-1, kernel=kernel2)

cv.imshow('Kernel Blur', blurred_image)
cv.imwrite('blurred.jpg', blurred_image)

# Gaussian Blurring
gaussian_blurred_image = cv.GaussianBlur(src=image, ksize=(5,5), sigmaX=0, sigmaY=0)

cv.imshow('Gaussian Blurred', gaussian_blurred_image)
cv.imwrite('gaussian_blurred.jpg', gaussian_blurred_image)

# Median Blurring
median_blurred_image = cv.medianBlur(src=image, ksize=5)

cv.imshow('Median Blurred', median_blurred_image)
cv.imwrite('median_blurred.jpg', median_blurred_image)

# Sharpening

kernel3 = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])

sharpened_image = cv.filter2D(src=image, ddepth=-1, kernel=kernel3)

cv.imshow('Sharpened', sharpened_image)
cv.imwrite('sharpened.jpg', sharpened_image)

cv.waitKey()
cv.destroyAllWindows()