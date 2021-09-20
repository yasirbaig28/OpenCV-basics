#Splitting image of png format 1
import cv2

image=cv2.imread('python.png')

#print(image)
#cv2.imshow('image of RGB',image)

B,G,R =cv2.split(image)
#print(G)

cv2.imshow('red',R)
