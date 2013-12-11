from scipy import ndimage, misc
import numpy
import cv2

def canny():
    
    
    image = cv2.imread('1_1.png', cv2.CV_LOAD_IMAGE_GRAYSCALE)
    #image = misc.lena()
    
    # apply gaussian blur 3x3 sigma 0.5
    smoothed_im = cv2.GaussianBlur(image,(3,3), 0)
    
    # calculate gradients with sobel filter
    grad_x = ndimage.sobel(image, 0)
    grad_y = ndimage.sobel(image, 1)
    
    # calculate magnitude
    grad_mag = numpy.sqrt(grad_x**2+grad_y**2)
    
    # calculating theta
    grad_angle = numpy.arctan2(grad_y, grad_x)
    
    # quantize angles 0 to 3 
    quantized_angle = numpy.around(3 * (grad_angle + numpy.pi) /  (numpy.pi * 2))
    
    # non-maximal suppression
    # quantize magnitude into 4 directions
    
    #NE = ndimage.maximum_filter(grad_mag, footprint=_NE)
    
   
    #cv2.imshow('grad_x',grad_x)
    #cv2.imshow('grad_y',grad_y)
    #cv2.imshow('grad_mag',grad_angle)
    cv2.waitKey()
    
canny()