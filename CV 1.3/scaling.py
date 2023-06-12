import numpy as np
import cv2 as cv

img = cv.imread('messi.jpg')
assert img is not None, "file could not be read, check with os.path.exists()"

res = cv.resize(img,None,fx=2,fy=2, interpolation = cv.INTER_CUBIC)

#OR

cv.imshow('img', img)
cv.imshow('scaled img', res)
height, width = img.shape[:2]
res = cv.resize(img,(2*width, 2*height), interpolation = cv.INTER_CUBIC)

cv.waitKey(0)
cv.destroyAllWindows()