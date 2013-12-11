import numpy as np
import cv2
from scipy import ndimage

import resize
import math
import draw_lines2


def calc_orient(image):
    #image = cv2.imread('test_window2.png', cv2.CV_LOAD_IMAGE_GRAYSCALE)
    #image = resize.resize_img(image)
    #dbl_image = image.astype(float)
    #cv2.imshow('orginal', image)
    
    smoothed_im = cv2.GaussianBlur(image,(3,3), 0) # gaussian blur using 3x3 window
   
    dx = ndimage.sobel(smoothed_im, 0)  # horizontal sobel gradient
    dy = ndimage.sobel(smoothed_im, 1)  # vertical sobel gradient
    print dy
    theta_mx = np.array([[]])
    for y in range(0,len(dy)):
        for x in range(0,len(dx)):
            theta_mx[x][y] = math.atan2(dy[y],dx[x])
            
    #theta =  # in radians
    print theta_mx
    
     
    #cv2.imshow('dx',dx)
    #cv2.waitKey()
    
    lines_im = draw_lines2.draw_lines(image, theta, 1)
    #print lines_im
    
    return lines_im
    #print dx.shape[0],dx.shape[1]
    #print dx
    #print 'hello',dy
#calc_orient()
    