'''
Created on April 2, 2013

GaussianFilter.py


'''

import numpy as np
from scipy.signal import convolve2d as conv


def gaussFilter(image,sigma,window):
    '''
    Description:
        This function will execute a Gaussian Blurring Filter on the given image. The sigma and window size
        are set to default sigma = 2 and window = 5x5. 
    
    Input:
        -image (np.array)
        -sigma (int)
        -window size (int)
    
    Output:
        - blurred_im (np.array)
    '''
    # creating an empty kernel
    kernel = np.zeros((window,window))
    # centre of the kernel
    c0 = window // 2 
    
    # computing kernel using Gaussian function
    for x in range(window):
            for y in range(window):
                r = np.hypot((x-c0),(y-c0)) #calculating magnitude of the centre pixel. x^2 + y^2
                val = (1.0/2*np.math.pi*sigma*sigma)*np.math.exp(-(r*r)/(2*sigma*sigma)) # computes gaussian filter
                kernel[x,y] = val
    
    kernel = kernel / kernel.sum()
    
    # executes convolution
    blurred_im = conv(image,kernel)[1:-1,1:-1]
    
    return blurred_im



def sobelFilter(image):
    '''
    Description:
    This function will execute a Sobel Filter on the given image to find its horizontal and vertical gradients.
    The default filter is set to 3x3.
    Input:
        -image (np.array)
        
    Output:
        - grad_x (np.array)
        - grad_y (np.array)
    '''
    
    # creating sobel kernels
    fx = np.array([1, 2, 1,
                   0, 0, 0,
                   -1,-2,-1])
    fy = np.array([-1,0,1,
                   -2,0,2,
                   -1,0,1])
    
    fx = fx.reshape(3,3)
    fy = fy.reshape(3,3)
    
    grad_x = conv(image,fx)
    grad_y = conv(image,fy)
    
    return grad_x,grad_y