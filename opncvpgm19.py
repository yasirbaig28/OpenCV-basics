# DRAWING in OpenCV

import cv2

image = cv2.imread('RGB.png')

image = cv2.line(image,(0,0),(1000,1000),(255,0,0),5)
image = cv2.circle(image,(200,200),200,(255,0,0),5)
image = cv2.rectangle(image,(100,100),(570,500),(255,0,0),5)
image = cv2.rectangle(image,(100,100),(200,200),(255,0,0),5)#square using rectrangle
cv2.imshow('Draw',image)
