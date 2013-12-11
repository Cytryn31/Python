'''
Created on April 2, 2013

SobelEdgeDetection.py
Description:
    The software will apply Sobel's Edge detection algorithm to a given image.
    The algorithm includes:
        - Gaussian Blurring
        - Sobel Filter
        - Thresholding
    
Input:
    - gS <gaussSigma> (float)
    - gW <gaussWindow> (int)
    - T  <threshold>   (int)
    
Output:
    - original_im (np.array)
    - blurred_im (np.array)
    - grad_x (np.array)
    - grad_y (np.array)
    - edge_im (np.array)
    

Note:
Still needs to be tested throughly

@author: Edoardo Foco
'''

import numpy as np
import cv2
import sys

import Filters



if __name__ == '__main__':
    pass

if len(sys.argv) > 8 or len(sys.argv) < 8:
    print "\n**Error: Invalid arguments.\nUsage: python SobelEdgeDetection.py -gS <gaussSigma> -gW <gaussWindow> -T <threshold> <filename>"
    sys.exit()

# getting input
image_str = sys.argv[7]
sigma = float(sys.argv[2])
win_size = int(sys.argv[4])
threshold = int(sys.argv[6])

length = len(image_str) - 4
file_extension = image_str[length:]

if not file_extension == ".png":
    print "**Error: Invalid file type.\nThe software supports only .png files"
    sys.exit()
    
image = cv2.imread(image_str, cv2.CV_LOAD_IMAGE_GRAYSCALE)

blurred_im = Filters.gaussFilter(image, sigma, win_size)
grad_x,grad_y = Filters.sobelFilter(blurred_im)

# calculate grad
grad = np.hypot(grad_y,grad_x)
# calculate theta
theta = np.arctan2(grad_y, grad_x)
# binarize
x0,y0 = np.where(grad > threshold)
x1,y1 = np.where(grad < threshold)
grad[x0,y0] = 1
grad[x1,y1] = 0

edge_im = grad

# show results
cv2.imshow('original_im', image)

blurred_im = blurred_im.astype(np.uint8)
cv2.imshow('blurred_im',blurred_im)
cv2.imshow('grad_x',grad_x)
cv2.imshow('grad_y',grad_y)
cv2.imshow('edge_im',edge_im)

cv2.waitKey()