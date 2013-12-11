''' file name : sobel.py

Description : This sample shows how to find derivatives of an image

This is Python version of this tutorial : http://opencv.itseez.com/doc/tutorials/imgproc/imgtrans/sobel_derivatives/sobel_derivatives.html#sobel-derivatives

Level : Beginner

Benefits : Learn to use Sobel and Scharr derivatives

Usage : python sobel.py 
'''

import cv2
import numpy as np
import math

scale = 1
delta = 0
ddepth = cv2.CV_16S

img = cv2.imread('1_1.png')
img = cv2.GaussianBlur(img,(3,3),0.5)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Gradient-X
grad_x = cv2.Sobel(gray,ddepth,1,0,ksize = 3, scale = scale, delta = delta,borderType = cv2.BORDER_DEFAULT)
#grad_x = cv2.Scharr(gray,ddepth,1,0)
print grad_x
cv2.imshow('grx', grad_x)
# Gradient-Y
grad_y = cv2.Sobel(gray,ddepth,0,1,ksize = 3, scale = scale, delta = delta, borderType = cv2.BORDER_DEFAULT)
#grad_y = cv2.Scharr(gray,ddepth,0,1)

abs_grad_x = cv2.convertScaleAbs(grad_x)   # converting back to uint8
abs_grad_y = cv2.convertScaleAbs(grad_y)

#dst = cv2.addWeighted(abs_grad_x,0.3,abs_grad_y,0.3,0)
dst = cv2.add(abs_grad_x,abs_grad_y)

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

theta_mx = grad_x
grad_mag = grad_x
# creating array of theta's and magnitudes
for x in range (grad_x.shape[0]):
    for y in range (grad_x.shape[1]):
        if not grad_x[x][y]== 0:
            theta_mx[x][y] = math.atan2(grad_y[x][y],grad_x[x][y])
            grad_mag[x][y] = math.sqrt(grad_x[x][y]**2 + grad_y[x][y]**2)
            
            print theta_mx[x][y]
            
        else:
            theta_mx[x][y] = 0

print 'hi',grad_mag
cv2.imshow('grad',grad_mag)
cv2.waitKey()

local_mx = cv2.Sobel(grad_mag,ddepth,0,1,ksize = 3, scale = scale, delta = delta, borderType = cv2.BORDER_DEFAULT)
print local_mx.shape[0],local_mx.shape[1]

#for y in range (grad_mag.shape[0]):
#    for x in range (grad_mag.shape[1]):
 #       if grad_mag[x][y]

#print theta_mx

# To see the results, vis