# 1. Write a program that uses basic morphological operations to identify and mark all vertical lines in the empty
# grid image. The result image should contain only the vertical lines. Then, write another program to detect only
# the vertical lines. Edit the web template to display your result images and the computer code that was used to
# generate it for this and all subsequent parts. You must solve part1 using Matlab and OpenCV.

import cv2
import numpy

raw_img = cv2.imread("images/image_part1b.png")
raw_img = cv2.cvtColor(raw_img, cv2.COLOR_BGR2GRAY)
_, img = cv2.threshold(raw_img, 215, 255, 0)
img = ~img

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 1))

horizontal = cv2.erode(img, kernel)
horizontal = cv2.dilate(horizontal, kernel)

cv2.imshow("vertical", horizontal)
cv2.waitKey(5000)
