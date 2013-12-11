

import numpy as np
from PIL import Image
from scipy import misc
import matplotlib.pyplot

import cv2

def resize_img(image):
   
    # slicing image first two pixel columns assumed not to be relevant to the image analysis 
    sliced_border = image[:,0:2]    
    
    
    # creating border [8, 338] to be added to original image
    border=sliced_border
    for x in range (0,3):   
        border = np.hstack((border,sliced_border))

    
    # Adding the border to the original image to create a 338x256 image           
    r_image = np.hstack((border,image))
    
    
    return r_image