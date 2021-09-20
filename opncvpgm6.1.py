#Splitting image of png format
import cv2

image=cv2.imread('RGB.png')

#print(image)
#cv2.imshow('image of RGB',image)

B,G,R =cv2.split(image)
#print(G)

cv2.imshow('green',G)
