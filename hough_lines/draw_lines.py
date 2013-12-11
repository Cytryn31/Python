import cv2
import math
import numpy as np

def draw_lines(image, theta):
    
    alpha = math.degrees(theta)
    
    beta = theta - math.pi/2
    
    x_component = math.cos(theta) * 1000
    y_component = math.sin(theta) * 1000
   # math.asin(beta)
    #x_diff = 1 = x_component
    x_diff = 1 - x_component
    
    y_diff = 1 - y_component
    
    
    point1_x = np.around(8 - x_component)
    point1_x = point1_x.astype(int) 
    point1_y = np.around(8 - y_component)
    point1_y = point1_y.astype(int)
    point1 = (point1_x,point1_y)
    
    point2_x = np.around(8 + x_component)
    point2_x = point2_x.astype(int) * 2
    point2_y = np.around(8 + y_component) * 2
    point2_y = point2_y.astype(int)
    
    point2 = (point2_x, point2_y)
    print point1,point2
     
    cv2.line(image, point1, point2, (255, 255, 255))
    
    #cv2.imshow('new',image)
    #cv2.waitKey()
    
    return image
    #print math.pi/2
   
    


