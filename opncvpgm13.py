# Erosion of image in openCV Morphological Image Processing

import cv2
import numpy as np

image=cv2.imread('a2.png')

#create a kernel
kernel= np.ones((90,90),np.uint8)

#print(kernel)
#cv2.imshow('Kernel',kernel)

#for erosion
erosion = cv2.erode(image,kernel)
cv2.imshow('Eroded Image',erosion)
