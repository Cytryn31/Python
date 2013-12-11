import Orientation
import numpy as np
import cv2
from PIL import Image
import ThreadController

image = cv2.imread('circle_test.png', cv2.CV_LOAD_IMAGE_GRAYSCALE)
print 'hi'
controller = ThreadController.ThreadController(image)
controller.start_threading()

oriented_im = controller.reconstruct_image()

Image.fromarray(oriented_im).show()
cv2.imshow('oriented,im', oriented_im)
cv2.waitKey()