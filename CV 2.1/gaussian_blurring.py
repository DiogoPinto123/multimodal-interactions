import cv2 as cv

image = cv.imread('test.jpg')

# sigmaX is Gaussian Kernel standard deviation
# ksize is kernel size
gaussian_blur = cv.GaussianBlur(src=image, ksize=(5,5), sigmaX=0, sigmaY=0)

cv.imshow('Original', image)
cv.imshow('Gaussian Blurred', gaussian_blur)

cv.waitKey()
cv.imwrite('gaussian_blue.jpg', gaussian_blur)
cv.destroyAllWindows()