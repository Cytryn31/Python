'''

Orientation.py
Description:
    This function computes the orientation angles. 
    The angles are then used to determine the angle of the line that passes in each 8x8 window in the image.
    
Input:
    image - 16x16 image

Output:
    orient_im - orientation image
    final_im - image representing the orientation angles

Note:
    The author is not happy with the output of the drawing function. Although the angles
    at each pixel are calculated correctly, when it comes to drawing the lines the algorithm
    approximates an angle for each 8x8 window by making an average of the
    angles computed at each pixel in the window. This results in drawing inaccurate lines. It is to be
    noted that this does not affect the enhancement algorithm because the lines will not be considered (they are
    drawn just for resemblance) 


@author: Edoardo Foco
'''

import cv2
import numpy as np
from scipy import ndimage
import math
import Filters
from PIL import Image

class Orientation():
    
    def __init__(self,image):
        self.image = image
        
        
        
    def calculateOrientation(self):
        
        self.image = self.image
        
        # smooth image with gaussian blur
        smoothed_im = Filters.gaussFilter(self.image, 0.5, 3)
        
        # calculate gradients with sobel filter
        dx,dy = Filters.sobelFilter(smoothed_im)
        
        # smooth gradients
        Gx = Filters.gaussFilter(dx,0.5,3)
        Gy = Filters.gaussFilter(dy,0.5,3) 
        
        # compute gradient magnitude
        Gxx = Gx **2
        Gyy = Gy **2
        G = np.sqrt(Gxx + Gyy)
       
        # calculate theta
        theta = np.arctan2(Gy,Gx)
        
        # smooth theta
        smoothed_theta = Filters.gaussFilter(theta, 0.5, 3)
        
        # calculate double sine and cosine on theta --> increases precision
        Tx = (G**2 + 0.001) * (np.cos(smoothed_theta)**2 - np.sin(smoothed_theta)**2)
        Ty = (G**2 + 0.001) * (2 * np.sin(smoothed_theta) * np.cos(smoothed_theta))
        
        denom = np.sqrt(Ty**2 + Tx**2)
        
        Tx = Tx / denom
        Ty = Ty / denom
        
        # smooth theta x and y
        smoothed_Tx = Filters.gaussFilter(Tx, 0.5, 3)
        smoothed_Ty = Filters.gaussFilter(Ty, 0.5, 3)
        
        # calculate new value for theta
        theta = np.pi + np.arctan2(smoothed_Ty,smoothed_Tx)/2
    
        #draw lines
        final_im = self.decomposeImage(theta)
        return theta, final_im 
        
        
    def decomposeImage(self,theta):
        # The following code will calculate the average angle and draw lines --> it should be replaced
        # the reason is that this approximation is very inaccurate.
        # Note: this piece of code will not impact the precision of the Gabor filter. It is used
        # just to draw the lines on the orientation image. 
        windows = {}
        orient = {}
        median = {}
        row_count = 0
        window_height = 8
        window_width = 8
        currentx= 0
        currenty = 0
        
        # decomposing the window in 8 x 8 windows
        for y in range (0,2):
                currentx = 0
                for x in range(0,2):
                    windows[row_count]=self.image[currenty:currenty+window_height,currentx:currentx+window_width]
                    orient[row_count]=theta[currenty:currenty+window_height,currentx:currentx+window_width]
                    
                    currentx += window_width
                    row_count += 1
                    
                currenty += window_height
        
        # drawing lines on each 8 x 8 window
        for wins in range (0,4):
            sum = 0    
            for i in range (0,orient[wins].shape[0]):
                for j in range(0,orient[wins].shape[1]):
                    sum += orient[wins][i][j]
            
            len = 1
            if not orient[wins].shape[0] == 0:
                median[wins] = sum/orient[wins].shape[0]**2
                x1 = 4 - len/2*math.cos(median[wins]) * 10
                x1 = np.around(x1)
                x1 = x1.astype(int)
                y1 = 4 - len/2*math.sin(median[wins]) * 10
                y1 = np.around(y1)
                y1 = y1.astype(int)
                
                x2 = 4 + math.cos(median[wins]) * 10
                x2 = np.around(x2)
                x2 = x2.astype(int)
                y2 = 4 + math.sin(median[wins]) * 10
                y2 = np.around(y2)
                y2 = y2.astype(int)
                 
                point1 = (x1,y1)
                point2 = (x2,y2)
                
                x0,y0 = np.where(windows[wins]<=0.5) # values below or equal to 0 are darker regions, hence ridges 
                
                if np.any(x0):
                    cv2.line(windows[wins], point1, point2, cv2.cv.CV_RGB(255, 255, 255))
                
                
        final_image = self.reconstructImage(windows)
        return final_image
    
    
    def reconstructImage(self,windows):
        stacked_rows =[] 
        counter=0
        
        orient_im = self.image
        
        #print n_windows
        for y in range (0,2):  # creating array of rows
            row = []
            for x in range (0,2):
                if x == 0:
                    row = windows[counter]
                    counter +=1
                else: 
                    row=np.hstack((row,windows[counter]))
                    counter += 1
                
                if x == 15:
                    stacked_rows.append(row)
        #print stacked_rows     
        counter = 0
        for x in stacked_rows:  # creating final image
                if counter == 0:
                    orient_im=stacked_rows[0]
                    counter+=1
                else:
                    orient_im=np.vstack((orient_im,x))
    
        return orient_im
    
    
