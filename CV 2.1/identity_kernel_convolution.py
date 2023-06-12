import cv2 as cv
import numpy as np

image = cv.imread('test.jpg')

kernel1 = np.array([[0, 0, 0],
                    [0, 1, 0],
                    [0, 0, 0]])

# ddepth is -1 is its the same depth as source image
identity = cv.filter2D(src=image, ddepth=-1, kernel=kernel1)
#or
#identity = cv.blur(src=image, ksize=(5,5))
# We should get the same image
cv.imshow('Original', image)
cv.imshow('Identity', identity)

cv.waitKey()
cv.imwrite('identity.jpg', identity)
cv.destroyAllWindows()