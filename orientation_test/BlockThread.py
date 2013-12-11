'''
Created on Mar 28, 2013

@author: Edoardo Foco
'''

import threading

import Orientation


class BlockThread(threading.Thread):

    
    def __init__(self, queue, n_windows):
        threading.Thread.__init__(self)
        self.queue = queue
        self.n_windows = n_windows

    def run(self):
        while True:
          
            print threading.currentThread().getName()
           
            # grabs window from queue
            # Note: win is a tuple [key, value], using dictionary data-structure
            win = self.queue.get()
           
            # Normalization
            #self.n_windows[win[0]] = WikiNorm.normalise(win[1])
            self.n_windows[win[0]] = win[1]
            
            # Orientation
            self.n_windows[win[0]] = Orientation.calculateOrientation(self.n_windows[win[0]])
            # signals queue job is done
            self.queue.task_done()
     
