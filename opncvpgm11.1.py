# Resizing Images

import cv2
image=cv2.imread('exp1.jpg')


resize_image = cv2.resize(image,(504,404))
cv2.imshow('img',resize_image)
