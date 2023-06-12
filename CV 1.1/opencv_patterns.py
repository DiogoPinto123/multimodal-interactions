import cv2 as cv

# Reading, displaying, saving images
"""
img = cv.imread('file', type)
cv.imshow('win', img)
cv.imwrite('file', img)
"""

# Interface
"""
cv.namedWindow('win', type)
cv.waitKey(ms)
cv.destroyAllWindows()
"""

# Video Capture
"""
cap = cv.VideoCapture(0)
cap.isOpened()
cap.get(id)
cap.set(id, val)
ret, frame = cap.read()
cap.release()
img2 = cv.cvtColor(img, type)
"""

# Drawing Functions
"""
cv.line(img, p0, p1, col, d)
cv.circle(img, c0, r, col, d)
cv.ellipse(img, p0, (w, h), a)
cv.polylines(img, [pts], True, col)

font = cv.FONT_
cv.putText(img, str, pos, font, size, col)
"""

# Mouse Callback
"""
cv.setMouseCallback('img', cb)
cb(evt, x, y, flags, param)
cv.createTrackbar('name', 'win', 0, max, cb)
cv.getTrackbarPos('name', 'win')
"""