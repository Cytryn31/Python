'''
FingerprintEnhancementSystem.py
Description:
    The software processes the image in parallel. It currently supports .png images
    of size 640x480. It will apply a Normalization algorithm and a Ridge Orientation
    algorithm to each 16x16 block of the fingerprint image.
    
    This system is not complete and is missing:
        - Frequency Estimation Algorithm
        - Gabor Filter
        - Binarization
        - Thinning
    

Usage:
    From command line:   python FingerprintEnhancementSystem.py <filename>

@author: Edoardo Foco
'''


import sys
import cv2
import ThreadController
from PIL import Image
import time


def main():
     
    image = validateInput()
    
    # process image
    start_time = time.time()
    controller = ThreadController.ThreadController(image)
    controller.start_threading()
    # orient_im is the orientation image neede for the Gabor Filter. It is not used because the software is not complete
    orient_im, processed_image = controller.reconstruct_image()
    elapsed_time = time.time() - start_time
    print elapsed_time
    
    cv2.imshow('original image',image)
    Image.fromarray(processed_image).show()
    cv2.imshow('proc_image', processed_image)
    cv2.waitKey()
    
    sys.exit()
    
def validateInput():
    if len(sys.argv) > 2:
        print "**Error: Invalid arguments.\nUsage: python main.py <filename>"
        sys.exit()
    
    image_str = sys.argv[1]
    if image_str == "-h":
        print "\nUsage:\npython FingerprintEnhacementSystem.py <filename>\n"
        print "Supported File Formats: .png\n"
        print "The system is going to compute an Enhancement algorithm on the image\n"
        sys.exit()
    
    
    length = len(image_str) - 4
    file_extension = image_str[length:]
    
    if not file_extension == ".png":
        print "**Error: Invalid file type.\nThe software supports only .png files"
        sys.exit()
        
   
    image = cv2.imread(image_str, cv2.CV_LOAD_IMAGE_GRAYSCALE)
    if image == None:
        print "**Error: File not found"
        sys.exit()
        
    if not image.shape[0] == 480:
        if not image.shape[1] == 640:
            print "\n**Error: Size of the image is not supported.\nSupported size: 640x480\n"
            sys.exit()
   
    return image
    
if __name__=="__main__":
    main()