import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('first.jpg')

cv2.imshow('image',img)
cv2.waitKey(0)
px = img[100,100]
print px
print img.size
