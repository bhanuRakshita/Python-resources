import cv2 # opencv library
import numpy as np # numpy library

# read the image
image = cv2.imread("medicine.jpg")

# convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# threshold the image
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# find the contours
contours,_ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# loop over the contours
for contour in contours:
    # get the bounding rectangle
    [x, y, w, h] = cv2.boundingRect(contour)

    # discard areas that are too large
    if h > 300 and w > 300:
        continue

    # discard areas that are too small
    if h < 40 or w < 40:
        continue

    # draw the bounding rectangle
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# display the image 
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()