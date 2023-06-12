import cv2 as cv

image = cv.imread('test.jpg')

median = cv.medianBlur(src=image, ksize=5)

cv.imshow('Original',image)
cv.imshow('Median Blurred', median)

cv.waitKey()
cv.imwrite('median_blur.jpg', median)
cv.destroyAllWindows()