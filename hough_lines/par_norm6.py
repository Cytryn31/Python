
'''
Created on Feb 28, 2013

@author: Edoardo Foco

Description: 
    Parallel normalization using a pool of threads and controlling their output
    using dictionary data-structure. Optimized for a 256x338 image. This function
    splits the image in windows of size 16x13 organizing them in a queue. The queue
    is then processed by the threads, the final result is a normalized image.
    
    Input:
        image - grayscale image 
    
    Output:
        norm_im - normalized image
        
    Notes:
        This function performs worst than the normal block approach. This function
        should be tested on more processors.

'''


import cv2
import numpy as np
import Queue
import threading
import time
from scipy import ndimage


import normalization6
#import hough_lines
import ridge_orientation2



# Creating shared memory for threads, dictionary data-structure
n_windows = {}
h_windows = {}


#  //--------------  Thread  -------------//
class ThreadRow(threading.Thread):

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            
            # grabs row from queue
            dict_row = self.queue.get()
            
            print 'Threead', threading.currentThread().getName()
          
            # Normalization
            # Note: dict_row is a tuple [key, value], using dictionary data-structure
            #n_windows[dict_row[0]] = normalization6.normalise(dict_row[1])
            n_windows[dict_row[0]] = ridge_orientation2.calc_orient(dict_row[1])
            
            # signals queue job is done
            self.queue.task_done()
     

# //-------------- Function -------------//

def parallel_normalization():
    
    
    image = cv2.imread('1_1.png', cv2.CV_LOAD_IMAGE_GRAYSCALE)
    # Applying Otsu's Algorithm for threshold discovery and Binarizing
    #(thresh, image) = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    
    cv2.imshow('window', image)
    cv2.waitKey()

    window_height = 13
    window_width = 16
    currentx = 0
    currenty = 0
    windows={}
    row_count = 0
    
    # create windows
    for y in range (0,26):
        currentx = 0
        for x in range(0,16):
            windows[row_count]=image[currenty:currenty+window_height,currentx:currentx+window_width]
            currentx += window_width
            row_count += 1
            
        currenty += window_height
    

    
   
    # initialize queue
    queue = Queue.Queue()
    
       
    # create pool of threads passing the queue object, this allows for threads to
    # recurrently analyze queue objects. Allows to create as many threads as you want
    start = time.time()
    for i in range(1): # change range to change number of threads
        t = ThreadRow(queue)
        t.setDaemon(True)
        t.start()
    

    # insert data in the queue   
    new_windows = windows.items()
    for window in new_windows:
        queue.put(window)
        
   
    # join operation waits until every element in the queue has been processed and
    # then joins the result     
    queue.join()
          
    
    
    
    # //-------- re-constructing image ----------//
    stacked_rows =[] 
    counter=0
    
    
    #print n_windows
    for y in range (0,26):  # creating array of rows
        row = []
        for x in range (0,16):
            if x == 0:
                row = n_windows[counter]
                counter +=1
            else: 
                row=np.hstack((row,n_windows[counter]))
                counter += 1
            
            if x == 15:
                stacked_rows.append(row)
    #print stacked_rows     
    counter = 0
    for x in stacked_rows:  # creating final image
            if counter == 0:
                norm_im=stacked_rows[0]
                counter+=1
            else:
                norm_im=np.vstack((norm_im,x))
        
    print "Elapsed Time: %s" % (time.time() - start)
    
    
    # //----------- Getting Mask ---------//
    #print norm_im
    
    cv2.imshow('im', norm_im)
    cv2.waitKey()
    
    return norm_im

    
parallel_normalization()

