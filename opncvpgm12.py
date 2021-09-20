# INTERPOLATING in Resizing Images

import cv2
image=cv2.imread('RGB.png')


#resize_image = cv2.resize(image,(600,600),interpolation = cv2.INTER_AREA)
#resize_image = cv2.resize(image,(600,600),interpolation = cv2.INTER_LINEAR)
#resize_image = cv2.resize(image,(600,600),interpolation = cv2.INTER_CUBIC)
cv2.imshow('img',resize_image)

