
'''
WikiNorm.py
Description: 
    Normalizing 0 - 255 initial fingerprint image to a 0 - 1 value image using
    normalization formula suggested by Wikipedia.
 
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
    
    # computing normalization
    currentMin = np.min(dbl_image)
    currentMax = np.max(dbl_image)
    currentRange = currentMax - currentMin
    newMin = 0
    newMax = 1
    newRange = newMax - newMin
    
    # calculating mean and standard deviation
    meanStd = cv2.meanStdDev(dbl_image)
    
    norm_im = dbl_image
    # regions with a low standard deviation are assumed to NOT be regions of interest and 
    # have values close to currentMax therefore their value is set to the brightest possible -> 1
    if meanStd[1]>20:
        
        norm_im = (dbl_image - currentMin)*(newRange / currentRange)
        
    elif meanStd[1]<=20:
        
        norm_im = norm_im / currentMax
    
    return norm_im

