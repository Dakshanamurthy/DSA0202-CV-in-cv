import cv2
import numpy as np
img = cv2.imread("C:/Users/Roshan/OneDrive/Pictures/animals-1663825597439-9977.jpg")
blur = cv2.GaussianBlur(img, (5, 5), 0)
cv2.imshow("Original", img)
cv2.imshow("Blurred", blur)
cv2.waitKey(0)
