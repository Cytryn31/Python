'''
ThreadController.py
Description:
    This class creates a thread controller which will takes as an input an image fragmenting it, then 
    spawnining a pool of threads to process it, and finally reconstructing it.
    
Input:
    -Image
Output:
    -orient_im : The Orientation Image needed for the Gabor filter
    -final_im : An normalized image representing the orientation through the use of lines

@author: Edoardo Foco
'''

import numpy as np
import Queue
import BlockThread

class ThreadController:
    
        
    def __init__(self,image):
        self.image = image
        self.windows = {}       #dictionary of windows controls input
        self.n_windows = {}     #dictionary of resulting windows controls output
        self.o_windows = {}     #dictionary of resulting oriented windows controls output
        self.window_height = 16 
        self.window_width = 16 
        
    
    def start_threading(self):
        '''Segments the image in windows of size 16x16, saves the windows in a queue then sends 
            each element to a thread which processes it
        '''
     
        # initialize queue
        queue = Queue.Queue()
        
        currentx = 0
        currenty = 0
        
        # create windows
        count = 0
        for y in range (0,self.image.shape[0]/self.window_height): 
            currentx = 0
            for x in range(0,self.image.shape[1]/self.window_width): 
                self.windows[count]=self.image[currenty:currenty+self.window_height,currentx:currentx+self.window_width]
                currentx += self.window_width
                count += 1
                
            currenty += self.window_height
       
        # spawn pool of threads passing the queue object, this allows for threads to
        # recurrently analyze queue objects.
        for i in range(2): # change range to change number of threads
            t = BlockThread.BlockThread(queue,self.n_windows,self.o_windows)
            t.setDaemon(True)
            t.start()
        
        # insert windows in the queue   
        new_windows = self.windows.items()
        for window in new_windows:
            queue.put(window)
    
    
        queue.join()
              
        
    def reconstruct_image(self):
        ''' Re-constructs Processed Images '''
       
        stacked_rows =[]
        o_stacked_rows = []
         
        counter=0
        
        # constructing rows by stacking the windows horizontally
        for y in range (0,self.image.shape[0]/self.window_height):  
            row = []
            o_row = []
            for x in range (0,self.image.shape[1]/self.window_width):
                if x == 0:
                    row = self.n_windows[counter]
                    o_row = self.o_windows[counter]
                    counter +=1
                else: 
                    row=np.hstack((row,self.n_windows[counter]))
                    o_row = np.hstack((o_row, self.o_windows[counter]))
                    counter += 1
                
                if x == self.image.shape[1]/self.window_width - 1:
                    stacked_rows.append(row)
                    o_stacked_rows.append(o_row)
        
        # constructing columns by stacking the rows vertically
        counter = 0
        for x in range (len(stacked_rows)):  
                if counter == 0:
                    final_im=stacked_rows[0] # creating final image
                    orient_im = o_stacked_rows[0]
                    counter+=1
                else:
                    final_im=np.vstack((final_im,stacked_rows[x]))
                    orient_im = np.vstack((orient_im,o_stacked_rows[x]))
        
        return orient_im, final_im 
    