
'''
IplNorm.py
Description: 
    Normalizing 0 - 255 initial fingerprint to a normalized image.
    Using energy normalization.
    
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
    # calculate the mean of the image.
    mean = np.mean(dbl_image)
    
    # converting numpy 8-bit image to 8- bit cv2.iplimage
    iplImage = cv2.cv.CreateImageHeader((image.shape[1], image.shape[0]), cv2.cv.IPL_DEPTH_8U, 1)
    cv2.cv.SetData(iplImage, image.tostring(), image.dtype.itemsize * 1 * image.shape[1])
    
    # initializing 32-bit floating point iplimage
    image_32F = cv2.cv.CreateImage(cv2.cv.GetSize(iplImage), cv2.cv.IPL_DEPTH_32F,1)
 
    # converting 8-bit unsigned integer image to 32-bit floating point image
    cv2.cv.CvtScale(iplImage,image_32F)
   
    # energy Normalization. Formula: image = image/mean(image)
    cv2.cv.ConvertScale(image_32F, image_32F, (1/mean), 0);
     
    # re-converting to numpy image
    norm_im = np.asarray(image_32F[:,:])
   
    return norm_im