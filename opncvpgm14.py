# DILATION of image in openCV Morphological Image Processing

import cv2
import numpy as np

image=cv2.imread('a2.png')

#create a kernel
kernel= np.ones((100,100),np.uint8)

#print(kernel)
#cv2.imshow('Kernel',kernel)

#for erosion
dilation = cv2.dilate(image,kernel)
cv2.imshow('Dilated Image',dilation)
