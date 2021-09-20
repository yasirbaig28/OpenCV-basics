# Substraction Operation  

import cv2

image1=cv2.imread('a1.png')
image2=cv2.imread('a2.png')


#cv2.imshow('img1',image1)
#cv2.imshow('img2',image2)

sub1=cv2.subtract(image1,image2)
cv2.imshow('sub',sub1)


    

