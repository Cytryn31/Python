'''
Description:
    This is the creation of the actual thread which will process the given sub-image applying
    first a Normalization algorithm then a orientation estimation algorithm.
Input:
    - queue : Thread-safe data structure which controls the input
    - wiki_windows : Dictionary which controls the output
    - meanStd_windows : Dictionary which controls the output
    - ipl_windows : Dictionary which controls the output
@author: Edoardo Foco
'''

import threading
import WikiNorm
import MeanStd_Norm
import IplNorm

class BlockThread(threading.Thread):

    
    def __init__(self, queue, wiki_windows,meanStd_windows,ipl_windows):
        threading.Thread.__init__(self)
        self.queue = queue
        self.wiki_windows = wiki_windows
        self.meanStd_windows = meanStd_windows
        self.ipl_windows = ipl_windows
        

    def run(self):
        while True:
            # grabs window from queue
            # Note: win is a tuple [key, value], using dictionary data-structure
            win = self.queue.get()
             
            # Normalization
            self.wiki_windows[win[0]] = WikiNorm.normalise(win[1])
            self.meanStd_windows[win[0]]=MeanStd_Norm.normalise(win[1])
            self.ipl_windows[win[0]] = IplNorm.normalise(win[1])
            self.queue.task_done()
     
