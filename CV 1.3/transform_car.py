import cv2 as cv
import numpy as np

img = cv.imread('carro.jpg')
assert img is not None, "file could not be read, check with os.path.exists()"
height, width = img.shape[:2]

# Scale image size 2x
dst = cv.resize(img,None,fx=2,fy=2, interpolation = cv.INTER_CUBIC)

cv.imwrite('carro_scale.png', dst)
# Rotate content 45 deg
M = cv.getRotationMatrix2D(((width-1)/2.0,(height-1)/2.0),45,1)
dst = cv.warpAffine(img,M,(width,height))

cv.imwrite('carro_rotation.png', dst)
# Translate content upwards 30 pixels
M = np.float32([[1,0,0],[0,1,-30]])
dst = cv.warpAffine(img, M, (width,height))

cv.imwrite('carro_translation.png', dst)
# Change perspective (zoom in the bottom and zoom out in the top)
pts1 = np.float32([[0, 202], [249, 202], [0, 0], [249, 0]])
pts2 = np.float32([[0, 202], [279, 232], [30, 0], [209, 0]])

M = cv.getPerspectiveTransform(pts1,pts2)
dst = cv.warpPerspective(img,M,(249,200))

cv.imwrite('carro_perspective.png', dst)