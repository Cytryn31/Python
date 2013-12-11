
'''
MeanStd_Norm.py
Description: 
    Normalizing 0 - 255 initial fingerprint using Hong et al approach. 
     
    Input:
        -image
    
    Output:
        -norm_im

@author: Edoardo Foco
'''

import cv2
import numpy as np


def normalise(image):
   
    dbl_image = image.astype(float)
    norm_im = dbl_image

    # finding mean and standard deviation
    # Note: mean_stddev is a tuple where: mean = mean_stddev[0], std = mean_stddev[1]
    meanStd = cv2.meanStdDev(dbl_image)    
    required_mean = 0
    required_stddev = 1
    
    # mapping coordinates where pixel is more or less than mean
    x0,y0 = np.where(norm_im >= meanStd[0])
    x1,y1 = np.where(norm_im < meanStd[0])
    
    # computing normalization
    norm_im = dbl_image - meanStd[0]
    norm_im = norm_im**2
    norm_im = norm_im/meanStd[1]
    
    # separating foreground from background
    if meanStd[1] > 20:
        norm_im[x0,y0] = required_mean + np.sqrt(required_stddev*norm_im[x0,y0]) 
        norm_im[x1,y1] = required_mean - np.sqrt(required_stddev*norm_im[x1,y1])
            
    else:
        norm_im[x1,y1] = 1 # 1 is the maximum desired value
        norm_im[x0,y0] = 1
   
    return norm_im
