import cv2
import math
import numpy as np

def draw_lines(image, theta,rho):
    
    
    alpha = math.degrees(theta)
    
    beta = theta - math.pi
    
    
    #lines = cv2.HoughLines(image, rho, theta, 100)
    
    x1 = 8 - math.cos(beta) * 1000
    x1 = np.around(x1)
    x1 = x1.astype(int)
    y1 = 8 - math.sin(beta) * 1000
    y1 = np.around(y1)
    y1 = y1.astype(int)
    
    x2 = 8 + math.cos(beta) * 1000
    x2 = np.around(x2)
    x2 = x2.astype(int)
    y2 = 8 + math.sin(beta) * 1000
    y2 = np.around(y2)
    y2 = y2.astype(int)
     
    point1 = (x1,y1)
    point2 = (x2,y2)
    print point1,point2
    cv2.line(image, point1, point2, cv2.cv.RGB(255, 255, 0))
    
    #cv2.imshow('new',lines)
    #cv2.waitKey()
    #print math.pi/2
   
    return image
     


