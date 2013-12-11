
'''
Created on Feb 28, 2013

@author: Edoardo Foco

Description: 
    Normalizing 0 - 255 initial fingerprint image to a 0 - 1 value image. 
'''

import cv2
import numpy as np


def normalise(image):
    
    dbl_image = image.astype(float)


    # finding mean and standard deviation
    mean_stddev = cv2.meanStdDev(dbl_image) 
    required_mean = 0
    required_stddev = 1
    
    # applying normalization
    norm_im = dbl_image - mean_stddev[0]
    norm_im = norm_im/mean_stddev[1]
    norm_im = required_mean + norm_im*np.sqrt(1/required_stddev)
    
    #cv2.imshow('hi', norm_im)
    #cv2.waitKey()
   
   
    return norm_im
