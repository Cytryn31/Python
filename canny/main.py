import canny3
import cv2

image = cv2.imread('1_1.png', cv2.CV_LOAD_IMAGE_GRAYSCALE)

im = canny3.Canny('1_1.png', 1.7, 50,10)

im2 = im.grad

cv2.imshow('final',im2)
cv2.waitKey()