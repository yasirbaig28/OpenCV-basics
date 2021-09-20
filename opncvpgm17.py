# EDGE Finding
import cv2

image=cv2.imread('img1.png')
gray =cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray,30,200)
cv2.imshow('Edges',edges)
