'''
Description:
    This is the creation of the actual thread which will process the given sub-image applying
    first a Normalization algorithm then a orientation estimation algorithm.
Input:
    - queue : Thread-safe data structure which controls the input
    - n_windows : Dictionary which controls the output
    - o_windows : Dictionary which controls the output

@author: Edoardo Foco
'''

import threading
import MeanStd_Norm
import Orientation


class BlockThread(threading.Thread):

    
    def __init__(self, queue, n_windows, o_windows):
        threading.Thread.__init__(self)
        self.queue = queue
        self.n_windows = n_windows
        self.o_windows = o_windows

    def run(self):
        while True:
          
            # print threading.currentThread().getName()
           
            # grabs window from queue
            # Note: win is a tuple [key, value], using dictionary data-structure
            win = self.queue.get()
           
            # Normalization
            self.n_windows[win[0]] = MeanStd_Norm.normalise(win[1])
            
            # Orientation
            self.o_windows[win[0]],self.n_windows[win[0]] = Orientation.Orientation(self.n_windows[win[0]]).calculateOrientation()
            
            # signals queue job is done
            self.queue.task_done()
     
