import cv2
import numpy as np
path = 'Resources/skills.png'
img = cv2.imread(path)

cv2.imshow("Original", img)
cv2.waitKey(0)