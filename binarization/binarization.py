'''
Created on Feb 27, 2013

@author: Edoardo Foco
'''
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

# Loading image with cv2
im_gray = cv2.imread('1_1_gray.png', cv2.CV_LOAD_IMAGE_GRAYSCALE)

# Applying Otsu's Algorithm for threshold discovery and Binarizing
(thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    
# Saving Binarized Image
cv2.imwrite('bw_image.png', im_bw)



# Calculating Histogram
im_bin = cv2.imread('bw_image.png')
plt.hist(im_bin.flatten(), 256, range=(0, 1), fc='k')
plt.show()
# Displaying Binarized Image

cv2.imshow("window", im_bw)
im_bin = cv2.imread('bw_image.png')
cv2.waitKey()

#im2,cdf = imtools.histeq(im)

#im2.show();
#if im2.ndim==2:
#    print '2D'
    

#plt.hist(img.flatten(), 256, range=(0, 250), fc='k')

#plt.hist(img.flatten(), 256,  fc='k')
#plt.show()