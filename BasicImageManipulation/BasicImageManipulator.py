import sys
import numpy as np
import cv2
from PIL import Image



def rotate(image,sigma):
    r_image = image * sigma
    return r_image

def binarise(image,threshold):
    x0,y0 = np.where(image >= threshold)
    x1,y1 = np.where(image < threshold)
    bw_image = image
    bw_image[x0,y0] = 255
    bw_image[x1,y1] = 0
    return bw_image
    


    
if __name__ == '__main__':
    pass

if len(sys.argv) > 2:
    print "**Error: Invalid arguments.\nUsage: python main.py <filename>"
    sys.exit()

image_str = sys.argv[1]
length = len(image_str) - 4
file_extension = image_str[length:]

if not file_extension == ".png":
    print "**Error: Invalid file type.\nThe software supports only .png files"
    sys.exit()
    
image = cv2.imread(image_str, cv2.CV_LOAD_IMAGE_GRAYSCALE)
cv2.imshow('origi',image)
cv2.waitKey()
if image == None:
    print "**Error: File not found"
    sys.exit()
    
if not image.shape[0] == 480 and image.shape[1] == 640:
    print "**Error: Size of the image is not supported.\nSupported size: 480x640"
    sys.exit()


ask_input = True
while ask_input == True:
    var = str(raw_input("\nPress:\n'r' to execute a rotation\n'b' to execute a brightening operation\n'bw' to binarize the image\n'q' to quit the program\n"))
    
    if var == 'r':
        print 'not ready yet'
    if var == 'b':
        sigma = float(raw_input("\nInsert the brightening factor:\n"))
        r_image=rotate(image,sigma)
        Image.fromarray(image).show('Original Image')

        Image.fromarray(r_image).show()
    
    if var == 'bw':
        threshold = int(raw_input("\nInsert a threshold value:\n"))
        bw_image = binarise(image,threshold)
        Image.fromarray(image).show('Original Image')
        Image.fromarray(bw_image).show('Binarised Image')
    if var == 'q':
        ask_input = False
        

    elif not var == 'r' or var == 'b' or var == 'bw' or var == 'q':
      
        print "\nPlease insert a valid input"
    