'''
NormalizationSystem.py
Description:
    This system was designed to compare three different Normalization algorithms applied on the entire image
    and then in parallel on sub-images of size 16 X 16.
    
Usage:
    From command line:   python NormalizationSystem.py <filenename>
    
Output:
    -original image
    -wiki_im : image after wikipedia's normalization algorithm on the entire image
    -meanStd_im : image after Mean and Standard Deviation algorithm on the entire image
    -ipl_im : image after iplImage algorithm on the entire image
    -p_wiki_im : image after a parallel wikipedia algorithm
    -p_meanStd_im : image after a parallel Mean and Standard Deviation algorithm 
    -p_ipl_im : image after a parallel iplImage algorithm
    -Min and Max values for each resulting image (visible from command line)
    
Usage:
    From command line:   python NormalizationSystem.py <filename>
@author: Edoardo Foco
'''

import numpy as np
import cv2
import ThreadController
import WikiNorm
import MeanStd_Norm
import IplNorm
import sys
from PIL import Image

def main():
    
    image = validateInput()
    
    # Wiki Normalization
    wiki_im = WikiNorm.normalise(image)
    
    # MeanStd Normalization
    meanStd_im = MeanStd_Norm.normalise(image)
    
    # IplImage Normalization
    ipl_im = IplNorm.normalise(image)
    
    # Parallalel Normalizations
    controller = ThreadController.ThreadController(image)
    controller.startThreading()
    p_wiki_im, p_meanStd_im, p_ipl_im = controller.reconstructImage()
    
    showResults(image,wiki_im,meanStd_im,ipl_im,p_wiki_im,p_ipl_im,p_meanStd_im)
    sys.exit()
    
    
    
def validateInput():
    if not len(sys.argv) == 2:
        print "\n**Error: Invalid arguments.\nUsage: python main.py <filename>\n"
        sys.exit()
    
    image_str = sys.argv[1]
    if image_str == "-h":
        print "\nUsage:\npython NormalizationSystem.py <filename>\n"
        print "Supported File Formats: .png\n"
        print "The system is going to compute Wikipedia's, Mean and Standard Deviation, and IplImage normalization algorithms\n"
        sys.exit()
    
    length = len(image_str) - 4
    file_extension = image_str[length:]
    
    if not file_extension == ".png":
        print "\n**Error: Invalid file type.\nThe software supports only .png files\n"
        sys.exit()
   
    image = cv2.imread(image_str, cv2.CV_LOAD_IMAGE_GRAYSCALE)
    
    if image == None:
        print "\n**Error: File not found\n"
        sys.exit()
    
    if not image.shape[0] == 480:
        if not image.shape[1] == 640:
            print "\n**Error: Size of the image is not supported.\nSupported size: 640x480\n"
            sys.exit()
    
    return image



def showResults(image,wiki_im,meanStd_im,ipl_im,p_wiki_im,p_ipl_im,p_meanStd_im):
    print "The Normalization applied on the whole image using Wikipedia's algorithm returned an image who's: \nMin = ",np.min(wiki_im)," and Max = ",np.max(wiki_im)
    print "\nThe Normalization applied on the whole image using Means and Standard Deviation algorithm returned an image who's: \nMin = ",np.min(meanStd_im)," and Max = ",np.max(meanStd_im)
    print "\nThe Normalization applied on the whole image using the IplImage energy normalization algorithm returned an image who's: \nMin = ",np.min(ipl_im)," and Max = ",np.max(ipl_im)
    print "\nThe Normalization applied locally on blocks of 16 x 16 using Wikipedia's algorithm returned an image who's: \nMin = ",np.min(p_wiki_im)," and Max = ",np.max(p_wiki_im)
    print "\nThe Normalization applied locally on blocks of 16 x16 using Means and Standard Deviation algorithm returned an image who's: \nMin = ",np.min(p_meanStd_im)," and Max = ",np.max(p_meanStd_im)
    print "\nThe Normalization applied locally on blocks of 16 x 16 using the IplImage energy normalization algorithm returned an image who's: \nMin = ",np.min(p_ipl_im)," and Max = ",np.max(p_ipl_im)

    cv2.imshow('original', image)
    cv2.imshow('wiki_normalization', wiki_im)    
    cv2.imshow('meanStd_normalization', meanStd_im)
    cv2.imshow('ipl_normalization', ipl_im)
    cv2.imshow("p_wiki_normalization",p_wiki_im)
    cv2.imshow("p_ipl_normalization", p_ipl_im)
    cv2.imshow("p_meanStd_normalization", p_meanStd_im)

    cv2.waitKey()
                
    
if __name__=="__main__":
    main()
