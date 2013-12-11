import numpy as np
import cv2
from scipy import ndimage

import resize
import math
import draw_lines2


def calc_orient(image):
    #image = cv2.imread('test_window.png', cv2.CV_LOAD_IMAGE_GRAYSCALE)
    #image = resize.resize_img(image)
    #dbl_image = image.astype(float)
    #cv2.imshow('orginal', image)
    
    smoothed_im = cv2.GaussianBlur(image,(3,3), 0) # gaussian blur using 3x3 window
   
    dx = ndimage.sobel(smoothed_im, 0)  # horizontal sobel gradient
    dy = ndimage.sobel(smoothed_im, 1)  # vertical sobel gradient
    
    max_dx = np.max(dx)-np.min(dx)
    max_dy = np.max(dy)-np.min(dy)
   
   # print max_dx
    #print max_dy
    
    theta = math.atan2(max_dy,max_dx) # in radians
    print 'grad',theta
   
    #cv2.imshow('dx',dx)
    #cv2.waitKey()
    
    orientation_im = draw_lines.draw_lines(image, theta)
    
    return orientation_im
    
    #print dx.shape[0],dx.shape[1]
    #print dx
    #print 'hello',dy
#calc_orient()
    