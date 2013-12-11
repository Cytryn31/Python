'''
SobelEdgeDetection.py
Description:
    The software will apply Sobel's Edge detection algorithm to a given image.
    The algorithm includes:
        - Gaussian Blurring
        - Sobel Filter
        - Thresholding
    
Input:
    - gS <gaussSigma> (float)
    - gW <gaussWindow> (int)
    - T  <threshold>   (int)
    
Output:
    - blurred_im (np.array)
    - grad_x (np.array)
    - grad_y (np.array)
    - edge_im (np.array)
    
Usage:
    From command line:   python SobelEdgeDetection.py <image>
    
@author: Edoardo Foco
'''

import numpy as np
import cv2
import sys

import Filters


def main():
    
    image = validateInput()
    
    t = True
    while(t):
        try:
            sigma = float(raw_input("\nInsert Gauss Sigma:\n"))
            t = False
        except ValueError:
            print "\n**Error: Parameter.\n Specified sigma is not a float or an int\n"
            
    t = True
    while(t): 
        try:
            win_size = int(raw_input("\nInsert Window size:\n"))
            t = False
        except ValueError:
            print "\n**Error: Parameter.\nSpecified window size is not an int\n"
            
        if not win_size == 3: 
            if not win_size == 5:
                if not win_size == 7:
                    print "\n**Error: Parameter Error.\nThe dimensions of the gaussian window are not supported.\nSupported values for the windows are: 3, 5, 7\n"
                    t = True
    t = True
    while(t):
        try:
            threshold = int(raw_input("\nInsert Threshold Value:\n"))
            t = False
        except ValueError:
            print "\n**Error: Parameter.\nSpecified threshold is not an int\n"
            
        
    # compute filters
    blurred_im, grad_x, grad_y = applyFilters(image, sigma, win_size)
    
    # calculate gradient
    grad = np.hypot(grad_y,grad_x)
    
    # binarise image
    edge_im = binarise(grad,threshold)
    
    # show results
    showResults(image, blurred_im,grad_x,grad_y,edge_im)
    
    sys.exit()

def validateInput():
    if not len(sys.argv) == 2:
        print "\n**Error: Invalid arguments.\nUsage: \npython SobelEdgeDetection.py <filename>\n"
        sys.exit()

    # getting input
    image_str = sys.argv[1]
   
    if image_str == "-h":
        print "\nUsage:\npython SobelEdgeDetection.py <filename>\n"
        print "Supported File Formats: .png\n"
        print "The system is going to compute the Sobel Edge Detection algorithm on the image\n"
        sys.exit()
        
    length = len(image_str) - 4
    file_extension = image_str[length:]
    
    if not file_extension == ".png":
        print "\n**Error: Invalid file type.\nThe software supports only .png files"
        sys.exit()
    
    image = cv2.imread(image_str, cv2.CV_LOAD_IMAGE_GRAYSCALE)
    if image == None:
        print "\n**Error: File not found\n"
        sys.exit()
    
    if not image.shape[0] == 480:
        if not image.shape[1] == 640:
            print "\n**Error: Size of the image is not supported.\nSupported size: 640x480\n"
            sys.exit()
    
    return image

def applyFilters(image, sigma, win_size):
    '''
    Apply Gaussian Blur and Sobel filter
    '''
    blurred_im = Filters.gaussFilter(image, sigma, win_size)
    grad_x,grad_y = Filters.sobelFilter(blurred_im)
    return blurred_im, grad_x, grad_y


def binarise(grad,threshold):
    x0,y0 = np.where(grad > threshold)
    x1,y1 = np.where(grad < threshold)
    grad[x0,y0] = 1
    grad[x1,y1] = 0
    edge_im = grad
    
    return edge_im

def showResults(image, blurred_im, grad_x, grad_y, edge_im):
    cv2.imshow('original_im', image)
    blurred_im = blurred_im.astype(np.uint8)
    cv2.imshow('blurred_im',blurred_im)
    cv2.imshow('grad_x',grad_x)
    cv2.imshow('grad_y',grad_y)
    cv2.imshow('edge_im',edge_im)
    cv2.waitKey()



if __name__ == '__main__':
    main()