# THRESHOLDING

import cv2

image = cv2.imread('BP.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow('Gray image',gray)

# BINARY THRESHOLDING
ret,thresh1 = cv2.threshold(gray,120,255,cv2.THRESH_BINARY)
cv2.imshow('binarythresh1',thresh1)

# INVERTED BINART THRESHOLDING
ret,thresh1 = cv2.threshold(gray,120,255,cv2.THRESH_BINARY_INV)
cv2.imshow('Inverted binary thresh1',thresh1)

# TRUNCATED THRESHOLDING
ret,thresh1 = cv2.threshold(gray,120,255,cv2.THRESH_TRUNC)
cv2.imshow('Truncated thresh1',thresh1)

# TO ZERO THRESHOLDING
ret,thresh1 = cv2.threshold(gray,120,255,cv2.THRESH_TOZERO)
cv2.imshow('To zero thresh1',thresh1)

# TO ZERO INVERTED THRESHOLDING
ret,thresh1 = cv2.threshold(gray,120,255,cv2.THRESH_TOZERO_INV)
cv2.imshow('To zero inverted thresh1',thresh1)
