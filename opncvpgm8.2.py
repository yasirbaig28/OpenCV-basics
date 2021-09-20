#Addition Operation  

import cv2

image1=cv2.imread('i3.png')
image2=cv2.imread('i4.png')


#cv2.imshow('img1',image1)
#cv2.imshow('img2',image2)

sum1=cv2.add(image1,image2)
cv2.imshow('sum',sum1)


    

