The main executable is NormalizationSystem.py

Description:
    This system was designed to compare three different Normalization algorithms applied on the entire image
    and then in parallel on sub-images of size 16 X 16.
    
Usage:
    From command line:   python NormalizationSystem.py <filenename>
    
Input:
    -image
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

Notes:
    The FVC database is provided in the 'db' folder

@author: Edoardo Foco
