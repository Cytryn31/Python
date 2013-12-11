import cv2
import math
import numpy as np

def draw_lines(image, p1,p2):
    
  
    cv2.line(image, p1, p2, cv2.cv.RGB(255, 255, 0))
    
    #cv2.imshow('new',lines)
    #cv2.waitKey()
    #print math.pi/2
   
    return image
     


