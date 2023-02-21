# Insert your code in part1/p1_opencv_code.cpp
# Edit the file extension and web template to match your programming language.

# 1. Write a program that uses basic morphological operations to identify and mark all vertical lines in the empty
# grid image. The result image should contain only the vertical lines. Then, write another program to detect only
# the vertical lines. Edit the web template to display your result images and the computer code that was used to
# generate it for this and all subsequent parts. You must solve part1 using Matlab and OpenCV.

import cv2
import numpy

raw_img = cv2.imread("image_part1b.png")
raw_img = cv2.cvtColor(raw_img, cv2.COLOR_BGR2GRAY)
_, img = cv2.threshold(raw_img, 215, 255, 0)
img = ~img

kernel_horizontal = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 1))

horizontal = cv2.erode(img, kernel_horizontal)
horizontal = cv2.dilate(horizontal, kernel_horizontal)

kernel_vertical = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 29))

vertical = cv2.erode(img, kernel_vertical)
vertical = cv2.dilate(vertical, kernel_vertical)

cv2.imshow("Vertical", vertical)
cv2.imshow("Horizontal", horizontal)
cv2.waitKey(5000)
