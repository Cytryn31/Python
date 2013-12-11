The main executable is SobelEdgeDetection.py

Description:
    The software will apply Sobel's Edge detection algorithm to a given image.
    The algorithm includes:
        - Gaussian Blurring
        - Sobel Filter
        - Thresholding
    
Input:
    - image : path to image
    - Gauss Sigma (float)
    - Window Size (int)
    - Threshold Value (int)
    
Output:
    - blurred_im (image)
    - grad_x (image)
    - grad_y (image)
    - edge_im (image)
    
Usage:
    From command line:   python SobelEdgeDetection.py <image>

Notes:
	The FVC Database 1 is provided int he 'db' folder
    
@author: Edoardo Foco