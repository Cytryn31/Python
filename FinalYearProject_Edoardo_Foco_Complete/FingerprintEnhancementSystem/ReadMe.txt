The main executable is FingerprintEnhancementSystem.py

Description:
    The software processes the image in parallel. It currently supports .png images
    of size 640x480. It will apply a Normalization algorithm and a Ridge Orientation
    algorithm to each 16x16 block of the fingerprint image.
    
    This system is not complete and is missing:
        - Frequency Estimation Algorithm
        - Gabor Filter
        - Binarization
        - Thinning
    
Input:
    -image
Usage:
    From command line:   python FingerprintEnhancementSystem.py <filename>

Notes:
    The FVC database is provided in the 'db' folder

@author: Edoardo Foco
