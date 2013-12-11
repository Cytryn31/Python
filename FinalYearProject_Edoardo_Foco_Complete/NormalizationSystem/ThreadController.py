'''
ThreadController.py
Description:
    This class creates a thread controller which will takes as an input an image fragmenting it, then 
    spawnining a pool of threads to process it, and finally reconstructing it.
    
Input:
    -Image
Output:
    - wiki_final_im : image after a parallel Wikipedia's algorithm
    - meanStd_final_im : image after a parallel Mean and Standard Deviation algorithm 
    - ipl_final_im: image after a parallel IplImage algorithm
@author: Edoardo Foco

'''

import numpy as np
import Queue
import BlockThread


class ThreadController:
    
        
    def __init__(self,image):
        self.image = image
        self.windows = {}       #dictionary of windows
        self.wiki_windows = {}  #dictionary of resulting windows
        self.meanStd_windows = {}
        self.ipl_windows = {}
        self.window_height = 16 
        self.window_width = 16 
        
    
    def startThreading(self):
        '''Segments the image in windows of size 16x16, creates a queue
            of windows and processes it using a pool of threads
        '''
     
        # initialize queue
        queue = Queue.Queue()
       
        currentx = 0
        currenty = 0
        
        # divide image in windows
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
        for i in range(4): # change range to change number of threads
            t = BlockThread.BlockThread(queue,self.wiki_windows,self.meanStd_windows,self.ipl_windows)
            t.setDaemon(True)
            t.start()
        
        
        # insert windows in the queue   
        new_windows = self.windows.items()
        for window in new_windows:
            queue.put(window)
    
        
        queue.join()
           
        
    def reconstructImage(self):
        ''' Re-constructs Processed Image '''
       
        wiki_stacked_rows =[]
        meanStd_stacked_rows = []
        ipl_stacked_rows = []
        counter=0
        
        # constructing rows by stacking the windows horizontally
        for y in range (0,self.image.shape[0]/self.window_height):  
            wiki_row = []
            meanStd_row = []
            ipl_row = []
            for x in range (0,self.image.shape[1]/self.window_width):
                if x == 0:
                    wiki_row = self.wiki_windows[counter]
                    meanStd_row = self.meanStd_windows[counter]
                    ipl_row = self.ipl_windows[counter]
                    counter +=1
                else: 
                    wiki_row=np.hstack((wiki_row,self.wiki_windows[counter]))
                    meanStd_row=np.hstack((meanStd_row,self.meanStd_windows[counter]))
                    ipl_row=np.hstack((ipl_row,self.ipl_windows[counter]))
                    counter += 1
                # if it is considering the last window of the row then append to stacked_rows
                if x == self.image.shape[1]/self.window_width - 1:
                    wiki_stacked_rows.append(wiki_row)
                    meanStd_stacked_rows.append(meanStd_row)
                    ipl_stacked_rows.append(ipl_row)
        
        # constructing columns by stacking the rows vertically
        counter = 0
        for x in range (0,len(wiki_stacked_rows)):  # creating final image
                if counter == 0:
                    wiki_final_im=wiki_stacked_rows[0]
                    meanStd_final_im = meanStd_stacked_rows[0]
                    ipl_final_im = ipl_stacked_rows[0]
                    counter+=1
                else:
                    wiki_final_im=np.vstack((wiki_final_im,wiki_stacked_rows[x]))
                    meanStd_final_im = np.vstack((meanStd_final_im,meanStd_stacked_rows[x]))
                    ipl_final_im = np.vstack((ipl_final_im,ipl_stacked_rows[x]))
            
        
        return wiki_final_im,meanStd_final_im,ipl_final_im
    
        
    
