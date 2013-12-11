import numpy as np
from numpy import pi
import scipy.ndimage as ndi
import cv2
import math


def non_maximal_edge_suppresion(mag, orient):
    """Non Maximal suppression of gradient magnitude and orientation."""
    # bin orientations into 4 discrete directions
    abin = ((orient + pi) * 4 / pi + 0.5).astype('int') % 4
    #print orient
    
    mask = np.zeros(mag.shape, dtype='bool')
    mask[1:-1,1:-1] = True
    edge_map = np.zeros(mag.shape, dtype='bool')
    offsets = ((1,0), (1,1), (0,1), (-1,1))
    for a, (di, dj) in zip(range(4), offsets):
        cand_idx = np.nonzero(np.logical_and(abin==a, mask))
        for i,j in zip(*cand_idx):
            if mag[i,j] > mag[i+di,j+dj] and mag[i,j] > mag[i-di,j-dj]:
                edge_map[i,j] = True
   # print edge_map
    return edge_map


def canny_edges(image, sigma=1.0, low_thresh=10, high_thresh=20):
    """Compute Canny edge detection on an image."""
    image = ndi.filters.gaussian_filter(image, sigma)
    dx = ndi.filters.sobel(image,0)
    dy = ndi.filters.sobel(image,1)

    mag = np.sqrt(dx**2 + dy**2)
    ort = np.arctan2(dy, dx)
    
    

    edge_map = non_maximal_edge_suppresion(mag,ort)
    
    
    max_points = []
    counter = 0
    for y in range(edge_map.shape[1]):
        for x in range(edge_map.shape[0]):
            if edge_map[x][y] == True:
                max_points.append((x,y))
                #cv2.line(image, point1, point2, cv2.cv.RGB(255, 255, 0))
    #if np.any(orient_im) == 1:
    #    print 'yes'
        
    print max_points
    
    for coordinates in max_points:
        '''draw lines'''
        p = coordinates
        print p
        
        x1 = p[0] - math.cos(ort[p[0]][p[1]])
        x1 = np.around(x1)
        x1 = x1.astype(int)
        y1 = p[1] - math.sin(ort[p[0]][p[1]])
        y1 = np.around(y1)
        y1 = y1.astype(int)
        
        x2 = p[0] + math.cos(ort[p[0]][p[1]])
        x2 = np.around(x2)
        x2 = x2.astype(int)
        y2 = p[1] + math.sin(ort[p[0]][p[1]]) 
        y2 = np.around(y2)
        y2 = y2.astype(int)
         
        point1 = (x1,y1)
        point2 = (x2,y2)
        #print point1,point2
        cv2.line(image, p, p, cv2.cv.RGB(0, 0, 0))
    
    cv2.imshow('0',image)
    cv2.waitKey()
    edge_map = np.logical_and(edge_map, mag > low_thresh)
    
    #cv2.imshow('low_thresh',edge_map)
    #cv2.waitKey()
    labels, num_labels = ndi.measurements.label(edge_map, np.ones((3,3)))
   # print num_labels
    for i in range(num_labels):
        #print 'hi',i,'equals',max(mag[labels==i]) 
        if max(mag[labels==i]) < high_thresh:
            edge_map[labels==i] = False
    #cv2.imshow('low_thresh',edge_map)
    #cv2.waitKey()
    return edge_map


if __name__ == "__main__":
    image = cv2.imread('1_1.png', cv2.CV_LOAD_IMAGE_GRAYSCALE)
    #(thresh, image) = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    from matplotlib.pyplot import imshow, gray, show
    imshow(canny_edges(image))
    gray()
    show()

