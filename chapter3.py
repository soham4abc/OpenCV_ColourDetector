import cv2
import numpy as np

img = cv2.imread("Resources/download.png")

cv2.imshow("Image",img)
print(img.shape)

imgResize = cv2.resize(img,(300,200))
imgCropped=img[0:200,0:100]
cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped",imgCropped)
print(imgResize.shape)

cv2.waitKey(0)
