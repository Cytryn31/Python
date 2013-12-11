'''
@author: Edoardo Foco
Date: 28 March 2013
'''

import numpy as np
import Queue

import BlockThread


class ThreadController:
    
        
    def __init__(self,image):
        self.image = image
        self.windows = {}       #dictionary of windows
        self.n_windows = {}     #dictionary of resulting windows
      
        
    
    def start_threading(self):
        '''Segments the image in windows of size 16x16 then sends 
            each windows to a thread which processes the window
        '''
     
        # initialize queue
        queue = Queue.Queue()
        
        
        window_height = 16 #13
        window_width = 16 #16
        currentx = 0
        currenty = 0
        
        # create windows
        count = 0
        for y in range (0,12): 
            currentx = 0
            for x in range(0,12): 
                self.windows[count]=self.image[currenty:currenty+window_height,currentx:currentx+window_width]
                currentx += window_width
                count += 1
                
            currenty += window_height
       
        # create pool of threads passing the queue object, this allows for threads to
        # recurrently analyze queue objects. Allows to create as many threads as you want
        for i in range(4): # change range to change number of threads
            t = BlockThread.BlockThread(queue,self.n_windows)
            t.setDaemon(True)
            t.start()
        
    
        # insert windows in the queue   
        new_windows = self.windows.items()
        for window in new_windows:
            queue.put(window)
    
    
        queue.join()
              
        
    def reconstruct_image(self):
        ''' Re-constructs Processed Image '''
       
        stacked_rows =[] 
        counter=0
        
        # constructing rows by stacking the windows horizontally
        for y in range (0,12):  
            row = []
            for x in range (0,12):
                if x == 0:
                    row = self.n_windows[counter]
                    counter +=1
                else: 
                    row=np.hstack((row,self.n_windows[counter]))
                    counter += 1
                
                if x == 11:
                    stacked_rows.append(row)
        
        # constructing columns by stacking the rows vertically
        counter = 0
        for x in stacked_rows:  # creating final image
                if counter == 0:
                    final_im=stacked_rows[0]
                    counter+=1
                else:
                    final_im=np.vstack((final_im,x))
            
        #cv2.imshow('im', final_im)
       # cv2.waitKey()
        
        return final_im
    
        
    
