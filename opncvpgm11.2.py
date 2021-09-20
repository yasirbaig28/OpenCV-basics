# Resizing Images

import cv2
image=cv2.imread('My signature.jpg')


resize_image = cv2.resize(image,(280,80))
cv2.imshow('img',resize_image)
cv2.imwrite('resized_signature.jpg',resize_image)
