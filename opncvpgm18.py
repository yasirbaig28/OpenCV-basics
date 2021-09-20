# Countouring

import cv2

image=cv2.imread('ironman.png')

edges = cv2.Canny(image,30,200)
cv2.imshow('Edges',edges)

contours, hierarchy = cv2.findContours(edges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

cv2.drawContours(image,contours,-1,(0,0,255),3)
cv2.imshow('Contour',image)
print(hierarchy)
